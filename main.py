#!/bin/env python
#-*-coding:utf-8-*-

"""
 JARwareZ proyect
"""
#
import os
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
import logging
import web

logging.basicConfig(format=('%(asctime)s - %(name)s - %(levelname)s - %(message)s'), level=logging.INFO)
logger = logging.getLogger('Kyo_Bot')
logger.info('Konichiwa master')  # esto metelo en otro archivo 

# Mensajes y tipos
  #logger.debug('TESTING')
  #logger.info('NORMAL')
  #logger.warning('ADVERTENCIA')
  #logger.error('PREOCUPATE')
  #logger.critical('YOU ARE X(´)')
#
#from config.auth import token
token = ('TOKEN') 

#¡PORT = int(os.environ.get('PORT, 5000')) """ Linea de codigo para HEROKU, descomentar al pasar al WebHook """

def start(update: Updater, context: CallbackContext) -> None:
   update.message.reply_text('Konichiwa, mi nombre es Kyo')
   logger.info('HAN INICIADO A KYO ¯\_(ツ)_/¯')


def main ():
  w = web.web()
  w.startThread()
  
  updater = Updater(token)
  dispatcher = updater.dispatcher

  # #Admin CLI
  dispatcher.add_handler(CommandHandler("start", start))

  # Start the Bot in local
  updater.start_polling();
  updater.idle()

if __name__ == '__main__':
  main()
