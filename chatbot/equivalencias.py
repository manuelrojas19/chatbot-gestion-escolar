from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher
)

from telegram import Update

# EQUIVALENCIAS
#mensajes de regreso al menu
mensaje_regreso_menu = 'Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Equivalencias utiliza el comando: /equivalencias\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

comandos = 'Por favor selecciona o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Equivalencias.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Cuáles son las equivalencias que pueden aplicar en mi trayectoria académica?: /equivalencias_opc1\nPregunta 2:¿Cuánto tiempo tarda en verse reflejadas mis equivalencias?: /equivalencias_opc2\nPregunta 3:¿Cuántas equivalencias puedo tener?: /equivalencias_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

equivalencias1 = '¿Cuáles son las equivalencias que pueden aplicar en mi trayectoria académica?\n\nSi tienes un cambio de carrera, te fuiste de movilidad académica o, vienes de otro plantel.\nTodas estas están sujetas a la revisión y autorización previa de la DAE y DES según los dictámenes, oficios y equivalencias que se emitan.\n\n\n' + mensaje_regreso_menu

equivalencias2 = '¿Cuánto tiempo tarda en verse reflejadas mis equivalencias?\n\nUna vez que la DAE y DES determinan que, si proceden las equivalencias, envían los oficios y dictámenes para su revisión y carga, esto se verá reflejado durante el semestre en curso de la solicitud.\n\n\n' + mensaje_regreso_menu

equivalencias3 = '¿Cuántas equivalencias puedo tener?\n\nLas que en el proceso que hayas aplicado te autoricen y tu programa y plan de estudios estén vigentes.\n\n\n' + mensaje_regreso_menu

def menu(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=comandos)


def opc_1(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=equivalencias1)


def opc_2(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=equivalencias2)


def opc_3(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=equivalencias3)

def start(dispatcher: Dispatcher) -> None:
    """Iniciar los comandos de este modulo en el chatbot"""
    equivalencias_menu_handler = CommandHandler('equivalencias', menu)
    equivalencias_opc1_handler = CommandHandler('equivalencias_opc1', opc_1)
    equivalencias_opc2_handler = CommandHandler('equivalencias_opc2', opc_2)
    equivalencias_opc3_handler = CommandHandler('equivalencias_opc3', opc_3)

    dispatcher.add_handler(equivalencias_menu_handler)
    dispatcher.add_handler(equivalencias_opc1_handler)
    dispatcher.add_handler(equivalencias_opc2_handler)
    dispatcher.add_handler(equivalencias_opc3_handler)