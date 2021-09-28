'''
    File name: main.py
    Author: Pavel Klimovskoy
    Date created: 28.09.2021
    Python Version: 3.9
'''

import telebot
from supModules import GetApiKey

bot = telebot.TeleBot(GetApiKey())

# Получение telegram id пользователя
@bot.message_handler(commands=['getid'])
def start_command(message):
    msg = "Ваш id: " + str(message.from_user.id)
    bot.send_message(message.chat.id, msg)

# Вывод telegram id пользователя при запуске
@bot.message_handler(commands=['start'])
def start_command(message):
    msg = "Ваш id: " + str(message.from_user.id)
    bot.send_message(message.chat.id, msg)

bot.polling(none_stop=True, interval=0)
