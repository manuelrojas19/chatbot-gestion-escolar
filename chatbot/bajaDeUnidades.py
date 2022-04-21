from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher
)

from telegram import Update

# BAJA DE UNIDADES
#mensajes de regreso al menu
mensaje_regreso_menu = 'Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Baja de unidades utiliza el comando: /bajaDeUnidades\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

bajaDeUnidades_comandos = 'Por favor selecciona o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Baja de unidades.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Si tengo carga menor a la mínima, puedo dar de baja UA?: /bajaDeUnidades_opc1\nPregunta 2:¿Cuánto tiempo tengo para dar de baja UA?: /bajaDeUnidades_opc2\nPregunta 3:¿Puedo dar de baja recurses?: /bajaDeUnidades_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
# Pregunta 1: ¿Si tengo carga menor a la mínima, puedo dar de baja UA?
# respuesta 1
bajaDeUnidades1 = '¿Si tengo carga menor a la mínima, puedo dar de baja UA?\n\nNo es posible según el art 54 del RGE que nos cita “El alumno podrá solicitar baja de UA, en las que se encuentra inscrito en el periodos escolar siempre y cuando mantenga la carga mínima establecida en su plan de estudios.”\n\n\n' + mensaje_regreso_menu
# Pregunta 2: ¿Cuánto tiempo tengo para dar de baja UA?
# respuesta 2
bajaDeUnidades2 = '¿Cuánto tiempo tengo para dar de baja UA?\n\nDentro de las primeras 3 semanas una vez iniciado el semestre.\n\n\n' + mensaje_regreso_menu
# Pregunta 3: ¿Puedo dar de baja recurses?
# respuesta 3
bajaDeUnidades3 = '¿Puedo dar de baja recurses?\n\nNo es posible según el art 54 “Cuando el alumno esté recursando una unidad de aprendizaje no procederá la baja de la misma.”\n\n\n' + mensaje_regreso_menu


def bajaDeUnidadesMenu(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=bajaDeUnidades_comandos)


def bajaDeUnidadesOpc1(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=bajaDeUnidades1)


def bajaDeUnidadesOpc2(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=bajaDeUnidades2)


def bajaDeUnidadesOpc3(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=bajaDeUnidades3)


def start(dispatcher: Dispatcher) -> None:
    """Iniciar los comandos de este modulo en el chatbot"""
    bajaDeUnidadesMenu_handler = CommandHandler('bajaDeUnidades', bajaDeUnidadesMenu)
    bajaDeUnidadesOpc1_handler = CommandHandler('bajaDeUnidades_opc1', bajaDeUnidadesOpc1)
    bajaDeUnidadesOpc2_handler = CommandHandler('bajaDeUnidades_opc2', bajaDeUnidadesOpc2)
    bajaDeUnidadesOpc3_handler = CommandHandler('bajaDeUnidades_opc3', bajaDeUnidadesOpc3)

    dispatcher.add_handler(bajaDeUnidadesMenu_handler)
    dispatcher.add_handler(bajaDeUnidadesOpc1_handler)
    dispatcher.add_handler(bajaDeUnidadesOpc2_handler)
    dispatcher.add_handler(bajaDeUnidadesOpc3_handler)