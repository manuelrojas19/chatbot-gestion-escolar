from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, dispatcher

#REINSCRIPCION
tramites_comandos = 'holahola tramitando'

def tramitesMenu(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=tramites_comandos)