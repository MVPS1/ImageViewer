import tkinter as tk


class Button(tk.Button):


    def __init__(self, *args, **kwargs):
        super().__init__(bg='grey',height=10, width=20 ,*args, **kwargs)
       