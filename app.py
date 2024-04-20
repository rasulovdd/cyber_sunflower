import telebot
#from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from requests import get
from dotenv import load_dotenv
import os
from time import sleep
from source.keyboard import inline, reply
from source.database import db
from source.log import logging
from source.utils import is_int
load_dotenv()
   
#загружаем переменные из .env
api_tokken = os.getenv('api_tokken')
app_debug = os.getenv('debug_on')
#users_id_all = os.getenv('users_id')
#users_id = users_id_all.split(",")
my_host = os.getenv('my_host')
my_port = os.getenv('my_port')
bot_tokken = os.getenv('bot_tokken')
admins_id = os.getenv('admins_id')

bot_tokken = os.getenv('bot_tokken') #загружаем токкен бота из файла
Bot = telebot.TeleBot(bot_tokken) #назначаем токкен в телебот

# -----------------------------------------------------------------
Bot = telebot.TeleBot(bot_tokken) #назначаем токкен в телебот
Bot.delete_my_commands(scope=None, language_code=None)
Bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("start", "🏠 Главное меню"),
        telebot.types.BotCommand("id", "👤 Телеграм ID"),
        # telebot.types.BotCommand("test", "проверка работы бота")
    ],
)
# -----------------------------------------------------------------

#обработка команды start
@Bot.message_handler(commands=['start'])
def send_welcome(message):
    """Обрабатываем текстовые сообщения '/start' """
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    
    if db.is_registered(user_id):
        Bot.send_message(user_id, "Привет 🤝\nРад видеть снова\nВыберите функцию 👇")
        #показываем меню
        main_menyu(user_id)
        #обнуляем статус пользователя
        db.set_status(user_id,0)
    else:
        db.add_userid_main_db(user_id) #добавить user_id в общию базу
        #создаем таблицу users
        db.create_table_user(user_id)
        #добавляем туда id пользователя 
        db.add_userid(user_id) #добавить user_id в персональную базу
        Bot.send_message(user_id, "Привет 🤝\nВыберите функцию 👇", reply_markup=reply.keyboard("MAIN"))
        #показываем меню
        main_menyu(user_id)
        #уведомляем админа
        Bot.send_message(admins_id, 
                         f'✅ Новый пользователь\n<a href="tg://user?id={user_id}">{full_name}</a>', 
                         parse_mode='HTML')
        
    if app_debug == "1":
        logging.info(f'[BOT] [UserID: {user_id}] Сообщение отправлено')

#обработка команды test
@Bot.message_handler(commands=['test'])
def send_welcome(message):
    """Обрабатываем текстовые сообщения '/test' """
    user_id = message.from_user.id
    print (admins_id) #debug
    if int(user_id) == int(admins_id):
        msg_id=db.get_msg_id(user_id, 10)
        print (msg_id)

    

def main_menyu(user_id):
    msg_id = db.get_msg_id(user_id, 10)
    if msg_id:
        for msg in msg_id:
            Bot.delete_message(user_id, msg)  # удаляем сообщение
    #очищаем msg_id
    db.del_msg_id(user_id,10)

    method_1="Как узнать количество семян на гектар и расстояние между ними"
    method_2="Как узнать количество семянок на погонный метр"
    method_3="Как узнать расход семян в килограммах на 1 га"
    #method_1
    msg_1=Bot.send_message(user_id, method_1, reply_markup=inline.button("method_1"))
    #пишем id сообщения
    db.set_msg_id(user_id, msg_1.message_id,10)
    #method_2
    msg_2=Bot.send_message(user_id, method_2, reply_markup=inline.button("method_2"))
    #пишем id сообщения
    db.set_msg_id(user_id, msg_2.message_id,10)
    #method_3
    msg_3=Bot.send_message(user_id, method_3, reply_markup=inline.button("method_3"))
    #пишем id сообщения
    db.set_msg_id(user_id, msg_3.message_id,10)

# работает когда пользователь вводит любой текст НАЧАЛО всего
@Bot.message_handler(content_types=['text'], chat_types=['private'])
def handle_command(message):
    user_id = message.from_user.id
    status=db.get_status(user_id)
    user_text = message.text 
    if user_text == "🏠 Главное меню":
        #удаляем сообщение пользователя 
        Bot.delete_message(user_id, message.message_id)
        #показываем меню 
        main_menyu(user_id)
        #обнуляем статус
        db.set_status(user_id, 0)
        if status == 11:
            print ("Кнопка нажата в режиме method_1")
        elif status == 21:
            print ("Кнопка нажата в режиме method_2")
        elif status == 31:
            print ("Кнопка нажата в режиме method_3")
            
    elif status == 11:
        print (user_id, "| method_1 | cтатус", status) #debug
        if is_int(user_text):
            db.set_shirina_mej_sm(user_id, user_text)
            Bot.send_message(user_id, f"Ширина междурядий, <b>{user_text} см</b>", parse_mode="HTML")
            db.set_status(user_id,12)
            Bot.send_message(user_id, "Введите пожалуйста:\n<b>Количество семян на погонный метр, ШТ</b>\n(данные нужно вводить в цифрах...)", parse_mode="HTML")
        else:
            Bot.send_message(user_id, "Ввидите пожалуйста данные в цифрах (1234567890)")    
    elif status == 12:
        print (user_id, "| method_1 | cтатус", status) #debug
        if is_int(user_text):
            #db.set_kol_sem_sht(user_id, user_text)
            Bot.send_message(user_id, f"Количество семян на погонный метр, <b>{user_text} шт</b>", parse_mode="HTML")
            shirina_mej_sm = db.get_shirina_mej_sm(user_id)
            result_1 = int(10000/int(shirina_mej_sm)/100*int(user_text)*10000)
            Bot.send_message(user_id, f"Количество семян на гектар:\n✅ <b>{result_1} шт</b>", parse_mode="HTML")
            result_2 = 100/int(user_text)
            Bot.send_message(user_id, f"Расстояние между семенами:\n✅ <b>{result_2} см</b>", parse_mode="HTML")
            db.set_status(user_id,0)
            Bot.send_message(user_id, "Нажмите на кнопку и я покажу Вам меню 👇", reply_markup=reply.keyboard("MAIN"))
        else:
            Bot.send_message(user_id, "Ввидите пожалуйста данные в цифрах (1234567890)")            


    elif status == 21:
        print (user_id, "| method_2 | cтатус", status) #debug
    
    elif status == 31:
        print (user_id, "| method_3 | cтатус", status) #debug
        #я тут
        if is_int(user_text):
            db.set_massa_1000(user_id, user_text)
            Bot.send_message(user_id, f"Масса 1000 семянок, <b>{user_text} г</b>", parse_mode="HTML")
            db.set_status(user_id,32)
            Bot.send_message(user_id, "Введите пожалуйста:\n<b>Количество семян на погонный метр, ШТ</b>\n(данные нужно вводить в цифрах...)", parse_mode="HTML")
        else:
            Bot.send_message(user_id, "Ввидите пожалуйста данные в цифрах (1234567890)")  

    elif status == 32:
        print (user_id, "| method_3 | cтатус", status) #debug
        if is_int(user_text):
            db.set_kol_sem_sht(user_id, user_text)
            Bot.send_message(user_id, f"Количество семян на погонный метр, <b>{user_text} шт</b>", parse_mode="HTML")
            db.set_status(user_id,33)
            Bot.send_message(user_id, "Введите пожалуйста:\n<b>Ширина междурядий, СМ</b>\n(данные нужно вводить в цифрах...)", parse_mode="HTML")
        else:
            Bot.send_message(user_id, "Ввидите пожалуйста данные в цифрах (1234567890)")  
    
    elif status == 33:
        print (user_id, "| method_3 | cтатус", status) #debug
        if is_int(user_text):
            db.set_kol_sem_sht(user_id, user_text)
            Bot.send_message(user_id, f"Ширина междурядий, <b>{user_text} см</b>", parse_mode="HTML")
            massa_1000 = db.get_massa_1000(user_id)
            kol_sem_sht = db.get_kol_sem_sht(user_id)
            result = int(massa_1000)*int(kol_sem_sht)*(10000/int(user_text)*100)/1000/1000
            Bot.send_message(user_id, f"Расход семяк:\n✅ <b>{result} кг</b>", parse_mode="HTML")
            db.set_status(user_id,0)
            Bot.send_message(user_id, "Нажмите на кнопку и я покажу Вам меню 👇", reply_markup=reply.keyboard("MAIN"))
        else:
            Bot.send_message(user_id, "Ввидите пожалуйста данные в цифрах (1234567890)") 


@Bot.message_handler(commands=['id'])
def send_id(message):
    """ Обрабатываем текстовые сообщения '/id'. """
    if message.chat.type != 'private':
        Bot.send_message(message.chat.id, f"ID чата: {message.chat.id}")
    else:
        Bot.send_message(message.from_user.id, f"Ваш ID: {message.from_user.id}")


@Bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user_id = call.from_user.id  # получаем id пользователя
    #print (call.data) #debug
    all_msg = db.get_msg_id(user_id, 10)
    #print (call.message.id) #debug
    if all_msg:
        for msg in all_msg:
            if int(msg) != int(call.message.id):
                Bot.delete_message(user_id, msg)  # удаляем сообщение
    #очищаем msg_id
    db.del_msg_id(user_id, 10)
    # редактируем сообщение
    Bot.edit_message_text(
            chat_id=user_id,
            message_id=call.message.id,
            text=f"{call.message.text}\n🤝 Принял"
        )
    if call.data == "method_1":
        Bot.send_message(user_id, "Введите пожалуйста:\n<b>Ширина междурядий, СМ</b>\n(данные нужно вводить в цифрах...)", parse_mode="HTML")
        db.set_status(user_id, 11)
    elif call.data == "method_2":
        Bot.send_message(user_id, "Введите пожалуйста:\n<b>Расход семян на поле, КГ</b>\n(данные нужно вводить в цифрах...)", parse_mode="HTML")
        db.set_status(user_id, 21)
    elif call.data == "method_3":
        Bot.send_message(user_id, "Введите пожалуйста:\n<b>Масса 1000 семянок, Г</b>\n(данные нужно вводить в цифрах...)", parse_mode="HTML")
        db.set_status(user_id, 31)

# Запуск APP
while True:
    try:
        logging.info('[BOT] запустился')
        #отправляем уведомеление в чат админу
        Bot.send_message(2964812, "Bot на сервере bot-test запустился") 
        #создаем таблицу users
        db.create_table_user("")
        #Непрекращающаяся прослушка наших чатов
        Bot.polling(none_stop=True, interval=0,  timeout=60) 
    except Exception as my_bot_error:
        logging.info(f'[BOT] startup, Ошибка: {my_bot_error}')
        logging.info(f'[BOT] startup, Ждем 10 секунд ........')
        sleep(10) #ждем 10 сек
        # отправляем сообщение админу
        Bot.send_message(admins_id, f"Ошибка: {my_bot_error}")
        Bot.send_message(admins_id, "Bot упал отжался и встал") # отправляем сообщение админу
    sleep(10) #ждем 10 сек
    logging.info(f'[BOT] Ждем 10 секунд')

