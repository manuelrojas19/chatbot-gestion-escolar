from telegram.ext import (
    CallbackContext,
    CommandHandler,
    MessageHandler,
    Filters,
    Dispatcher
)

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update

# BAJAS
# mensajes de regreso al menu
MENSAJE_REGRESO_MENU = 'Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Bajas utiliza el comando: /bajas\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
COMANDOS = 'Por favor selecciona o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Bajas.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Hasta cuándo tengo para darme de baja temporal?: /bajas_opc1\nPregunta 2:¿Hasta cuándo tengo para darme de baja definitiva?: /bajas_opc2\nPregunta 3:¿Una vez que regrese de baja temporal como podré reinscribirme?: /bajas_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
BAJAS_PREGUNTA_UNO = '¿Hasta cuándo tengo para darme de baja temporal?'
BAJAS_PREGUNTA_DOS = '¿Hasta cuándo tengo para darme de baja definitiva?'
BAJAS_PREGUNTA_TRES = '¿Una vez que regrese de baja temporal como podré reinscribirme?'
BAJAS_RESPUESTA_UNO = '¿Hasta cuándo tengo para darme de baja temporal?\n\nDentro del primer mes iniciado el periodo escolar y por causas de fueza mayor probatorias durante todo el periodo. Se debe consultar las fechas de publicación y proceso a seguir en https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#baj\n\n\n' + MENSAJE_REGRESO_MENU
BAJAS_RESPUESTA_DOS = '¿Hasta cuándo tengo para darme de baja definitiva?\n\nDurante todo el periodo escolar. Se debe consultar las fechas de publicación y proceso a seguir en https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#baj\n\n\n' + MENSAJE_REGRESO_MENU
BAJAS_RESPUESTA_TRES = '¿Una vez que regrese de baja temporal como podré reinscribirme?\n\nDeberás solicitar tu cita con el departamento de gestión escolar de manera presencial o via Whatsapp https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#ase\nTu cita dependerá del estatus como alumno regural o irregular. NO PODRÁS SOLICITAR BAJA con materias desfasadas.\n\n\n' + MENSAJE_REGRESO_MENU

preguntas = {BAJAS_PREGUNTA_UNO: BAJAS_RESPUESTA_UNO,
             BAJAS_PREGUNTA_DOS: BAJAS_RESPUESTA_DOS,
             BAJAS_PREGUNTA_TRES: BAJAS_RESPUESTA_TRES}


def menu(update: Update, context: CallbackContext) -> None:
    buttons = [[KeyboardButton(BAJAS_PREGUNTA_UNO)], [KeyboardButton(
        BAJAS_PREGUNTA_DOS)], [KeyboardButton(BAJAS_PREGUNTA_TRES)]]
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=COMANDOS, reply_markup=ReplyKeyboardMarkup(buttons))


def opc_1(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=BAJAS_RESPUESTA_UNO)


def opc_2(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=BAJAS_RESPUESTA_DOS)


def opc_3(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=BAJAS_PREGUNTA_TRES)

def start(dispatcher: Dispatcher) -> None:
    """Iniciar los comandos de este modulo en el chatbot"""
    dispatcher.add_handler(CommandHandler('bajas', menu))
    dispatcher.add_handler(CommandHandler('bajas_opc1', opc_1))
    dispatcher.add_handler(CommandHandler('bajas_opc2', opc_2))
    dispatcher.add_handler(CommandHandler('bajas_opc3', opc_3))
