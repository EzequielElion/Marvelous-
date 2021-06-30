from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser


def WorkSpace():
    work = Tk()
    work.title("Marvelous System - Work Area")
    work.geometry("1000x600")
    work.config(background="white")
    work.resizable(width=False, height=False)


    LeftFrame = Frame(work, width=200, height=600, bg="light steel blue", relief="raise")
    LeftFrame.pack(side=LEFT)

    TopFrame = Frame(work, width=1000, height=40, bg="Pale Turquoise4", relief="raise" )
    TopFrame.pack(side=TOP)



    work.mainloop()