from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, dispatcher
from constants import BOT_TOKEN
from functions import saludar, hello, paginaGe, start

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start_bot():    
    start_handler = CommandHandler('start', start)
    hello_handler = CommandHandler('iran', hello)
    saludar_handler = CommandHandler('hola', saludar)
    paginaGe_handler = CommandHandler('paginaGE', paginaGe)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(hello_handler)
    dispatcher.add_handler(saludar_handler)
    dispatcher.add_handler(paginaGe_handler)
    updater.start_polling()