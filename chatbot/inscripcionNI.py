from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher
)

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update

# INSCRIPCION
#mensajes de regreso al menu
mensaje_regreso_menu = 'Si deseas seguir viendo las dudas y preguntas relacionadas al tema de Inscripción utiliza el comando: /inscripcion\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'

inscripcion_comandos = 'Por favor selecciona la opción de los recuadros de abajo o escribe el comando de acuerdo a la pregunta que deseas consultar relacionada al tema de Inscripción.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1:¿Qué documentos debo de entregar?: /inscripcion_opc1\nPregunta 2:¿Cómo podré ver mi horario?: /inscripcion_opc2\nPregunta 3:¿Cómo solicito cambio de turno?: /inscripcion_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
# Pregunta 1: ¿Qué documentos debo de entregar?
# respuesta 1

INSCRIPCION_PREGUNTA_UNO = '¿Qué documentos debo de entregar?'
INSCRIPCION_PREGUNTA_DOS = '¿Cómo podré ver mi horario?'
INSCRIPCION_PREGUNTA_TRES = '¿Cómo solicito cambio de turno?'

INSCRIPCION_RESPUESTA_UNO = '¿Qué documentos debo de entregar?\n\nDeberás subir en archivo PDF a la plataforma www.tramites.upiicsa.ipn.mx y entregar en forma física cuando te sea solicitado, los siguientes:\n-Identificación Oficial\n-Copia Acta de Nacimiento\n-2 Fotografías tamaño infantil\n-Copia CURP\n-Hoja de datos generales ( descárgala aquí https://bit.ly/3r0UVeg ) Original y copia\n-Solicitud de inscripción Original y copia\n-Copia de donativo \n-Copia certificado de bachillerato\n\n\n' + mensaje_regreso_menu
INSCRIPCION_RESPUESTA_DOS = '¿Cómo podré ver mi horario?\n\nSe publicará la fecha en la página de UPIICSA, y deberás de ingresar a www.saes.upiics.ipn.mx\nUsuario: Número de Boleta, PP o PE\nPassword: Primeras 4 letras de tu apellido paterno en minúsculas.\n\n\n' +  mensaje_regreso_menu
INSCRIPCION_RESPUESTA_TRES = '¿Cómo solicito cambio de turno?\n\nLos cambios de turno y permutas no se realizan, recuerda que, a partir del 2do semestre, tu puedes elegir las materias y turno a cursar.\n\n\n' + mensaje_regreso_menu

preguntas = {INSCRIPCION_PREGUNTA_UNO: INSCRIPCION_RESPUESTA_UNO,
             INSCRIPCION_PREGUNTA_DOS: INSCRIPCION_RESPUESTA_DOS,
             INSCRIPCION_PREGUNTA_TRES: INSCRIPCION_RESPUESTA_TRES}

def inscripcionMenu(update: Update, context: CallbackContext) -> None:
    buttons = [[KeyboardButton(INSCRIPCION_PREGUNTA_UNO)], [KeyboardButton(
        INSCRIPCION_PREGUNTA_DOS)], [KeyboardButton(INSCRIPCION_PREGUNTA_TRES)]]
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=inscripcion_comandos, reply_markup=ReplyKeyboardMarkup(buttons))


def inscripcionOpc1(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=INSCRIPCION_RESPUESTA_UNO)


def inscripcionOpc2(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=INSCRIPCION_RESPUESTA_DOS)


def inscripcionOpc3(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=INSCRIPCION_RESPUESTA_TRES)


def start(dispatcher: Dispatcher) -> None:
    """Iniciar los comandos de este modulo en el chatbot"""
    inscripcionMenu_handler = CommandHandler('inscripcion', inscripcionMenu)
    inscripcionOpc1_handler = CommandHandler('inscripcion_opc1', inscripcionOpc1)
    inscripcionOpc2_handler = CommandHandler('inscripcion_opc2', inscripcionOpc2)
    inscripcionOpc3_handler = CommandHandler('inscripcion_opc3', inscripcionOpc3)

    dispatcher.add_handler(inscripcionMenu_handler)
    dispatcher.add_handler(inscripcionOpc1_handler)
    dispatcher.add_handler(inscripcionOpc2_handler)
    dispatcher.add_handler(inscripcionOpc3_handler)