#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 18:08:31 2022

@author: acankaytaz

"""
import Constants as keys
from telegram.ext import *
import Responses as Res


#bot
def start_command(update, context):
    update.message.reply_text('Type something random to get started. To see some commands pls type /help')
    
def help_command(update, context):
    update.message.reply_text('Welcome to Acan bot \nTo check price of some coins you can type: \nFor Ethereum: eth, eth price, p eth \nFor Bitcoin: btc, btc price, p btc')
    
def handle_message(update, context):
    text = str(update.message.text).lower()
    response = Res.sample_responses(text)   
    update.message.reply_text(response)
    
def error(update, context):
    print(f"Update {update} caused error {context.error} ")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()
    
    
main()