import logging
import sqlite3

from .config import db, use_db, tables


def get_connection():
    db_loc = db[use_db]['host']
    conn = None
    try:
        conn = sqlite3.connect(db_loc)
        logging.debug('Connected to %s', db_loc)
    except sqlite3.OperationalError as e:
        logging.critical('Could not connect to %s: %s', db_loc, str(e))
    return conn


def execute_select(stmt):
    conn = get_connection()
    c = conn.cursor()
    logging.debug('Executing %s', stmt)
    c.execute(stmt)
    logging.debug('Executing %s', stmt)
    results = c.fetchall()
    conn.close()
    return results


def all_subjects_for_class(class_id):
    stmt = 'SELECT `vtuID` FROM `class` WHERE `classID` = ' + str(class_id)
    return execute_select(stmt=stmt)


def get_subject_by_id(sub_id):
    stmt = 'SELECT `vtuID` FROM `class` WHERE `id` = ' + str(sub_id)
    return execute_select(stmt=stmt)


def recreate_db():
    conn = get_connection()
    c = conn.cursor()

    for table in tables:
        stmt = 'DROP TABLE IF EXISTS ' + tables[table]['name']
        logging.info('Dropping table %s', tables[table]['name'])
        c.execute(stmt)
        stmt = 'CREATE TABLE ' + tables[table]['name'] + '('
        for column in tables[table]['columns']:
            stmt = stmt + column + ','
        stmt = stmt[:-1] + ')'
        logging.info('Creating table %s', tables[table]['name'])
        logging.debug(stmt)
        c.execute(stmt)

    conn.commit()
    conn.close()


def execute_update(stmt):
    conn = get_connection()
    c = conn.cursor()
    logging.debug('Executing %s', stmt)
    c.execute(stmt)
    conn.commit()
    conn.close()


def add_subject_to_class(sub_id, class_id):
    stmt = 'INSERT INTO `class`(`vtuID`,`classID`) VALUES(' + str(sub_id) + ',' + str(class_id) + ')'
    execute_update(stmt=stmt)


def all_classes():
    stmt = 'SELECT DISTINCT `classID` FROM `class`'
    return execute_select(stmt=stmt)


def stud_name_for_id(vtu_id):
    stmt = 'SELECT `studName` FROM `student` WHERE `vtuID` =' + str(vtu_id)
    name = execute_select(stmt)
    return name[0][0]


def class_name_for_id(class_id):
    stmt = 'SELECT `className` FROM `courses` WHERE `classID` =' + str(class_id)
    name = execute_select(stmt)
    return name[0][0]


def add_student(vtu_id, stud_name):
    stmt = 'INSERT INTO `student`(`vtuID`,`studName`) VALUES(' + str(vtu_id) + ',' + str(stud_name) + ')'
    execute_update(stmt=stmt)


def add_course(course_id, course_name):
    stmt = 'INSERT INTO `courses`(`classID`,`className`) VALUES(' + str(course_id) + ',' + str(course_name) + ')'
    execute_update(stmt=stmt)


def add_attendance(course_id, vtu_id, hour_id):
    stmt = 'INSERT INTO `attendance`(`classID`,`vtuID`,`hourID`) VALUES(' + str(course_id) + ',' + str(
        vtu_id) + ',' + str(hour_id) + ')'
    execute_update(stmt=stmt)
