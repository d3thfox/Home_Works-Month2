import sqlite3


def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as error:
        print(error)


def insert_product(db_name, products):
    sql = '''INSERT INTO products
    (title_product, price, quantity)
    VALUES (?, ?, ?)
    '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, products)
    except sqlite3.Error as error:
        print(error)


def update_quantity(db_name, id, new_quantity):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (new_quantity, id))
    except sqlite3.Error as error:
        print(error)


def update_price(db_name, id, new_price):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connected:
            cursor = connected.cursor()
            cursor.execute(sql, (new_price, id))
    except sqlite3.Error as error:
        print(error)


def delete_product(db_name, id):
    sql = '''DELETE FROM products WHERE id = ? '''
    try:
        with sqlite3.connect(db_name) as connected:
            cursor = connected.cursor()
            cursor.execute(sql, (id,))
    except sqlite3.Error as error:
        print(error)


def print_all_products(db_name):
    sql = '''SELECT * FROM products'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            for row in cursor:
                print(row)
    except sqlite3.Error as error:
      print(error)


def select_limit_product(db_name, price_limit, quantity_limit):
    sql = '''SELECT * FROM products WHERE price < ? AND quantity  > ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql,(price_limit, quantity_limit))
            for row in cursor:
                print(row)
    except sqlite3.Error as error:
        print(error)



def select_product_name(db_name,name):
    sql = '''SELECT * FROM products WHERE title_product LIKE ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql,(f'%{name}%',))
            for row in cursor:
                print(row)
    except sqlite3.Error as error:
        print(error)


def add_product():
    insert_product(database_name, ('ASUS ROG Chakram Core', '7999.0', 10))
    insert_product(database_name, ('Logitech G Pro X Superlight', '9990.0', 15))
    insert_product(database_name, ('Razer DeathAdder V2', '6490.0', 12))
    insert_product(database_name, ('SteelSeries Rival 3', '3990.0', 20))
    insert_product(database_name, ('Zowie EC2', '7490.0', 8))
    insert_product(database_name, ('Corsair Harpoon RGB Wireless', '4990.0', 25))
    insert_product(database_name, ('HyperX Pulsefire Haste', '5990.0', 30))
    insert_product(database_name, ('Glorious Model O', '6990.0', 18))
    insert_product(database_name, ('Microsoft Classic IntelliMouse', '3490.0', 14))
    insert_product(database_name, ('Cooler Master MM720', '4490.0', 10))
    insert_product(database_name, ('Logitech G502 Hero', '6990.0', 22))
    insert_product(database_name, ('Roccat Kone AIMO', '8490.0', 12))
    insert_product(database_name, ('ASUS TUF Gaming M3', '2990.0', 40))
    insert_product(database_name, ('Redragon M711 Cobra', '3290.0', 35))
    insert_product(database_name, ('Razer Naga X', '8990.0', 9))
    insert_product(database_name, ('Corsair Scimitar RGB Elite', '9490.0', 5))


create_product_table_sql = '''
CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title_product VARCHAR(200) NOT NULL,
    price FLOAT(10,2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0)
    '''

database_name = 'hw.db'

# create_table(database_name, create_product_table_sql)
# add_product()
# update_quantity(database_name, 1, '100')
# update_price(database_name, 3, 10000.0)
# delete_product(database_name, 5)
# print_all_products(database_name)
# select_limit_product(database_name, '10000.0', 10)
# select_product_name(database_name, 'ASUS')

