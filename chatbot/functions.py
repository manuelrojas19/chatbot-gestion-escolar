from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, dispatcher

chatBotGE_comandos = 'Hola, mucho gusto. Para comenzar escribe o elige alguno de los siguientes comandos relacionados a los temas de las dudas y preguntas más frecuentes de los alumnos hacia el departamento de Gestión Escolar de la UPIICSA:\n\nReinscripción: /reinscripcion\nTrámites: /tramites\nDictámenes: /dictamenes\nETS: /ETS\nOtros:\nPágina de Gestión Escolar de la UPIICSA: /paginaGE\n\nRecuerda que para escribir un comando este debe de comenzar por una "/" seguido de la palabra clave del tema a consultar sin espacios entre palabras'
respuestaPorDefecto_comandos = 'Hola, es posible que el comando que ingresaste no es reconocido debido a un error de sintaxis o posiblemente no esté registrado dentro de las funciones que tiene este ChatBot, te recomendamos intentar nuevamente.\nEn caso de que el problema persista por favor, envía un correo directamente al área de Gestión Escolar de la UPIICSA en donde se te podrá atender de forma personalizada\nCorreo: tramitesgestionescolar@gmail.com o visita la página: https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html.\n\nDe igual manera puedes consultar todos los temas que abarca el ChatBot con el siguiente comando: /start'


#funciones para establecer y finalizar conversacion con el ChatBot
def start(update, context):    
    context.bot.send_message(chat_id=update.effective_chat.id, text=chatBotGE_comandos)

def saludar(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Mucho gusto, en que puedo servirte?, puedes ver el menú de todos los temas disponibles en este ChatBot tecleando o seleccionando el siguiente comando: /start')

def finalizarConsulta(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Fue un placer atenderte, hasta luego.')

def paginaGe(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='La página de Gestión Escolar de la UPIICSA es:https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html')

#Funcion para respoder por defecto a todos los comandos no registrados en el ChatBot
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=respuestaPorDefecto_comandos)