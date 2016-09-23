import os
import logging
from datetime import datetime
from telegram.ext import Updater, MessageHandler, Filters
from random import choice

words = (
    'porra',
    'caralho',
    'filha da puta',
    'merda',
    'cacete',
    'arrombado',
    'trouxa',
    'filho de chocadeira',
    'otário',
    'babaca',
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

TOKEN = os.environ.get('TOKEN')
APPNAME = os.environ.get('APPNAME')
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.setWebhook("https://" + APPNAME + ".herokuapp.com/" + TOKEN)

# Loads external messages, from bot_phrases.txt, to bot.
with open('bot_phrases.txt', 'r') as file:
    automatic_phrases = file.read().strip().split('\n')


def echo(bot, update):
    last_message_hour = 0
    if update.message.from_user.username == "andremesquita96":
        last_message_hour = datetime.now().hour
        user_message = update.message.text
        if '?' in user_message:
            bot.sendMessage(update.message.chat_id, text='{}, {}'.format(
                            'Responde', choice(words)))
        else:
            bot.sendMessage(update.message.chat_id, text='{}, {}'.format(
                            user_message, choice(words)))

    elif (last_message_hour + 8) % 24 == datetime.now().hour:
        last_message_hour = datetime.now().hour
        bot.sendMessage(update.message.chat_id, text=choice(automatic_phrases))

updater.dispatcher.add_handler(MessageHandler([Filters.text], echo))
updater.idle()
