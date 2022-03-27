from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, dispatcher

#REINSCRIPCION
reinscripcion_comandos = 'holahola reinscripcion'

def reinscripcionMenu(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=reinscripcion_comandos)
