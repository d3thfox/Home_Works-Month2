#-*- coding: utf-8 -*-
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
sql_create_table_prod = '''
CREATE TABLE products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(150),
category_code VARCHAR(2) REFERENCES categories(code),
untit_price FLOAT NOT NULL DEFAULT 0,
stock_quantity INTEGER NOT NULL DEFAULT 0,
store_id INTEGER REFERENCES store(store_id),)'''

sql_create_table_store = '''
CREATE TABLE stores(
store_id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(100))'''


def insert_categories(db_name, sql_insert_categories):
    sql = '''INSERT INTO categories(code,title) VALUES(?, ?)'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, sql_insert_categories)
    except sqlite3.Error as error:
        print(error)

def insert_products(db_name, sql_insert_products):
    sql = '''INSERT INTO products(title,untit_price,stock_quantity,category_code,store_id) 
             VALUES(?, ?,?,?,?)'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, sql_insert_products)
    except sqlite3.Error as error:
        print(error)

def insert_stores(db_name, sql_insert_stores):
    sql = '''INSERT INTO stores(title) VALUES(?)'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, sql_insert_stores)
    except sqlite3.Error as error:
        print(error)


def select_store(db_name):
    sql = '''SELECT * FROM stores'''
    try:
        with sqlite3.connect(db_name) as conn:
            cur = conn.cursor()
            cur.execute(sql)
            store = cur.fetchall()
            for row in store:
                print(f'ID: {row[0]}, Title: {row[1]}')

    except sqlite3.Error as error:
        print(error)

def select_products(db_name, id):
    sql = '''SELECT * FROM products
    JOIN stores ON products.store_id = stores.store_id
    WHERE stores.store_id = ?
    '''
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        cur.execute(sql, (id,))
        products = cur.fetchall()
        for row in products:
            print(f'ID: {row[0]}, Title: {row[1]}, Code: {row[2]}, Price: {row[3]}, Stock: {row[4]}')




def product_list():
    print('Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже,'
          ' для выхода из программы введите цифру 0')
    select_store(database_name)
    user_id = int(input('Введите ваш айди'))
    select_products(database_name, user_id)


database_name = 'exs.db'


# create_tables(database_name, sql_create_table_ca)
# create_tables(database_name, sql_create_table_prod)
# create_tables(database_name, sql_create_table_store)
# insert_categories(database_name,('pcc','pc_component'))
# insert_categories(database_name,('ff','fast food'))
# insert_categories(database_name,('cp', 'construction products'))
# insert_stores(database_name,('gamestore',))
# insert_stores(database_name,('mack',))
# insert_stores(database_name,('helmet',))
# insert_products(database_name, ('RAZER OPUS X','5.990',10,'pcc',1))
# insert_products(database_name, ('ASUS TUF GAMING','7.500',6,'pcc',1))
# insert_products(database_name, ('potato free','150.0',100,'ff',2))
# insert_products(database_name, ('coca cola','70.0',150,'ff',2))
# insert_products(database_name, ('cement','370.0',50,'cp',3))
# insert_products(database_name, ('concrete mixer','22000.0',5,'cp',3))


product_list()