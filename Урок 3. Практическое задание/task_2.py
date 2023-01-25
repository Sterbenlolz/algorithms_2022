"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""


import hashlib, mysql.connector

def password_validation():
    login = input('please enter your nickname: ')
    first_pw = input('please enter a password: ')
    try:
        cnx = mysql.connector.connect(user = 'root', password = '12345', host = '127.0.0.1', port = 3306, database = 'password_db')
        cursor = cnx.cursor()
        cursor.execute('select pw_hash from nicknames;')
        res = cursor.fetchall()
        if str(hashlib.sha256(login.encode() + first_pw.encode()).hexdigest()) in [item for t in res for item in t]:
            verify_pw = input('please verify your password: ')
            if str(hashlib.sha256(login.encode() + verify_pw.encode()).hexdigest()) in [item for t in res for item in t]:
                print('you have successfully logged in!')
                cursor.close()
                cnx.close()
            else:
                cursor.close()
                cnx.close()
                return print('verification passwords do not match, please try again.'), password_validation()
        else:
            cursor.close()
            cnx.close()
            return print('your login information was incorrect. please try again\n'), password_validation()
    except mysql.connector.errors.Error:
        return print('your login information was incorrect. please try again\n'), password_validation()


def registration():
    login = input('please enter your nickname: ')
    first_pw = input('please enter a password: ')
    try:
        cnx = mysql.connector.connect(user = 'root', password = '12345', host = '127.0.0.1', port = 3306, database = 'password_db')
        cursor = cnx.cursor(buffered = True)
        cursor.execute('select login from nicknames;')
        res = cursor.fetchall()
        if login not in [item for t in res for item in t]:
            verify_pw = input('please verify your password: ')
            if str(verify_pw) == str(first_pw):
                cursor.execute(f'insert into nicknames (login, pw_hash) values ("{login}", '
                               f'"{hashlib.sha256(login.encode() + first_pw.encode()).hexdigest()}")')
                print('you have successfully registered!\n')
                cnx.commit()
            else:
                cursor.close()
                cnx.close()
                return print('verification passwords do not match, please try again.\n'), registration()
        else:
            cursor.close()
            cnx.close()
            return print('this login already exists. please try again.\n'), registration()
        cursor.close()
        cnx.close()
    except mysql.connector.errors.Error:
        return print('something went wrong. please try again\n'), registration()


registration()
password_validation()