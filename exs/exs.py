import sqlite3

def create_tables(db_name, sql_create_tables):
  try:
      with sqlite3.connect(db_name) as conn:
          cursor = conn.cursor()
          cursor.execute(sql_create_tables)
  except sqlite3.Error as error:
         print(error)

sql_create_table_ca = '''
CREATE TABLE categories(
code VARCHAR(2) PRIMARY KEY,
title VARCHAR(150))
'''

database_name = 'exs.db'


create_tables(database_name, sql_create_table_ca)