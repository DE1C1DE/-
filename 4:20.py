# -*- coding: utf-8 -*-
import telebot
import time
from datetime import datetime
bot = telebot.TeleBot("Токен бота", parse_mode=None)
BOT_URL = "URL бота" 
now = datetime.now()
current_time = now.strftime("%H:%M")
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)
    time.sleep(1)
    if current_time == '10:52' or current_time == '10:53':  # Выставляете ваше время
        print('pass')
        bot.send_message("id чата", 'text')
        time.sleep(60)
    bot.infinity_polling()
