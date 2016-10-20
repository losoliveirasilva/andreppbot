import os
import logging
from telegram.ext import Updater, MessageHandler, Filters, Job
from random import choice, randint

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

TOKEN = os.environ.get('TOKEN')
APPNAME = os.environ.get('APPNAME')
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)
job_queue = updater.job_queue
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.setWebhook("https://" + APPNAME + ".herokuapp.com/" + TOKEN)

# Loads external messages, from bot_phrases.txt, to bot.
with open('bot_phrases.txt', 'r') as phrases_file:
    automatic_phrases = phrases_file.read().strip().split('\n')

# Loads external messages, from bot_swearwords.txt, to bot.
with open('bot_swearwords.txt', 'r') as swearwords_file:
    automatic_swearwords = swearwords_file.read().strip().split('\n')

max_ = 3

def echo(bot, update):
    global max_

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
            max_ += 1
        else:
            max_ = 3


def automatic_message(bot, update, delay):
    delayed_message = Job(bot.sendMessage(update.message.chat_id, text=choice(automatic_phrases)),
                          delay, repeat=False)
    job_queue.put(delayed_message, next_t=delay)

updater.dispatcher.add_handler(MessageHandler([Filters.text], echo))
updater.idle()
