from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher
)

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update

# EXAMENES DE SABERES PREVIAMENTE ADQUIRIDOS
# mensajes de regreso al menu
mensaje_regreso_menu = 'Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Exámenes de Saberes Previamente Adquiridos utiliza el comando: /espa\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

comandos = 'Por favor selecciona la opción de los recuadros de abajo o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Exámenes de Saberes Previamente Adquiridos.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿En que casos debo presentar saberes previamente adquiridos?: /espa_opc1\nPregunta 2:¿Cuántas veces puedo presentar un examen de saberes previamente adquiridos?: /espa_opc2\nPregunta 3:¿Qué proceso debo seguir para presentar un examen de saberes previmente adquiridos?: /espa_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

ESPA_PREGUNTA_UNO = '¿En que casos debo presentar saberes previamente adquiridos?'
ESPA_PREGUNTA_DOS = '¿Cuántas veces puedo presentar un examen de saberes previamente adquiridos?'
ESPA_PREGUNTA_TRES = '¿Qué proceso debo seguir para presentar un examen de saberes previmente adquiridos?'

ESPA_RESPUESTA_UNO = '¿En que casos debo presentar saberes previamente adquiridos?\n\nEl alumno debera estar inscrito y no haberla cursado con anterioridad.\n\n\n' + mensaje_regreso_menu
ESPA_RESPUESTA_DOS = '¿Cuántas veces puedo presentar un examen de saberes previamente adquiridos?\n\nPuede presentar cada unidad de aprendizaje una sola vez durante toda su trayectoria académica.\n\n\n' + mensaje_regreso_menu
ESPA_RESPUESTA_TRES = '¿Qué proceso debo seguir para presentar un examen de saberes previmente adquiridos?\n\nDeberás contar con una reinscripción y revisar la información publicada dentro de los primeros 10 días iniciado el semestre. Considera lo siguiente:\n-Tendrás que llenar tu solicitud.\n-El jefe de programa académico te hará una previa entrevista para conocer tus conocimientos de la unidad de aprendizaje.\n-En caso de no aprovar el examen de saberes previamente adquiridos, la calificación no se verá reflejada en tu kardex.\n\n\n' + mensaje_regreso_menu

preguntas = {ESPA_PREGUNTA_UNO: ESPA_RESPUESTA_UNO,
             ESPA_PREGUNTA_DOS: ESPA_RESPUESTA_DOS,
             ESPA_PREGUNTA_TRES: ESPA_RESPUESTA_TRES}

def menu(update: Update, context: CallbackContext) -> None:
    buttons = [[KeyboardButton(ESPA_PREGUNTA_UNO)], [KeyboardButton(
        ESPA_PREGUNTA_DOS)], [KeyboardButton(ESPA_PREGUNTA_TRES)]]
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=comandos, reply_markup=ReplyKeyboardMarkup(buttons))



def opc_1(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=ESPA_RESPUESTA_UNO)


def opc_2(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=ESPA_RESPUESTA_DOS)


def opc_3(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=ESPA_RESPUESTA_TRES)


def start(dispatcher: Dispatcher) -> None:
    """Iniciar los comandos de este modulo en el chatbot"""
    espa_menu_handler = CommandHandler('espa', menu)
    espa_opc1_handler = CommandHandler('espa_opc1', opc_1)
    espa_opc2_handler = CommandHandler('espa_opc2', opc_2)
    espa_opc3_handler = CommandHandler('espa_opc3', opc_3)

    dispatcher.add_handler(espa_menu_handler)
    dispatcher.add_handler(espa_opc1_handler)
    dispatcher.add_handler(espa_opc2_handler)
    dispatcher.add_handler(espa_opc3_handler)
