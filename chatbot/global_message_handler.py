import bajaDeUnidades
import bajas
import cargaMenor
import dictamenes
import electivas
import equivalencias
import espa
import ets
import inscripcionNI
import reinscripcion
import tramites

from telegram.ext import (
    CallbackContext,
    MessageHandler,
    Filters,
    Dispatcher
)

from telegram import Update


def global_message_handler(update: Update, context: CallbackContext) -> None:
    preguntas = {**bajaDeUnidades.preguntas, **bajas.preguntas, **cargaMenor.preguntas,
                 **dictamenes.preguntas, **electivas.preguntas, **equivalencias.preguntas,
                 **espa.preguntas, **ets.preguntas, **inscripcionNI.preguntas, **reinscripcion.preguntas,
                 **tramites.preguntas}

    for key, value in preguntas.items():
        if key in update.message.text:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=value)


def start(dispatcher: Dispatcher) -> None:
    """Iniciar los comandos de este modulo en el chatbot"""
    dispatcher.add_handler(MessageHandler(
        Filters.text, global_message_handler))
