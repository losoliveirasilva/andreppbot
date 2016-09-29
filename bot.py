import os
import logging
from telegram.ext import Updater, MessageHandler, Filters, Job
from random import choice, randint

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

TOKEN = os.environ.get('TOKEN')
APPNAME = os.environ.get('APPNAME')
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)
jobQueue = updater.job_queue
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.setWebhook("https://" + APPNAME + ".herokuapp.com/" + TOKEN)

# Loads external messages, from bot_phrases.txt, to bot.
with open('bot_phrases.txt', 'r') as file:
    automatic_phrases = file.read().strip().split('\n')

# Loads external messages, from bot_swearwords.txt, to bot.
with open('bot_swearwords.txt', 'r') as file:
    automatic_swearwords = file.read().strip().split('\n')


def echo(bot, update):
    max_ = 3
    if update.message.from_user.username == "andremesquita96":
        user_message = update.message.text

        if randint(1, max_) == 3:
            if '?' in user_message:
                bot.sendMessage(update.message.chat_id, text='{}, {}'.format(
                                'Responde', choice(automatic_swearwords)))
            else:
                bot.sendMessage(update.message.chat_id, text='{}, {}'.format(
                                user_message, choice(automatic_swearwords)))

        if max_ < 6:
            max_ = max_ + 1
        else:
            max_ = 3


def automatic_message(bot, update, delay):
    delayed_message = Job(bot.sendMessage(update.message.chat_id, text=choice(automatic_phrases)),
                          delay, repeat=False)
    jobQueue.put(delayed_message, next_t=delay)

updater.dispatcher.add_handler(MessageHandler([Filters.text], echo))
updater.idle()
