from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, dispatcher

#ETS
ets_comandos = 'Por favor selecciona o escribe el comando de acuerdo a la pregunta que deseas consultar relacionadas al tema de ETS.\nCada pregunta tiene un comando asociado, verifica y elige el adecuado.\n\nPregunta 1: ¿Cómo se si tengo derecho a ETS?: /ets_opc1\n#Pregunta 2: ¿Qué puedo hacer si mi profesor no acento o se equivocó de calificación?: /ets_opc2\n#Pregunta 3: ¿Cómo solicito revisión a un examen ETS? /ets_opc3\n\nSi deseas volver para consultar el menú principal de los temas que abarca este Chatbot utiliza el comando: /start'
#Pregunta 1: ¿Cómo se si tengo derecho a ETS?
#respuesta 1
ets1 = 'Si estuviste inscrito al periodo correspondiente anterior o cuentas con un dictamen vigente que te permita presentarlo.'
#Pregunta 2: ¿Qué puedo hacer si mi profesor no acento o se equivocó de calificación?
#respuesta 2
ets2 = 'El profesor deberá solicitar la corrección al departamento de gestión escolar.'
#Pregunta 3: ¿Cómo solicito revisión a un examen ETS?
#respuesta 3
ets3 = 'Deberás solicitarlo al Profesor sinodal con apoyo del jefe de la academia correspondiente.'

def etsMenu(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=ets_comandos)

def etsOpc1(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=ets1)

def etsOpc2(update, context):    
    context.bot.send_message(chat_id=update.effective_chat.id, text=ets2)

def etsOpc3(update, context):    
    context.bot.send_message(chat_id=update.effective_chat.id, text=ets3)