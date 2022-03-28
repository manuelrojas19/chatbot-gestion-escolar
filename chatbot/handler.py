from constants import BOT_TOKEN

from telegram.ext import (
    Updater,
    MessageHandler,
    Filters,
)

import inicio as inicio_comandos
import dictamenes as dictamentes_comandos
import ets as ets_comandos

RESPUESTA_DEFECTO_COMANDOS = 'Hola, es posible que el comando que ingresaste no es reconocido debido a un error de sintaxis o posiblemente no esté registrado dentro de las funciones que tiene este ChatBot, te recomendamos intentar nuevamente.\nEn caso de que el problema persista por favor, envía un correo directamente al área de Gestión Escolar de la UPIICSA en donde se te podrá atender de forma personalizada\nCorreo: tramitesgestionescolar@gmail.com o visita la página: https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html.\n\nDe igual manera puedes consultar todos los temas que abarca el ChatBot con el siguiente comando: /start'

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start_bot():
    """Iniciar el chatbot"""

    # Comandos de inicio y fin para establecer comunicacion con el ChatBot
    inicio_comandos.start(dispatcher=dispatcher)

    # Aqui ya comienzan los procesos para el sprint 2
    dictamentes_comandos.start(dispatcher=dispatcher)
    ets_comandos.start(dispatcher=dispatcher)

    # funcion por defecto para comandos no registrados en el ChatBot
    unknown_handler = MessageHandler(
        Filters.command, RESPUESTA_DEFECTO_COMANDOS)
    dispatcher.add_handler(unknown_handler)
    updater.start_polling()
