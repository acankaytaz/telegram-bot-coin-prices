#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 18:10:51 2022

@author: acankaytaz
"""
import requests
import json
from datetime import datetime

print("bot activated....")

#coingecko api
req1 = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
                    , headers = {"accept" : "application/json"})

req2 = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
                    , headers = {"accept" : "application/json"})

price_eth = ("Price of ethereum is currently $" +str(req1.json() ['ethereum']['usd']))
price_btc = ("Price of bitcoin is currently $" +str(req2.json() ['bitcoin']['usd']))

def sample_responses(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ("hello", "hi", "selam"):
        return "heeey whatsup, welcome"
    
    if user_message in ("who are you", "who are you?", "kimsin", "kimsin?"):
        return "this is acan bot, nice to meet you!"
    
    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    
    if user_message in ("p eth", "ethereum", "eth", "eth price"):
        return price_eth
    
    if user_message in ("p btc", "bitcoin", "btc", "btc price"):
        return price_btc
    
    return "i don't understand you, sorry"