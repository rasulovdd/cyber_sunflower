import os

def is_int_v2(text):
    return text.isdigit()

def is_int(user_text):
    if user_text.replace(".", "", 1).replace("-", "", 1).isnumeric():
        return True
    else:
        return False

def text_to_float(text):    
    number = text.replace(',', '.')
    return float(number)

def check_number(text):
    try:
        number = float(text.replace(",", "."))
        return number
    except ValueError:
        return False

# def date_format(s):
#     now = datetime.now()
#     my_now = now.strftime("%d.%m.%Y")
#     data=f"{s}.{now.year}"
    
#     my_data_text=str(data).replace(",",".")
#     my_date=datetime.strptime(my_data_text, "%d.%m.%Y")
#     print (f"Сейчас: {now}")
#     print (f"Дата пользователя: {my_data_text}")
#     if now <= my_date:
#         print (f"Дата пользователя: {my_data_text}")
#     else:
#         print ("Вы ввели прошедшую дату")
#     #return my_date
#     return my_now