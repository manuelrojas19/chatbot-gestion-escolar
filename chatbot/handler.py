from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, dispatcher
from constants import BOT_TOKEN

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Encender auto')

def start_bot():    
    hello_handler = CommandHandler('iran', hello)
    dispatcher.add_handler(hello_handler)
    updater.start_polling()