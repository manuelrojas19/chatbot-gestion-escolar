from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher
)

from telegram import Update

# BAJAS
#mensajes de regreso al menu
mensaje_regreso_menu = 'Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Bajas utiliza el comando: /bajas\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

comandos = 'Por favor selecciona o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Bajas.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Hasta cuándo tengo para darme de baja temporal?: /bajas_opc1\nPregunta 2:¿Hasta cuándo tengo para darme de baja definitiva?: /bajas_opc2\nPregunta 3:¿Una vez que regrese de baja temporal como podré reinscribirme?: /bajas_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

bajas1 = '¿Hasta cuándo tengo para darme de baja temporal?\n\nDentro del primer mes iniciado el periodo escolar y por causas de fueza mayor probatorias durante todo el periodo. Se debe consultar las fechas de publicación y proceso a seguir en https://www.upiicsa.ipn.mx/estudiantes/gestion-esoclar.html#baj\n\n\n' + mensaje_regreso_menu

bajas2 = '¿Hasta cuándo tengo para darme de baja definitiva?\n\nDurante todo el periodo escolar. Se debe consultar las fechas de publicación y proceso a seguir en https://www.upiicsa.ipn.mx/estudiantes/gestion-esoclar.html#baj\n\n\n' + mensaje_regreso_menu

bajas3 = '¿Una vez que regrese de baja temporal como podré reinscribirme?\n\nDeberás solicitar tu cita con el departamento de gestión escolar de manera presencial o via Whatsapp https://www.upiicsa.ipn.mx/estudiantes/gestions-escolar.html#ase\nTu cita dependerá del estatus como alumno regural o irregular. NO PODRÁS SOLICITAR BAJA con materias desfasadas.\n\n\n' + mensaje_regreso_menu


def menu(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=comandos)


def opc_1(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=bajas1)


def opc_2(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=bajas2)


def opc_3(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=bajas3)

def start(dispatcher: Dispatcher) -> None:
    """Iniciar los comandos de este modulo en el chatbot"""
    bajas_menu_handler = CommandHandler('bajas', menu)
    bajas_opc1_handler = CommandHandler('bajas_opc1', opc_1)
    bajas_opc2_handler = CommandHandler('bajas_opc2', opc_2)
    bajas_opc3_handler = CommandHandler('bajas_opc3', opc_3)

    dispatcher.add_handler(bajas_menu_handler)
    dispatcher.add_handler(bajas_opc1_handler)
    dispatcher.add_handler(bajas_opc2_handler)
    dispatcher.add_handler(bajas_opc3_handler)