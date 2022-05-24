# To get the URL
import requests
# For the GUI of the project
from tkinter import *
import tkinter as tk
#  Importing various widgets
from tkinter import ttk

# Creating a constructor for calculating the real time exchange rates


class CurrencyConverterRealTime():
    def __init__(self, url):
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
            # precision of the rate upto 4 decimal points
        amount = round(amount * self.currencies[to_currency], 4)
        return amount

# Creating an UI for the Currency Converter


class App(tk.Tk):
    # Creating the frame of the converter


    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = "Currency Converter"
        self.currency_converter = converter
        # Creating the converter
        self.geometry("600x450")

        # Label
        self.intro_label = Label(self, text="The Real Time Currency Converter made in Python",
                             fg="blue", relief=tk.RAISED, borderwidth=4)
        self.intro_label.config(font=('Courier', 15, 'bold'))
        self.date_label = Label(
        self, text=f"1 Indian Rupee equals = {self.currency_converter.convert('INR','USD',1)} USD \n Date : {self.currency_converter.data['date']}", relief=tk.GROOVE, borderwidth=5)
        self.intro_label.place(relx= 0.5,rely=0.5, anchor='center')
        self.date_label.place(x=170, y=50)
        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        # restricNumberOnly function will restrict thes user to enter invavalid number in Amount field. We will define it later in code
        self.amount_field = Entry(self, bd=3, relief=tk.RIDGE,
                              justify=tk.CENTER, validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(
        self, text='', fg='black', bg='white', relief=tk.RIDGE, justify=tk.CENTER, width=17, borderwidth=3)

    # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("INR")  # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD")  # default value

        font = ("Times New Roman", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable, values=list(
        self.currency_converter.currencies.keys()), font=font, state='readonly', width=12, justify=tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable, values=list(
        self.currency_converter.currencies.keys()), font=font, state='readonly', width=12, justify=tk.CENTER)

        # placing
        self.from_currency_dropdown.place(x=30, y=120)
        self.amount_field.place(x=36, y=150)
        self.to_currency_dropdown.place(x=340, y=120)
        #self.converted_amount_field.place(x = 346, y = 150)
        self.converted_amount_field_label.place(x=346, y=150)

        # Convert button
        self.convert_button = Button(
        self, text="Convert", fg="black", command=self.perform)
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.place(x=245, y=155)

    def perform(self,):
            amount = float(self.amount_field.get())
            from_curr = self.from_currency_variable.get()
            to_curr = self.to_currency_variable.get()

            converted_amount = self.currency_converter.convert(
                from_curr, to_curr, amount)
            converted_amount = round(converted_amount, 2)

            self.converted_amount_field_label.config(text=str(converted_amount))

    def restrictNumberOnly(self, action, string):
            regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
            result = regex.match(string)
            return (string == "" or (string.count('.') <= 1 and result is not None))

if __name__ == '__main__':
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        converter = CurrencyConverterRealTime(url)

        App(converter)
        mainloop()


