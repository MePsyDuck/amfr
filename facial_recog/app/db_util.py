import sqlite3

from facial_recog.app.config import db, default_db, tables


def get_connection():
    conn = sqlite3.connect(db[default_db]['host'])
    return conn


def execute_select(stmt):
    conn = get_connection()
    c = conn.cursor()
    c.execute(stmt)
    results = c.fetchall()
    conn.close()
    return results


def all_subjects_for_class(class_id):
    stmt = "SELECT `vtuID` FROM `class` WHERE `classID` = " + str(class_id)
    return execute_select(stmt=stmt)


def recreate_db():
    conn = get_connection()
    c = conn.cursor()

    for table in tables:
        stmt = "DROP TABLE IF EXISTS " + tables[table]['name']
        c.execute(stmt)
        stmt = "CREATE TABLE " + tables[table]['name'] + "("
        for column in tables[table]['columns']:
            stmt = stmt + column + ","
        stmt = stmt[:-1] + ")"
        c.execute(stmt)

    conn.commit()
    conn.close()