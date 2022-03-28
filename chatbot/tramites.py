from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher
)

from telegram import Update

# TRAMITES
tramites_comandos = 'Por favor selecciona o escribe el comando de acuerdo a la pregunta que deseas consultar relacionadas al tema de Trámites.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Dónde puedo solicitar un trámite?: /tramites_opc1\nPregunta 2:¿Cuánto es el tiempo de espera de mi trámite?: /tramites_opc2\nPregunta 3:¿Qué pasa si no puedo ingresar a la plataforma aún con mis datos de acceso?: /tramites_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
# Pregunta 1: ¿Dónde puedo solicitar un trámite?
# respuesta 1
tramites1 = '¿Dónde puedo solicitar un trámite?\n\nDeberás solicitarlo a través de la plataforma www.tramites.upiicsa.ipn.mx\n\nUsuario: Boleta\n\nContraseña: Apellido paterno en minúsculas.\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
# Pregunta 2: ¿Cuánto es el tiempo de espera de mi trámite?
# respuesta 2
tramites2 = '¿Cuánto es el tiempo de espera de mi trámite?\n\nConstancias (estudios, periodo vacacional, servicio social y prácticas) de 5 a 10 días hábiles\n\nBoleta Global de 15 a 20 días hábiles\n\nBoleta Global Certificada de 30 a 40 días hábiles.\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
# Pregunta 3: ¿Qué pasa si no puedo ingresar a la plataforma aún con mis datos de acceso?
# respuesta 3
tramites3 = '¿Qué pasa si no puedo ingresar a la plataforma aún con mis datos de acceso?\n\nDeberás comunicarte con tu asesor de carrera\n\nhttps://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#ase\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'


def tramites_menu(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=tramites_comandos)


def tramite_opc_1(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=tramites1)


def tramite_opc_2(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=tramites2)


def tramite_opc_3(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=tramites3)


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

