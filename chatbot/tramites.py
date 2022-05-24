from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher
)

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update

# TRAMITES
#mensajes de regreso al menu
mensaje_regreso_menu = 'Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Trámites utiliza el comando: /tramites\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

tramites_comandos = 'Por favor selecciona la opción de los recuadros de abajo o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Trámites.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Dónde puedo solicitar un trámite?: /tramites_opc1\nPregunta 2:¿Cuánto es el tiempo de espera de mi trámite?: /tramites_opc2\nPregunta 3:¿Qué pasa si no puedo ingresar a la plataforma aún con mis datos de acceso?: /tramites_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'


TRAMITES_PREGUNTA_UNO = '¿Dónde puedo solicitar un trámite?'
TRAMITES_PREGUNTA_DOS = '¿Cuánto es el tiempo de espera de mi trámite?'
TRAMITES_PREGUNTA_TRES = '¿Qué pasa si no puedo ingresar a la plataforma aún con mis datos de acceso?'

TRAMITES_RESPUESTA_UNO = '¿Dónde puedo solicitar un trámite?\n\nDeberás solicitarlo a través de la plataforma www.tramites.upiicsa.ipn.mx\n\nUsuario: Boleta\n\nContraseña: Apellido paterno en minúsculas.\n\n\n' + mensaje_regreso_menu
TRAMITES_RESPUESTA_DOS = '¿Cuánto es el tiempo de espera de mi trámite?\n\nConstancias (estudios, periodo vacacional, servicio social y prácticas) de 5 a 10 días hábiles\n\nBoleta Global de 15 a 20 días hábiles\n\nBoleta Global Certificada de 30 a 40 días hábiles.\n\n\n' + mensaje_regreso_menu
TRAMITES_RESPUESTA_TRES = '¿Qué pasa si no puedo ingresar a la plataforma aún con mis datos de acceso?\n\nDeberás comunicarte con tu asesor de carrera\n\nhttps://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#ase\n\n\n' + mensaje_regreso_menu


preguntas = {TRAMITES_PREGUNTA_UNO: TRAMITES_RESPUESTA_UNO,
             TRAMITES_PREGUNTA_DOS: TRAMITES_RESPUESTA_DOS,
             TRAMITES_PREGUNTA_TRES: TRAMITES_RESPUESTA_TRES}

def tramites_menu(update: Update, context: CallbackContext) -> None:
    buttons = [[KeyboardButton(TRAMITES_PREGUNTA_UNO)], [KeyboardButton(
        TRAMITES_PREGUNTA_DOS)], [KeyboardButton(TRAMITES_PREGUNTA_TRES)]]
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=tramites_comandos, reply_markup=ReplyKeyboardMarkup(buttons))


def tramite_opc_1(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=TRAMITES_RESPUESTA_UNO)


def tramite_opc_2(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=TRAMITES_RESPUESTA_DOS)


def tramite_opc_3(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=TRAMITES_RESPUESTA_TRES)


def start(dispatcher: Dispatcher) -> None:
    """Iniciar los comandos de este modulo en el chatbot"""
    tramites_menu_handler = CommandHandler(
        'tramites', tramites_menu)
    tramites_opc_1_handler = CommandHandler('tramites_opc1', tramite_opc_1)
    tramites_opc_2_handler = CommandHandler('tramites_opc2', tramite_opc_2)
    tramites_opc_3_handler = CommandHandler('tramites_opc3', tramite_opc_3)

    dispatcher.add_handler(tramites_menu_handler)
    dispatcher.add_handler(tramites_opc_1_handler)
    dispatcher.add_handler(tramites_opc_2_handler)
    dispatcher.add_handler(tramites_opc_3_handler)

