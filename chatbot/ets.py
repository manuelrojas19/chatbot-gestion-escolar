from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher
)

from telegram import Update

# ETS
ets_comandos = 'Por favor selecciona o escribe el comando de acuerdo a la pregunta que deseas consultar relacionadas al tema de ETS.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1: ¿Cómo se si tengo derecho a ETS?: /ets_opc1\n#Pregunta 2: ¿Qué puedo hacer si mi profesor no acento o se equivocó de calificación?: /ets_opc2\n#Pregunta 3: ¿Cómo solicito revisión a un examen ETS? /ets_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
# Pregunta 1: ¿Cómo se si tengo derecho a ETS?
# respuesta 1
ets1 = 'Si estuviste inscrito al periodo correspondiente anterior o cuentas con un dictamen vigente que te permita presentarlo.'
# Pregunta 2: ¿Qué puedo hacer si mi profesor no acento o se equivocó de calificación?
# respuesta 2
ets2 = 'El profesor deberá solicitar la corrección al departamento de gestión escolar.'
# Pregunta 3: ¿Cómo solicito revisión a un examen ETS?
# respuesta 3
ets3 = 'Deberás solicitarlo al Profesor sinodal con apoyo del jefe de la academia correspondiente.'


def etsMenu(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=ets_comandos)


def etsOpc1(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=ets1)


def etsOpc2(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=ets2)


def etsOpc3(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=ets3)


def start(dispatcher: Dispatcher) -> None:
    """Iniciar los comandos de este modulo en el chatbot"""
    etsMenu_handler = CommandHandler('ETS', etsMenu)
    etsOpc1_handler = CommandHandler('ets_opc1', etsOpc1)
    etsOpc2_handler = CommandHandler('ets_opc2', etsOpc2)
    etsOpc3_handler = CommandHandler('ets_opc3', etsOpc3)

    dispatcher.add_handler(etsMenu_handler)
    dispatcher.add_handler(etsOpc1_handler)
    dispatcher.add_handler(etsOpc2_handler)
    dispatcher.add_handler(etsOpc3_handler)
