# To get the URL
import requests 
# For the GUI of the project
from tkinter import *  
import tkinter as tk 
#  Importing various widgets
from tkinter import ttk
import re

# Creating a constructor for calculating the real time exchange rates
class CurrencyConverterRealTime():
    def __init__(self,url):
        # requests.get(url) will load the page in python program and .json will convert the page in json format
        self.data = requests.get(url).json()
        # Storing it in data variable
        self.currencies = self.data['rates']
    def convert(self, from_currency, to_currency, amount):
        intial_amount = amount
        # Keeping base currency as USD! 
        # If entered currency is not in USD converting it to USD first
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
            #precision of the rate upto 4 decimal points
        amount = round(amount * self.currencies[to_currency],4)
        return amount







       






