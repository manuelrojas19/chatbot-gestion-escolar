from constants import BOT_TOKEN

from telegram.ext import Updater

import inicio as inicio_comandos
import dictamenes as dictamentes_comandos
import ets as ets_comandos
import tramites as tramites_comandos
import reinscripcion as reinscripcion_comandos
import inscripcionNI as inscripcionNI_comandos
import bajaDeUnidades as bajaDeUnidades_comandos
import bajas as bajas_comandos
import espa as espa_comandos
import cargaMenor as cargaMenor_comandos
import electivas as electivas_comandos
import equivalencias as equivalencias_comandos
import error_handler as error_handler


updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start_bot():
    """Iniciar el chatbot"""

    # Comandos de inicio y fin para establecer comunicacion con el ChatBot
    inicio_comandos.start(dispatcher=dispatcher)

    # Aqui ya comienzan los procesos para el sprint 2
    dictamentes_comandos.start(dispatcher=dispatcher)
    ets_comandos.start(dispatcher=dispatcher)
    reinscripcion_comandos.start(dispatcher=dispatcher)
    tramites_comandos.start(dispatcher=dispatcher)

    #Sprint 3
    inscripcionNI_comandos.start(dispatcher=dispatcher)
    bajaDeUnidades_comandos.start(dispatcher=dispatcher)
    bajas_comandos.start(dispatcher=dispatcher)
    espa_comandos.start(dispatcher=dispatcher)

    #Sprint 4
    cargaMenor_comandos.start(dispatcher=dispatcher)
    electivas_comandos.start(dispatcher=dispatcher)
    equivalencias_comandos.start(dispatcher=dispatcher)

    # Modulo de manejo de errores
    error_handler.start(dispatcher=dispatcher)

    updater.start_polling()
