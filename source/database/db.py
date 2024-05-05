# Подключение к базе данных SQLite
import sqlite3
from source.log import logging

#db_path = "source/database/main_db.db"
db_path = "source/database/"


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
                                user_name TEXT,
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
                                shirina_mej_sm REAL,
                                kol_sem_sht REAL,
                                rasxod_sem REAL,
                                ploshad_ga REAL,
                                massa_1000 REAL,
                                status INTEGER,
                                msg_id INTEGER)''')
            logging.info(f'[DB] таблица user создался | {db_path}users/{user_id}.db')
            conn.commit()
            conn.close()
        except Exception as my_bot_error:
            logging.error(f'[DB] create_table_user, Ошибка: {my_bot_error}')


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

def add_userid_main_db(user_id, user_name):
    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect(f'{db_path}main_db.db')
        cursor = conn.cursor()
        # Запись userid в базу данных SQLite
        cursor.execute("INSERT INTO users (user_id, user_name, status) VALUES (?,?,?)", (user_id,user_name,0))
        conn.commit()
        conn.close()
    except Exception as e:
        logging.error(f'[DB] add_userid_main_db, Ошибка: {e}')

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

def is_allowed(user_id):
    allowed = None
    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect(f'{db_path}main_db.db')
        cursor = conn.cursor()
        # Проверка наличия user_id в таблице users
        cursor.execute("SELECT * FROM users WHERE user_id=? AND status = 1 ", (user_id,))
        result = cursor.fetchone()
        if result:
            allowed = result[0]
        else:
            allowed = None
        #print (allowed) #debug
        conn.close()
        logging.info('[DB] is_allowed | Информация получена')
    except Exception as e:
        logging.error(f'[DB] is_allowed, Ошибка: {e}')
    return allowed

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

def user_allow(user_id, status):
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect(f'{db_path}main_db.db')
        cursor = conn.cursor()
        # Изменяем статус пользователя
        cursor.execute("UPDATE users SET status = ? WHERE user_id = ?", (status,user_id))
        # Сохраняем изменения
        conn.commit()
        # Закрываем соединение
        conn.close()
        logging.info(f'[DB] user_allow | status {user_id} изменен на {status}')
    except Exception as e:
        logging.error(f'[DB] user_allow, Ошибка: {e}')

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
    return float(result)

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
    return float(result)

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
    return float(result)

def set_rasxod_sem(user_id, rasxod_sem):
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # Изменяем статус пользователя
        cursor.execute("UPDATE user SET rasxod_sem = ? WHERE user_id = ?", (rasxod_sem, user_id))
        # Сохраняем изменения
        conn.commit()
        # Закрываем соединение
        conn.close()
        logging.info(f'[DB] set_rasxod_sem | ID: {user_id} | Внес данные {rasxod_sem}')
    except Exception as e:
        logging.error(f'[DB] set_rasxod_sem, Ошибка: {e}')

def get_rasxod_sem(user_id):
    result = None
    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # получаем статус 
        cursor.execute("SELECT rasxod_sem FROM user WHERE user_id=?", (user_id,))
        raw = cursor.fetchone()
        if raw:
            result = raw[0]
        else:
            result = None
        #print (status) #debug
        conn.close()
        logging.info(f'[DB] get_rasxod_sem | ID: {user_id}, rasxod_sem: {result}')
    except Exception as e:
        logging.error(f'[DB] get_rasxod_sem, Ошибка: {e}')
    return float(result)

def set_ploshad_ga(user_id, ploshad_ga):
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # Изменяем статус пользователя
        cursor.execute("UPDATE user SET ploshad_ga = ? WHERE user_id = ?", (ploshad_ga, user_id))
        # Сохраняем изменения
        conn.commit()
        # Закрываем соединение
        conn.close()
        logging.info(f'[DB] set_ploshad_ga | ID: {user_id} | Внес данные {ploshad_ga}')
    except Exception as e:
        logging.error(f'[DB] set_ploshad_ga, Ошибка: {e}')

def get_ploshad_ga(user_id):
    result = None
    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # получаем статус 
        cursor.execute("SELECT ploshad_ga FROM user WHERE user_id=?", (user_id,))
        raw = cursor.fetchone()
        if raw:
            result = raw[0]
        else:
            result = None
        #print (status) #debug
        conn.close()
        logging.info(f'[DB] get_ploshad_ga | ID: {user_id}, ploshad_ga: {result}')
    except Exception as e:
        logging.error(f'[DB] get_ploshad_ga, Ошибка: {e}')
    return float(result)

def get_method_2(user_id):
    result = None
    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # получаем статус 
        cursor.execute("SELECT rasxod_sem, ploshad_ga, massa_1000 FROM user WHERE user_id=?", (user_id,))
        raw = cursor.fetchone()
        if raw:
            result = raw
        else:
            result = None
        #print (result) #debug
        conn.close()
        logging.info(f'[DB] get_method_2 | ID: {user_id}, method_2: {result}')
    except Exception as e:
        logging.error(f'[DB] get_method_2, Ошибка: {e}')
    return result

def get_method_3(user_id):
    result = None
    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect(f'{db_path}users/{user_id}.db')
        cursor = conn.cursor()
        # получаем статус 
        cursor.execute("SELECT massa_1000, kol_sem_sht FROM user WHERE user_id=?", (user_id,))
        raw = cursor.fetchone()
        if raw:
            result = raw
        else:
            result = None
        #print (result) #debug
        conn.close()
        logging.info(f'[DB] get_method_3 | ID: {user_id}, method_3: {result}')
    except Exception as e:
        logging.error(f'[DB] get_method_3, Ошибка: {e}')
    return result

def get_all_users():
    all_users = []
    try:
        # Подключение к базе данных SQLite
        conn = sqlite3.connect(f'{db_path}main_db.db')
        cursor = conn.cursor()
        # выполняем запрос 
        cursor.execute("SELECT user_id, user_name, status FROM users")
        # Получение результатов
        rows = cursor.fetchall()
        if rows:
            # Вывод результатов
            for row in rows:
                all_users.append(row)
        else:
            all_users = None
        conn.commit()
        conn.close()
        logging.info('[DB] all_users | Информация получена')
    except Exception as e:
        logging.error(f'[DB] all_users, Ошибка: {e}')
    return all_users

def set_ban(user_id, status):
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect(f'{db_path}main_db.db')
        cursor = conn.cursor()
        # Изменяем статус пользователя
        cursor.execute("UPDATE users SET status = ? WHERE user_id = ?", (status, user_id))
        # Сохраняем изменения
        conn.commit()
        # Закрываем соединение
        conn.close()
        logging.info(f'[DB] set_ban | ID: {user_id} | Бан: {status}')
    except Exception as e:
        logging.error(f'[DB] set_ban, Ошибка: {e}')