from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher
)

from telegram import Update

# REINSCRIPCION
reinscripcion_comandos = 'Por favor selecciona o escribe el comando de acuerdo a la pregunta que deseas consultar relacionadas al tema de Reinscripción.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Cuántas materias puedo reinscribir?: /reinscripcion_opc1\nPregunta 2:¿Si paso mis adeudos en la primera ronda de ETS, soy alumno regular?: /reinscripcion_opc2\nPregunta 3:¿Si cuento con dictamen vigente puedo reinscribirme?: /reinscripcion_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
# Pregunta 1: ¿Cuántas materias puedo reinscribir?
# respuesta 1
reinscripcion1 = '¿Cuántas materias puedo reinscribir?\n\nSi eres alumno regular cualquier carga académica.\n\nSi eres alumno irregular, tiene derecho entre tu carga mínima y media.\n\nConsultar las cargas en https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
# Pregunta 2: ¿Si paso mis adeudos en la primera ronda de ETS, soy alumno regular?
# respuesta 2
reinscripcion2 = '¿Si paso mis adeudos en la primera ronda de ETS, soy alumno regular?\n\nNo, eres alumno regular cuando al cierre del semestre no cuentas con materias adeudadas.\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
# Pregunta 3: ¿Si cuento con dictamen vigente puedo reinscribirme?
# respuesta 3
reinscripcion3 = '¿Si cuento con dictamen vigente puedo reinscribirme?\n\nSi, siempre y cuando tu dictamen ZACATENCO o UPIICSA te permita reinscripción.\n\nEn caso de duda consulta con tu asesor de carrera https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#ase\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'


def reinscripcion_menu(update: Update, context: CallbackContext) -> None:
    """Menu del módulo de reinscripciones"""
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=reinscripcion_comandos)


def rns_opc_1(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=reinscripcion1)


def rns_opc_2(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=reinscripcion2)


def rns_opc_3(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=reinscripcion3)


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
