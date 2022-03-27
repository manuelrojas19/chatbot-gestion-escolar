from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, dispatcher
from constants import BOT_TOKEN
from functions import saludar, paginaGe, start, unknown, finalizarConsulta
from dictamenes import  dictamenMenu, dictamenOpc1, dictamenOpc2, dictamenOpc3
from ets import etsMenu, etsOpc1, etsOpc2, etsOpc3
from reinscripcion import reinscripcionMenu
from tramites import tramitesMenu

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
    reinscripcionMenu_handler = CommandHandler('reinscripcion', reinscripcionMenu)
    tramitesMenu_handler = CommandHandler('tramites', tramitesMenu)
    dictamenesMenu_handler = CommandHandler('dictamenes', dictamenMenu)
    dictamenesOpc1_handler = CommandHandler('dictamen_opc1', dictamenOpc1)
    dictamenesOpc2_handler = CommandHandler('dictamen_opc2', dictamenOpc2)
    dictamenesOpc3_handler = CommandHandler('dictamen_opc3', dictamenOpc3)
    etsMenu_handler = CommandHandler('ETS', etsMenu)
    etsOpc1_handler = CommandHandler('ets_opc1', etsOpc1)
    etsOpc2_handler = CommandHandler('ets_opc2', etsOpc2)
    etsOpc3_handler = CommandHandler('ets_opc3', etsOpc3)
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
    dispatcher.add_handler(unknown_handler)
    #Segundo sprint
    dispatcher.add_handler(reinscripcionMenu_handler)
    dispatcher.add_handler(tramitesMenu_handler)
    dispatcher.add_handler(dictamenesMenu_handler)
    dispatcher.add_handler(dictamenesOpc1_handler)
    dispatcher.add_handler(dictamenesOpc2_handler)
    dispatcher.add_handler(dictamenesOpc3_handler)
    dispatcher.add_handler(etsMenu_handler)
    dispatcher.add_handler(etsOpc1_handler)
    dispatcher.add_handler(etsOpc2_handler)
    dispatcher.add_handler(etsOpc3_handler)
    updater.start_polling()