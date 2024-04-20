""" Модуль для клавиатуры БОТа """
from telebot.types import (KeyboardButton, ReplyKeyboardMarkup, 
                           ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton)

def keyboard(key_type):
    """ Функция для создание клавиатуры."""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    if key_type == "MAIN":
        markup.add(KeyboardButton("🏠 Главное меню"))
    elif key_type == "CANCEL":
        markup.add(KeyboardButton("Отменить"))
    elif key_type == "CONTACT":
        markup.add(KeyboardButton(
            text="Отправить телефон", request_contact=True))
    elif key_type == "GEO":
        markup.add(KeyboardButton(
            text="Поделиться с местоположением", request_location=True))
    elif key_type == "BACK":
        markup.add(KeyboardButton("⬅️ Главное меню"))
    elif key_type == "FEEDBACK":
        markup.add(KeyboardButton("❌ Пропустить"))
    elif key_type == "DONE":
        markup = ReplyKeyboardRemove()
    elif key_type == "ADMIN":
        markup.add(KeyboardButton("Проверка"),
                   KeyboardButton("Рассылка"),
                   KeyboardButton("Уведомления")
                   )
        markup.add(KeyboardButton("Обновить марки и модели авто"),
                   KeyboardButton("Ошибки"),
                   KeyboardButton("Статистика"))
        markup.add(KeyboardButton("Отменить"))

    return markup
