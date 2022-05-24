from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher
)

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update

# ETS
#mensajes de regreso al menu
mensaje_regreso_menu = 'Si deseas seguir viendo las dudas y preguntas relacionadas al tema de ETS utiliza el comando: /ETS\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

ets_comandos = 'Por favor selecciona la opción de los recuadros de abajo o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de ETS.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Cómo se si tengo derecho a ETS?: /ets_opc1\nPregunta 2:¿Qué puedo hacer si mi profesor no acento o se equivocó de calificación?: /ets_opc2\nPregunta 3:¿Cómo solicito revisión a un examen ETS?: /ets_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

ETS_PREGUNTA_UNO = '¿Cómo se si tengo derecho a ETS?'
ETS_PREGUNTA_DOS = '¿Qué puedo hacer si mi profesor no acento o se equivocó de calificación?'
ETS_PREGUNTA_TRES = '¿Cómo solicito revisión a un examen ETS?'

ETS_RESPUESTA_UNO = '¿Cómo se si tengo derecho a ETS?\n\nSi estuviste inscrito al periodo correspondiente anterior o cuentas con un dictamen vigente que te permita presentarlo.\n\n\n' + mensaje_regreso_menu
ETS_RESPUESTA_DOS = '¿Qué puedo hacer si mi profesor no acento o se equivocó de calificación?\n\nEl profesor deberá solicitar la corrección al departamento de gestión escolar.\n\n\n' + mensaje_regreso_menu
ETS_RESPUESTA_TRES = '¿Cómo solicito revisión a un examen ETS?\n\nDeberás solicitarlo al Profesor sinodal con apoyo del jefe de la academia correspondiente.\n\n\n' + mensaje_regreso_menu

preguntas = {ETS_PREGUNTA_UNO: ETS_RESPUESTA_UNO,
             ETS_PREGUNTA_DOS: ETS_RESPUESTA_DOS,
             ETS_PREGUNTA_TRES: ETS_RESPUESTA_TRES}


def etsMenu(update: Update, context: CallbackContext) -> None:
    buttons = [[KeyboardButton(ETS_PREGUNTA_UNO)], [KeyboardButton(
        ETS_PREGUNTA_DOS)], [KeyboardButton(ETS_PREGUNTA_TRES)]]
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=ets_comandos, reply_markup=ReplyKeyboardMarkup(buttons))


def etsOpc1(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=ETS_PREGUNTA_UNO)


def etsOpc2(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=ETS_RESPUESTA_DOS)


def etsOpc3(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=ETS_RESPUESTA_TRES)


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
