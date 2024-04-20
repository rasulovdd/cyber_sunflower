# Подключение к базе данных SQLite
import sqlite3
from source.log import logging

#db_path = "source/database/main_db.db"
db_path = "source/database/"


def add_userid(user_id):
    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # Запись userid в базу данных SQLite
        cursor.execute("INSERT INTO user (user_id, status) VALUES (?,?)", (user_id,0))
        conn.commit()
        conn.close()
    except Exception as e:
        logging.error(f'[DB] add_userid, Ошибка: {e}')

def add_userid_main_db(user_id):
    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect(f'{db_path}main_db.db')
        cursor = conn.cursor()
        # Запись userid в базу данных SQLite
        cursor.execute("INSERT INTO users (user_id, status) VALUES (?,?)", (user_id,0))
        conn.commit()
        conn.close()
    except Exception as e:
        logging.error(f'[DB] add_userid_main_db, Ошибка: {e}')

def create_table_user(user_id):
    if user_id == "":
        try:
            # Подключение к базе данных SQLite
            conn = sqlite3.connect(f'{db_path}main_db.db')
            cursor = conn.cursor()
            # Создание таблицы, если она еще не создана
            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id BIGINT,
                                status INTEGER)''')
            logging.info(f'[DB] таблица users создался | {db_path}main_db.db')
            conn.commit()
            conn.close()
        except Exception as my_bot_error:
            logging.error(f'[DB] create_table_user, Ошибка: {my_bot_error}')
    else:
        try:
            # Подключение к базе данных SQLite
            conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
            cursor = conn.cursor()
            # Создание таблицы, если она еще не создана
            cursor.execute('''CREATE TABLE IF NOT EXISTS user (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id BIGINT,
                                shirina_mej_sm INTEGER,
                                kol_sem_sht INTEGER,
                                rasxod_sem INTEGER,
                                ploshad_ga INTEGER,
                                massa_1000 INTEGER,
                                status INTEGER,
                                msg_id INTEGER)''')
            logging.info(f'[DB] таблица user создался | {db_path}users/{user_id}.db')
            conn.commit()
            conn.close()
        except Exception as my_bot_error:
            logging.error(f'[DB] create_table_user, Ошибка: {my_bot_error}')
    
def is_registered(user_id):
    user_info = None
    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect(f'{db_path}main_db.db')
        cursor = conn.cursor()
        # Проверка наличия user_id в таблице users
        cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        result = cursor.fetchone()
        if result:
            user_info = result[0]
        else:
            user_info = None
        #print (result[1]) #debug
        conn.close()
        logging.info('[DB] is_registered | Информация получена')
    except Exception as e:
        logging.error(f'[DB] is_registered, Ошибка: {e}')
    return user_info

def set_status(user_id, status):
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # Изменяем статус пользователя
        cursor.execute("UPDATE user SET status = ? WHERE user_id = ?", (status,user_id))
        # Сохраняем изменения
        conn.commit()
        # Закрываем соединение
        conn.close()
        logging.info(f'[DB] set_status | status {user_id} изменен на {status}')
    except Exception as e:
        logging.error(f'[DB] set_status, Ошибка: {e}')

def get_status(user_id):
    status = None
    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # получаем статус 
        cursor.execute("SELECT status FROM user WHERE user_id=?", (user_id,))
        result = cursor.fetchone()
        if result:
            status = result[0]
        else:
            status = None
        #print (status) #debug
        conn.close()
        logging.info(f'[DB] get_status | ID: {user_id}, status: {status}')
    except Exception as e:
        logging.error(f'[DB] get_status, Ошибка: {e}')
    return status

def set_msg_id(user_id, msg_id, status):
    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # Запись msg_id
        cursor.execute("INSERT INTO user (msg_id, status) VALUES (?,?)", (msg_id,status))
        conn.commit()
        conn.close()
    except Exception as e:
        logging.error(f'[DB] set_msg_id, Ошибка: {e}')

def get_msg_id(user_id, status):
    msg_id = []
    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # выполняем запрос 
        cursor.execute("SELECT msg_id FROM user WHERE status=?", (status,))
        # Получение результатов
        rows = cursor.fetchall()
        if rows:
            # Вывод результатов
            for row in rows:
                msg_id.append(row[0])
        else:
            msg_id = None
        conn.commit()
        conn.close()
        logging.info(f'[DB] get_msg_id | ID: {user_id}, Информация получена')
    except Exception as e:
        logging.error(f'[DB] get_msg_id, Ошибка: {e}')
    return msg_id

def del_msg_id(user_id,status):
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # выполняем запрос 
        cursor.execute("DELETE FROM user WHERE status=?",(status,))
        # Сохраняем изменения
        conn.commit()
        # Закрываем соединение
        conn.close()
        logging.info(f'[DB] del_msg_id | ID: {user_id} очистил msg_id')
    except Exception as e:
        logging.error(f'[DB] del_msg_id, Ошибка: {e}')


def set_shirina_mej_sm(user_id, shirina_mej_sm):
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # Изменяем статус пользователя
        cursor.execute("UPDATE user SET shirina_mej_sm = ? WHERE user_id = ?", (shirina_mej_sm, user_id))
        # Сохраняем изменения
        conn.commit()
        # Закрываем соединение
        conn.close()
        logging.info(f'[DB] set_shirina_mej_sm | ID: {user_id} | Внес данные {shirina_mej_sm}')
    except Exception as e:
        logging.error(f'[DB] set_shirina_mej_sm, Ошибка: {e}')

def get_shirina_mej_sm(user_id):
    result = None
    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # получаем статус 
        cursor.execute("SELECT shirina_mej_sm FROM user WHERE user_id=?", (user_id,))
        raw = cursor.fetchone()
        if raw:
            result = raw[0]
        else:
            result = None
        #print (status) #debug
        conn.close()
        logging.info(f'[DB] get_shirina_mej_sm | ID: {user_id}, shirina_mej_sm: {result}')
    except Exception as e:
        logging.error(f'[DB] get_shirina_mej_sm, Ошибка: {e}')
    return result

def set_kol_sem_sht(user_id, kol_sem_sht):
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # Изменяем статус пользователя
        cursor.execute("UPDATE user SET kol_sem_sht = ? WHERE user_id = ?", (kol_sem_sht, user_id))
        # Сохраняем изменения
        conn.commit()
        # Закрываем соединение
        conn.close()
        logging.info(f'[DB] kol_sem_sht | ID: {user_id} | Внес данные {kol_sem_sht}')
    except Exception as e:
        logging.error(f'[DB] kol_sem_sht, Ошибка: {e}')

def get_kol_sem_sht(user_id):
    result = None
    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # получаем статус 
        cursor.execute("SELECT kol_sem_sht FROM user WHERE user_id=?", (user_id,))
        raw = cursor.fetchone()
        if raw:
            result = raw[0]
        else:
            result = None
        #print (status) #debug
        conn.close()
        logging.info(f'[DB] get_kol_sem_sht | ID: {user_id}, kol_sem_sht: {result}')
    except Exception as e:
        logging.error(f'[DB] get_kol_sem_sht, Ошибка: {e}')
    return result

def set_massa_1000(user_id, massa_1000):
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # Изменяем статус пользователя
        cursor.execute("UPDATE user SET massa_1000 = ? WHERE user_id = ?", (massa_1000, user_id))
        # Сохраняем изменения
        conn.commit()
        # Закрываем соединение
        conn.close()
        logging.info(f'[DB] set_massa_1000 | ID: {user_id} | Внес данные {massa_1000}')
    except Exception as e:
        logging.error(f'[DB] set_massa_1000, Ошибка: {e}')

def get_massa_1000(user_id):
    result = None
    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # получаем статус 
        cursor.execute("SELECT massa_1000 FROM user WHERE user_id=?", (user_id,))
        raw = cursor.fetchone()
        if raw:
            result = raw[0]
        else:
            result = None
        #print (status) #debug
        conn.close()
        logging.info(f'[DB] get_massa_1000 | ID: {user_id}, massa_1000: {result}')
    except Exception as e:
        logging.error(f'[DB] get_massa_1000, Ошибка: {e}')
    return result