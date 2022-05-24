from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher
)

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update

# REINSCRIPCION
# mensajes de regreso al menu
mensaje_regreso_menu = 'Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Reinscripción utiliza el comando: /reinscripcion\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

reinscripcion_comandos = 'Por favor selecciona o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Reinscripción.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Cuántas materias puedo reinscribir?: /reinscripcion_opc1\nPregunta 2:¿Si paso mis adeudos en la primera ronda de ETS, soy alumno regular?: /reinscripcion_opc2\nPregunta 3:¿Si cuento con dictamen vigente puedo reinscribirme?: /reinscripcion_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

REINSCRIPCION_PREGUNTA_UNO = '¿Cuántas materias puedo reinscribir?'
REINSCRIPCION_PREGUNTA_DOS = '¿Si paso mis adeudos en la primera ronda de ETS, soy alumno regular?'
REINSCRIPCION_PREGUNTA_TRES = '¿Si cuento con dictamen vigente puedo reinscribirme?'

REINSCRIPCION_RESPUESTA_UNO = '¿Cuántas materias puedo reinscribir?\n\nSi eres alumno regular cualquier carga académica.\n\nSi eres alumno irregular, tiene derecho entre tu carga mínima y media.\n\nConsultar las cargas en https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html\n\n\n' + mensaje_regreso_menu
REINSCRIPCION_RESPUESTA_DOS = '¿Si paso mis adeudos en la primera ronda de ETS, soy alumno regular?\n\nNo, eres alumno regular cuando al cierre del semestre no cuentas con materias adeudadas.\n\n\n' + mensaje_regreso_menu
REINSCRIPCION_RESPUESTA_TRES = '¿Si cuento con dictamen vigente puedo reinscribirme?\n\nSi, siempre y cuando tu dictamen ZACATENCO o UPIICSA te permita reinscripción.\n\nEn caso de duda consulta con tu asesor de carrera https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#ase\n\n\n' + mensaje_regreso_menu


preguntas = {REINSCRIPCION_PREGUNTA_UNO: REINSCRIPCION_RESPUESTA_UNO,
             REINSCRIPCION_PREGUNTA_DOS: REINSCRIPCION_RESPUESTA_DOS,
             REINSCRIPCION_PREGUNTA_TRES: REINSCRIPCION_RESPUESTA_TRES}


def reinscripcion_menu(update: Update, context: CallbackContext) -> None:
    """Menu del módulo de reinscripciones"""
    buttons = [[KeyboardButton(REINSCRIPCION_PREGUNTA_UNO)], [KeyboardButton(
        REINSCRIPCION_PREGUNTA_DOS)], [KeyboardButton(REINSCRIPCION_PREGUNTA_TRES)]]
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=reinscripcion_comandos, reply_markup=ReplyKeyboardMarkup(buttons))


def rns_opc_1(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=REINSCRIPCION_RESPUESTA_UNO)


def rns_opc_2(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=REINSCRIPCION_RESPUESTA_DOS)


def rns_opc_3(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=REINSCRIPCION_RESPUESTA_TRES)


def start(dispatcher: Dispatcher) -> None:
    """Iniciar los comandos de este modulo en el chatbot"""
    reinscripcion_menu_handler = CommandHandler(
        'reinscripcion', reinscripcion_menu)
    rns_opc_1_handler = CommandHandler('reinscripcion_opc1', rns_opc_1)
    rns_opc_2_handler = CommandHandler('reinscripcion_opc2', rns_opc_2)
    rns_opc_3_handler = CommandHandler('reinscripcion_opc3', rns_opc_3)

    dispatcher.add_handler(reinscripcion_menu_handler)
    dispatcher.add_handler(rns_opc_1_handler)
    dispatcher.add_handler(rns_opc_2_handler)
    dispatcher.add_handler(rns_opc_3_handler)
