from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher
)

from telegram import Update

# DICTAMENES
dictamen_comandos = 'Por favor selecciona o escribe el comando de acuerdo a la pregunta que deseas consultar relacionadas al tema de Dictámenes.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1: ¿Qué dictamen debo de solicitar si estoy desfasado?: /dictamen_opc1\n#Pregunta 2: ¿En qué casos debo de solicitar dictamen ZACATENCO?: /dictamen_opc2\n#Pregunta 3: ¿Dónde puedo ver la resolución de mi dictamen?: /dictamen_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
# Pregunta 1: ¿Qué dictamen debo de solicitar si estoy desfasado?
# respuesta 1
dictamen1 = 'Si tu periodo de ingreso es del 17/2 en adelante, deberás solicitar dictamen UPIICSA por oportunidad\n\nSi tu periodo es 17/1 hacía atrás, deberás solicitar dictamen CGC ZACATENCO por oportunidad'
# Pregunta 2: ¿En qué casos debo de solicitar dictamen ZACATENCO?
# respuesta 2
dictamen2 = 'Si tu periodo de ingreso fue del 17/1 hacia atrás debes de solicitar ampliación de plazo para tener derecho a reinscripción\n\nSi tu periodo de ingreso fue del 17/1 hacia atrás y tienes materias adeudadas o desfasas , debes solicitar oportunidad.'
# Pregunta 3: ¿Dónde puedo ver la resolución de mi dictamen?
# respuesta 3
dictamen3 = 'Si solicitaste dictamen UPIICSA, directamente en tu SAES en el apartado Dictamenes \n\nSi solicitaste dictamen CGC Zacatenco en la página de UPIICSA https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#dicz'


def dictamenMenu(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=dictamen_comandos)


def dictamenOpc1(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=dictamen1)


def dictamenOpc2(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=dictamen2)


def dictamenOpc3(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=dictamen3)


def start(dispatcher: Dispatcher) -> None:
    """Iniciar los comandos de este modulo en el chatbot"""
    dictamenesMenu_handler = CommandHandler('dictamenes', dictamenMenu)
    dictamenesOpc1_handler = CommandHandler('dictamen_opc1', dictamenOpc1)
    dictamenesOpc2_handler = CommandHandler('dictamen_opc2', dictamenOpc2)
    dictamenesOpc3_handler = CommandHandler('dictamen_opc3', dictamenOpc3)

    dispatcher.add_handler(dictamenesMenu_handler)
    dispatcher.add_handler(dictamenesOpc1_handler)
    dispatcher.add_handler(dictamenesOpc2_handler)
    dispatcher.add_handler(dictamenesOpc3_handler)
