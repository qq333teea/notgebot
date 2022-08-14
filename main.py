#!/usr/bin/python

import os
import telebot


API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	pass

@bot.message_handler(commands=['createNote'])
def createNote(message):
    try:
        file = open(str(message.chat.id), 'w')
        file.close()
        bot.send_message(message.chat.id, 'ok')
    except:
        bot.send_message(message.chat.id, 'error')

@bot.message_handler(commands=['cat'])
def cat(message):
    try:
        file = open(str(message.chat.id), 'r')
        note = file.read()
        bot.send_message(message.chat.id, note)
        file.close()
    except:
        bot.send_message(message.chat.id, 'error')

def main():
    try:
        bot.polling()
    except:
        main()

if __name__ == '__main__':
    main()
