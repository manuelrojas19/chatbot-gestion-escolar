from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher
)

from telegram import Update

#REINSCRIPCION
reinscripcion_comandos = 'Por favor selecciona o escribe el comando de acuerdo a la pregunta que deseas consultar relacionadas al tema de Dictámenes.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1: ¿Cuántas materias puedo reinscribir?: /reinscripcion_opc1\nPregunta 2: ¿Si paso mis adeudos en la primera ronda de ETS, soy alumno regular?: /reinscripcion_opc2\n#Pregunta 3: ¿Si cuento con dictamen vigente puedo reinscribier?: /reinscripcion_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
# Pregunta 1: ¿Qué dictamen debo de solicitar si estoy desfasado?
# respuesta 1
reinscripcion1 = 'Si tu periodo de ingreso es del 17/2 en adelante, deberás solicitar dictamen UPIICSA por oportunidad\n\nSi tu periodo es 17/1 hacía atrás, deberás solicitar dictamen CGC ZACATENCO por oportunidad'
# Pregunta 2: ¿En qué casos debo de solicitar dictamen ZACATENCO?
# respuesta 2
reinscripcion2 = 'Si tu periodo de ingreso fue del 17/1 hacia atrás debes de solicitar ampliación de plazo para tener derecho a reinscripción\n\nSi tu periodo de ingreso fue del 17/1 hacia atrás y tienes materias adeudadas o desfasas , debes solicitar oportunidad.'
# Pregunta 3: ¿Dónde puedo ver la resolución de mi dictamen?
# respuesta 3
reinscripcion3 = 'Si solicitaste dictamen UPIICSA, directamente en tu SAES en el apartado Dictamenes \n\nSi solicitaste dictamen CGC Zacatenco en la página de UPIICSA https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html#dicz'



def reinscripcion_menu(update: Update, context: CallbackContext) -> None:
    """Menu del módulo de reinscripciones"""
    context.bot.send_message(chat_id=update.effective_chat.id, text=reinscripcion_comandos)

def start(dispatcher: Dispatcher) -> None:
    """Iniciar los comandos de este modulo en el chatbot"""
    reinscripcion_menu_handler = CommandHandler('reinscripcion', reinscripcion_menu)

    dispatcher.add_handler(reinscripcion_menu_handler)
