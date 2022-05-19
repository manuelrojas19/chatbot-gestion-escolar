from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Dispatcher

PAGINA_GESTION_ESCOLAR = 'https://www.upiicsa.ipn.mx/estudiantes/gestion-escolar.html'

CHATBOT_GE_COMANDOS = 'Hola, para comenzar escribe o elige alguno de los siguientes comandos relacionados a los temas de las dudas y preguntas más frecuentes de los alumnos hacia el departamento de Gestión Escolar de la UPIICSA:\n\nReinscripción: /reinscripcion\nTrámites: /tramites\nDictámenes: /dictamenes\nETS: /ETS\nInscripción: /inscripcion\nBaja de unidades: /bajaDeUnidades\nBajas: /bajas\nExamenes de saberes previamente adquiridos: /espa\nTrámites con Carga Menor a la Mínima: /cargaMenor\nElectivas: /electivas\nOtros:\nPágina de Gestión Escolar de la UPIICSA: /paginaGE\n\nRecuerda que para escribir un comando este debe de comenzar por una "/" seguido de la palabra clave del tema a consultar sin espacios entre palabras'


def inicio(update: Update, context: CallbackContext) -> None:
    """Mensaje de inicio del chatbot."""
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=CHATBOT_GE_COMANDOS)


def saludar(update: Update, context: CallbackContext) -> None:
    """Mensaje de saludo del chatbot."""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Mucho gusto, en que puedo servirte?, puedes ver el menú de todos los temas disponibles en este ChatBot tecleando o seleccionando el siguiente comando: /start')


def finalizar_consulta(update: Update, context: CallbackContext) -> None:
    """Mensaje de despedida del chatbot"""
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='Fue un placer atenderte, hasta luego.')


def pagina_ge(update: Update, context: CallbackContext) -> None:
    """Mensaje con la información de la página de gestión escolar."""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='La página de Gestión Escolar de la UPIICSA es:' + PAGINA_GESTION_ESCOLAR)


def start(dispatcher: Dispatcher) -> None:
    """Iniciar los comandos de este modulo en el chatbot"""
    inicio_handler = CommandHandler('start', inicio)
    saludar1_handler = CommandHandler('hola', saludar)
    saludar2_handler = CommandHandler('buenosDias', saludar)
    saludar3_handler = CommandHandler('buenasTardes', saludar)
    saludar4_handler = CommandHandler('buenasNoches', saludar)
    finalizarConsulta1_handler = CommandHandler('gracias', finalizar_consulta)
    finalizarConsulta2_handler = CommandHandler(
        'muchasGracias', finalizar_consulta)
    finalizarConsulta3_handler = CommandHandler('adios', finalizar_consulta)
    paginaGe_handler = CommandHandler('paginaGE', pagina_ge)

    dispatcher.add_handler(inicio_handler)
    dispatcher.add_handler(saludar1_handler)
    dispatcher.add_handler(saludar2_handler)
    dispatcher.add_handler(saludar3_handler)
    dispatcher.add_handler(saludar4_handler)
    dispatcher.add_handler(finalizarConsulta1_handler)
    dispatcher.add_handler(finalizarConsulta2_handler)
    dispatcher.add_handler(finalizarConsulta3_handler)
    dispatcher.add_handler(paginaGe_handler)
