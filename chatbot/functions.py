from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, dispatcher

comandosChatBotGE = 'Para comenzar escribe o elige alguno de los siguientes comandos: \nPagina de Gestion Escolar: /paginaGE'


def start(update, context):    
    context.bot.send_message(chat_id=update.effective_chat.id, text=comandosChatBotGE)

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Encender auto')

def saludar(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Mucho gusto, en que puedo servirte?')

def paginaGe(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='La pagina de gestion escolar es:https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html')

