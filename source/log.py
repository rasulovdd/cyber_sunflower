import logging
import os

# создаем папку если его нет 
if not os.path.exists('logs'):
    try:
        os.mkdir('logs')
    except Exception as my_error:
        print(f"Ошибка: {my_error}") #debug

# устанавливаем стандартные параметры логирования
logging.basicConfig(
    filename='logs/cyber_sunflower.log', 
    level=logging.INFO, 
    #format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',
    format=f'%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]',
    datefmt='%d-%m-%Y %H:%M:%S'
)