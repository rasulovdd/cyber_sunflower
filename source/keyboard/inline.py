""" Модуль для клавиатуры БОТа """
from telebot.types import (KeyboardButton, ReplyKeyboardMarkup, 
                           ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton)

def button(key_type):
    markup = InlineKeyboardMarkup()
    #markup.row_width = 1
    if key_type == "MAIN":
        markup.add(InlineKeyboardButton(
                   "⚙️ Сменить Город обслуживания ", callback_data="edit-city_nocoordinates"))
    elif key_type == "method_1":
        markup.add(InlineKeyboardButton(
                    "✅ Расчитать", 
                    callback_data="method_1")
                   )
    elif key_type == "method_2":
        markup.add(InlineKeyboardButton(
                    "✅ Расчитать", 
                    callback_data="method_2")
                   )
    elif key_type == "method_3":
        markup.add(InlineKeyboardButton(
                    "✅ Расчитать", 
                    callback_data="method_3")
                   )
    elif key_type == "yes_no":
        markup.row_width = 2
        markup.add(
            InlineKeyboardButton("✅ Да", callback_data="cb_yes"),
            InlineKeyboardButton("❌ Нет", callback_data="cb_no")
        )

    return markup

def yes_no(user_id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("✅ Да", callback_data=f"yes_{user_id}"),
        InlineKeyboardButton("❌ Нет", callback_data=f"no_{user_id}")
    )

    return markup
