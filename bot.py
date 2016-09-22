import os, logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
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

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

TOKEN = os.environ.get('TOKEN')
APPNAME = os.environ.get('APPNAME')
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.setWebhook("https://"+APPNAME+".herokuapp.com/"+TOKEN)

def echo(bot, update):
	if update.message.from_user.username == "Lucasbordignon":
		bot.sendMessage(update.message.chat_id,
			text='{}, {}'.format(
				update.message.text, choice(words)))

# if __name__ == '__main__':

	# updater = Updater("240204199:AAE1437Swm7onr3g4tjEYqxP90WplSVBWng")

	# dp = updater.dispatcher

	# dp.add_handler(MessageHandler([Filters.text], echo))

updater.dispatcher.add_handler(MessageHandler([Filters.text], echo))

	# updater.start_polling()

updater.idle()
