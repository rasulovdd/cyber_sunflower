<h1 align="center">cyber_sunflower</h1>

## Описание

БОТ помощник. Поможет рассчитать расход семян 

## Стек
Core: python 3, pyTelegramBotAPI<br/>
#Future Database: mysql<br/>

## Установка

1. Скачайте репозиторий<br/>

    ```bash
    git clone https://github.com/rasulovdd/cyber_sunflower.git && cd cyber_sunflower
    ```

2. Устанавливаем виртуальное окружение<br/>

    ```bash
    apt install -y python3-venv
    ```
    ```bash
    python3 -m venv env
    ```

3. Активируем её <br/>

    ```bash
    source env/bin/activate
    ```

4. Скачиваем и устанавливаем нужные библиотеки<br/>

    ```bash
    pip install -r requirements.txt
    ```

5. Создаем .env файл с вашими данными, можно создать из шаблона и просто поправить поля <br/>

    ```bash
    cp .env.sample .env
    nano .env
    ```

6. Создаем .service файл для вашего бота 
    sudo nano /etc/systemd/system/cyber_sunflower.service<br/>

    ```ini
    [Unit]
    Description='Service for cyber_sunflower'
    After=network.target

    [Service]
    Type=idle
    Restart=on-failure
    StartLimitBurst=2
    # Restart, but not more than once every 30s (for testing purposes)
    StartLimitInterval=120
    User=root
    ExecStart=/bin/bash -c 'cd ~/cyber_sunflower/ && source env/bin/activate && python3 app.py'

    [Install]
    WantedBy=multi-user.target

    ```

7. Включаем сервис и запускаем<br/>

    ```bash
    systemctl enable cyber_sunflower.service
    systemctl start cyber_sunflower.service
    ```

8. Бот готов к использованию 

## Дополнительно
пример заполнения .env файла:

    bot_tokken="Токен бота"
    #Адрес базы данных
    db_host="127.0.0.1"
    #имя пользователя БД
    db_user="bot_user" 
    #пароль пользователя БД
    db_password="bot_password1!"
    #название БД
    database="taxi_calls_bot"
    #список пользователей для уведомления
    users_id="2964812"
    #список пользователей c правами администратора
    admins_id="2964812"
    #статус debug режима
    debug_on=1 
