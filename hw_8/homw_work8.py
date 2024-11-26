import sqlite3



def create_tables(db_name, sql_create_tables):
    try:
        with sqlite3.connect(db_name) as conn:
            cusrsor = conn.cursor()
            cusrsor.execute(sql_create_tables)
    except sqlite3.Error as error:
        print(error)


sql_create_table_c = '''
CREATE TABLE country(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(50) NOT NULL)'''


sql_create_table_city = '''
CREATE  TABLE city(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(50) NOT NULL,
area FLOAT NOT NULL DEFAULT NULL,
country_id INTEGER NOT NULL REFERENCES country(id))'''

sql_create_table_stu = '''
CREATE TABLE students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
city_id INTEGER NOT NULL REFERENCES city(id))'''

def insert_country(db_name, country):
    sql = '''INSERT INTO country 
             (title)
             VALUES (?)'''
    try:
        with sqlite3.connect(db_name) as conn:
            cusrsor = conn.cursor()
            cusrsor.execute(sql, country)
    except sqlite3.Error as error:
        print(error)


def insert_city(db_name, citys):
    sql = '''INSERT INTO city 
             (title, area, country_id)
             VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as conn:
            cusrsor = conn.cursor()
            cusrsor.execute(sql, citys)
    except sqlite3.Error as error:
        print(error)

def insert_student(db_name, student):
    sql = '''INSERT INTO students
    ( first_name, last_name, city_id)
    VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as conn:
            cusrsor = conn.cursor()
            cusrsor.execute(sql, student)
    except sqlite3.Error as error:
        print(error)

def add_student():
    insert_student(database_name, ('Alex', 'Messer', 2))
    insert_student(database_name, ('Olivia', 'Taylor', 1))
    insert_student(database_name, ('Liam', 'Brown', 3))
    insert_student(database_name, ('Emma', 'Wilson', 2))
    insert_student(database_name, ('Noah', 'Johnson', 1))
    insert_student(database_name, ('Sophia', 'Clark', 3))
    insert_student(database_name, ('Lucas', 'Lee', 2))
    insert_student(database_name, ('Mia', 'Walker', 1))
    insert_student(database_name, ('Ethan', 'Hall', 3))
    insert_student(database_name, ('Ava', 'Lewis', 2))
    insert_student(database_name, ('James', 'Young', 1))
    insert_student(database_name, ('Isabella', 'King', 3))
    insert_student(database_name, ('Benjamin', 'Wright', 2))
    insert_student(database_name, ('Charlotte', 'Hill', 1))
    insert_student(database_name, ('Elijah', 'Scott', 3))





database_name = 'homw8.db'

# create_tables(database_name, sql_create_table_c)
# insert_country(database_name, ('Russia',))
# insert_country(database_name, ('Usa',))
# insert_country(database_name, ('Serbia',))
# create_tables(database_name, sql_create_table_city)
# insert_city(database_name,('Moscow', '2511000000 ', 1))
# insert_city(database_name,('Saint Petersburg', '1439000000 ', 1))
# insert_city(database_name,('Krasnodar', '339000000 ', 1))
# insert_city(database_name, ('Washington', '177000000', 2))
# insert_city(database_name, ('Miami', '143000000', 2))
# insert_city(database_name, ('Belgrad', '3234000000', 3))
# insert_city(database_name, ('Bor', '856000000', 3))
# create_tables(database_name, sql_create_table_stu)
# add_student()


