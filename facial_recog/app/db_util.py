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
        print(db_loc + e)
        logging.critical('Could not connect to %s', db_loc)
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
