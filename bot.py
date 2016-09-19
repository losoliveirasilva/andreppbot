from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import choice

words = (
	'porra',
	'caralho',
	'filha da puta',
	'merda',
	'cacete',
)

def echo(bot, update):
	# if update.message.from_user.username == "andremesquita96":
	if update.message.from_user.username == "losoliveirasilva":
		bot.sendMessage(update.message.chat_id,
			text='{}, {}'.format(
				update.message.text, choice(words)))

if __name__ == '__main__':

	updater = Updater("240204199:AAE1437Swm7onr3g4tjEYqxP90WplSVBWng")

	dp = updater.dispatcher

	dp.add_handler(MessageHandler([Filters.text], echo))

	updater.start_polling()

	updater.idle()
