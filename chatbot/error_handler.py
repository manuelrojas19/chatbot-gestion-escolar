from telegram.ext import (
    CallbackContext,
    MessageHandler,
    Filters,
    Dispatcher
)

from telegram import Update

RESPUESTA_DEFECTO_COMANDOS = 'Hola, es posible que el comando que ingresaste no es reconocido debido a un error de sintaxis o posiblemente no esté registrado dentro de las funciones que tiene este ChatBot, te recomendamos intentar nuevamente.\nEn caso de que el problema persista por favor, envía un correo directamente al área de Gestión Escolar de la UPIICSA en donde se te podrá atender de forma personalizada\nCorreo: tramitesgestionescolar@gmail.com o visita la página: https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html.\n\nDe igual manera puedes consultar todos los temas que abarca el ChatBot con el siguiente comando: /start'


def unknown(update: Update, context: CallbackContext) -> None:
    """Mensaje de error para algun comando desconocido."""
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=RESPUESTA_DEFECTO_COMANDOS)


def start(dispatcher: Dispatcher) -> None:
    """Iniciar los comandos de este modulo en el chatbot"""
    # funcion por defecto para comandos no registrados en el ChatBot
    unknown_handler = MessageHandler(
        Filters.command, unknown)

    dispatcher.add_handler(unknown_handler)
