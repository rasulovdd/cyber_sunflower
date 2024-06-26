""" Модуль для клавиатуры БОТа """
from telebot.types import (KeyboardButton, ReplyKeyboardMarkup, 
                           ReplyKeyboardRemove)

def keyboard(key_type):
    """ Функция для создание клавиатуры."""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    if key_type == "MAIN":
        markup.add(KeyboardButton("🏠 Главное меню"))
    elif key_type == "DONE":
        markup = ReplyKeyboardRemove()
    elif key_type == "ADMIN":
        markup.add(KeyboardButton("🌼 Расчеты"))
        markup.add(KeyboardButton("📖 Список сотрудников"))
    return markup
