""" Модуль для клавиатуры БОТа """
from telebot.types import (KeyboardButton, ReplyKeyboardMarkup, 
                           ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton)

def keyboard(key_type):
    """ Функция для создание клавиатуры."""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    if key_type == "MAIN":
        markup.add(KeyboardButton("🏠 Главное меню"))
    return markup
