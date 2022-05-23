from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher
)

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update

# DICTAMENES
# mensajes de regreso al menu
mensaje_regreso_menu = 'Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Dictámenes utiliza el comando: /dictamenes\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

dictamen_comandos = 'Por favor selecciona o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Dictámenes.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Qué dictamen debo de solicitar si estoy desfasado?: /dictamen_opc1\nPregunta 2:¿En qué casos debo de solicitar dictamen ZACATENCO?: /dictamen_opc2\nPregunta 3:¿Dónde puedo ver la resolución de mi dictamen?: /dictamen_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

DICTAMEN_PREGUNTA_UNO = '¿Qué dictamen debo de solicitar si estoy desfasado?'
DICTAMEN_PREGUNTA_DOS = '¿En qué casos debo de solicitar dictamen ZACATENCO?'
DICTAMEN_PREGUNTA_TRES = '¿Dónde puedo ver la resolución de mi dictamen?'

DICTAMEN_RESPUESTA_UNO = '¿Qué dictamen debo de solicitar si estoy desfasado?\n\nSi tu periodo de ingreso es del 17/2 en adelante, deberás solicitar dictamen UPIICSA por oportunidad\n\nSi tu periodo es 17/1 hacía atrás, deberás solicitar dictamen CGC ZACATENCO por oportunidad.\n\n\n' + mensaje_regreso_menu
DICTAMEN_RESPUESTA_DOS = '¿En qué casos debo de solicitar dictamen ZACATENCO?\n\nSi tu periodo de ingreso fue del 17/1 hacia atrás debes de solicitar ampliación de plazo para tener derecho a reinscripción\n\nSi tu periodo de ingreso fue del 17/1 hacia atrás y tienes materias adeudadas o desfasas , debes solicitar oportunidad.\n\n\n' + mensaje_regreso_menu
DICTAMEN_RESPUESTA_TRES = '¿Dónde puedo ver la resolución de mi dictamen?\n\nSi solicitaste dictamen UPIICSA, directamente en tu SAES en el apartado Dictamenes \n\nSi solicitaste dictamen CGC Zacatenco en la página de UPIICSA https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#dicz\n\n\n' + mensaje_regreso_menu

preguntas = {DICTAMEN_PREGUNTA_UNO: DICTAMEN_RESPUESTA_UNO,
             DICTAMEN_PREGUNTA_DOS: DICTAMEN_RESPUESTA_DOS,
             DICTAMEN_PREGUNTA_TRES: DICTAMEN_RESPUESTA_TRES}


def dictamenMenu(update: Update, context: CallbackContext) -> None:
    buttons = [[KeyboardButton(DICTAMEN_PREGUNTA_UNO)], [KeyboardButton(
        DICTAMEN_PREGUNTA_DOS)], [KeyboardButton(DICTAMEN_PREGUNTA_TRES)]]
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=dictamen_comandos, reply_markup=ReplyKeyboardMarkup(buttons))


def dictamenOpc1(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=DICTAMEN_RESPUESTA_UNO)


def dictamenOpc2(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=DICTAMEN_RESPUESTA_DOS)


def dictamenOpc3(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=DICTAMEN_RESPUESTA_TRES)


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
