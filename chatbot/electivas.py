from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher
)

from telegram import Update

# ELECTIVAS
#mensajes de regreso al menu
mensaje_regreso_menu = 'Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Electivas utiliza el comando: /electivas\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

comandos = 'Por favor selecciona o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Electivas.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Cuándo procede un dictamen UPIICSA para acreditar Electivas?: /electivas_opc1\nPregunta 2:¿Cuándo procede un dictamen Zacatenco para acreditar Electivas?: /electivas_opc2\nPregunta 3:¿En cuánto tiempo se verá reflejada mi electiva en kardex?: /electivas_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

electivas1 = '¿Cuándo procede un dictamen UPIICSA para acreditar Electivas?\n\nSi dejaste pasar un semestre desde tu última inscripción y aún cuentas con periodos para cumplir la totalidad de créditos de tu programa académico.\n\n\n' + mensaje_regreso_menu

electivas2 = '¿Cuándo procede un dictamen Zacatenco para acreditar Electivas?\n\nSi dejaste pasar un semestre desde tu última inscripción y/o , ya no cuentas con periodos para cumplir la totalidad de créditos de tu programa académico.\n\n\n' + mensaje_regreso_menu

electivas3 = '¿En cuánto tiempo se verá reflejada mi electiva en kardex?\n\nUna vez validadas las electivas por parte de la coordinación, serán acreditadas cuando se valide que tu trayectoria académica lo permite sin necesidad de dictamen, durante las fechas previamente acordadas en los calendarios publicados.\n\n\n' + mensaje_regreso_menu

def menu(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=comandos)


def opc_1(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=electivas1)


def opc_2(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=electivas2)


def opc_3(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=electivas3)

def start(dispatcher: Dispatcher) -> None:
    """Iniciar los comandos de este modulo en el chatbot"""
    electivas_menu_handler = CommandHandler('electivas', menu)
    electivas_opc1_handler = CommandHandler('electivas_opc1', opc_1)
    electivas_opc2_handler = CommandHandler('electivas_opc2', opc_2)
    electivas_opc3_handler = CommandHandler('electivas_opc3', opc_3)

    dispatcher.add_handler(electivas_menu_handler)
    dispatcher.add_handler(electivas_opc1_handler)
    dispatcher.add_handler(electivas_opc2_handler)
    dispatcher.add_handler(electivas_opc3_handler)