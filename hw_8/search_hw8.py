#-*- coding: utf-8 -*-
import sqlite3


from hw_8.homw_work8 import database_name


def select_city(db_name):
    sql = "SELECT title,id FROM city"
    try:
        with sqlite3.connect(db_name) as conn:
            cur = conn.cursor()
            cur.execute(sql)
            cityes = cur.fetchall()
            for city in cityes:
                print(f'Город - {city[0]}, ID - {city[1]}')
    except sqlite3.Error as error:
       print(error)


def select_stu(db_name, c_id):
    sql = '''SELECT students.first_name, students.last_name,city.area
             FROM students
             JOIN city ON students.city_id = city.id
             WHERE city.id = ?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cur = conn.cursor()
            cur.execute(sql, (c_id,))
            students = cur.fetchall()

            if students:
                for student in students:
                    print(f"ИМЯ - {student[0]}, ФАМИЛИЯ - {student[1]} , Площадь города - {student[2]}")
            else:
                print("В данном городе нет студентов.")
    except sqlite3.Error as error:
        print(f"Ошибка базы данных: {error}")


def search_stu():
    try:
        while True:
            print('Вы можете отобразить список учеников по выбранному ID города из перечня городов ниже.')
            select_city(database_name)
            print('Для выхода из программы введите 0')

            user_val = input('Введите ID города: ')

            if user_val == '0':
                print('Выход из программы.')
                break

            if not user_val.isdigit():
                print('Некорректный ввод. Введите целое число.')
                continue

            user_val = int(user_val)

            select_stu(database_name, user_val)

    except ValueError as error:
        print(f"Ошибка: {error}")


search_stu()







