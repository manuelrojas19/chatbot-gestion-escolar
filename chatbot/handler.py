from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, dispatcher
from constants import BOT_TOKEN
from functions import saludar, paginaGe, start, constancias, electivas, reinscripcion, e_r_materias, unknown, finalizarConsulta

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start_bot():    
    #Comandos de inicio y fin para establecer comunicacion con el ChatBot
    start_handler = CommandHandler('start', start)
    saludar1_handler = CommandHandler('hola', saludar)
    saludar2_handler = CommandHandler('buenosDias', saludar)
    saludar3_handler = CommandHandler('buenasTardes', saludar)
    saludar4_handler = CommandHandler('buenasNoches', saludar)
    finalizarConsulta1_handler = CommandHandler('gracias', finalizarConsulta)
    finalizarConsulta2_handler = CommandHandler('muchasGracias', finalizarConsulta)
    finalizarConsulta3_handler = CommandHandler('adios', finalizarConsulta)
    paginaGe_handler = CommandHandler('paginaGE', paginaGe)
    #Aqui ya comienzan los procesos para el sprint 2
    constancias_handler = CommandHandler('constancias', constancias)
    electivas_handler = CommandHandler('electivas', electivas)
    reinscripcion_handler = CommandHandler('reinscripcion', reinscripcion)
    equivalencias_r_handler = CommandHandler('equivalenciasYrevalidacion', e_r_materias)
    #funcion por defecto para comandos no registrados en el ChatBot
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(saludar1_handler)
    dispatcher.add_handler(saludar2_handler)
    dispatcher.add_handler(saludar3_handler)
    dispatcher.add_handler(saludar4_handler)
    dispatcher.add_handler(finalizarConsulta1_handler)
    dispatcher.add_handler(finalizarConsulta2_handler)
    dispatcher.add_handler(finalizarConsulta3_handler)
    dispatcher.add_handler(paginaGe_handler)
    dispatcher.add_handler(constancias_handler)
    dispatcher.add_handler(electivas_handler)
    dispatcher.add_handler(reinscripcion_handler)
    dispatcher.add_handler(equivalencias_r_handler)
    dispatcher.add_handler(unknown_handler)
    updater.start_polling()