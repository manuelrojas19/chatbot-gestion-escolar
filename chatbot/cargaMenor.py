from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher
)

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update

# TRAMITES CON CARGA MENOR A LA MINIMA
# mensajes de regreso al menu
mensaje_regreso_menu = 'Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Trámites con Carga Menor a la Mínima utiliza el comando: /cargaMenor\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

comandos = 'Por favor selecciona la opción de los recuadros de abajo o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Trámites con Carga Menor a la Mínima.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Cuándo me corresponde la carta por carga menor a la mínima?: /cargaMenor_opc1\nPregunta 2:¿Cuándo me corresponde dictamen  por carga menor a la mínima?: /cargaMenor_opc2\nPregunta 3:¿Si tengo un dictamen vigente que me permitió reinscribirme, debo de solicitar la carta o el dictamen?: /cargaMenor_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

CARGA_MENOR_PREGUNTA_UNO = '¿Cuándo me corresponde la carta por carga menor a la mínima?'
CARGA_MENOR_PREGUNTA_DOS = '¿Cuándo me corresponde dictamen  por carga menor a la mínima?'
CARGA_MENOR_PREGUNTA_TRES = '¿Si tengo un dictamen vigente que me permitió reinscribirme, debo de solicitar la carta o el dictamen?'

CARGA_MENOR_RESPUESTA_UNO = '¿Cuándo me corresponde la carta por carga menor a la mínima?\n\nSi eres alumno regular con una carga menor a la mínima de tu programa académico.\nConsulta la tabla de cargas https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#carga\n\n\n' + mensaje_regreso_menu
CARGA_MENOR_RESPUESTA_DOS = '¿Cuándo me corresponde dictamen  por carga menor a la mínima?\n\nSi eres alumno irregular con una carga menor a la mínima de tu programa académico\nConsulta la tabla de cargas https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#carga\n\n\n' + mensaje_regreso_menu
CARGA_MENOR_RESPUESTA_TRES = '¿Si tengo un dictamen vigente que me permitió reinscribirme, debo de solicitar la carta o el dictamen?\n\nNo es necesario, ya que el dictamen vigente te ampara la inscripción al semestre en curso.\n\n\n' + mensaje_regreso_menu


preguntas = {CARGA_MENOR_PREGUNTA_UNO: CARGA_MENOR_RESPUESTA_UNO,
             CARGA_MENOR_PREGUNTA_DOS: CARGA_MENOR_RESPUESTA_DOS,
             CARGA_MENOR_PREGUNTA_TRES: CARGA_MENOR_RESPUESTA_TRES}

def menu(update: Update, context: CallbackContext) -> None:
    buttons = [[KeyboardButton(CARGA_MENOR_PREGUNTA_UNO)], [KeyboardButton(
        CARGA_MENOR_PREGUNTA_DOS)], [KeyboardButton(CARGA_MENOR_PREGUNTA_TRES)]]
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=comandos, reply_markup=ReplyKeyboardMarkup(buttons))

def opc_1(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=CARGA_MENOR_RESPUESTA_UNO)


def opc_2(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=CARGA_MENOR_RESPUESTA_DOS)


def opc_3(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=CARGA_MENOR_RESPUESTA_TRES)


def start(dispatcher: Dispatcher) -> None:
    """Iniciar los comandos de este modulo en el chatbot"""
    cargaMenor_menu_handler = CommandHandler('cargaMenor', menu)
    cargaMenor_opc1_handler = CommandHandler('cargaMenor_opc1', opc_1)
    cargaMenor_opc2_handler = CommandHandler('cargaMenor_opc2', opc_2)
    cargaMenor_opc3_handler = CommandHandler('cargaMenor_opc3', opc_3)

    dispatcher.add_handler(cargaMenor_menu_handler)
    dispatcher.add_handler(cargaMenor_opc1_handler)
    dispatcher.add_handler(cargaMenor_opc2_handler)
    dispatcher.add_handler(cargaMenor_opc3_handler)
