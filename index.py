#importar bibliotecas 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser
from PyQt5.QtWidgets import QSplashScreen, QApplication 
from PyQt5.QtCore import QTimer 
from PyQt5.QtGui import QPixmap
import time


def splash():
    app = QApplication ([])




    pixmap = QPixmap("C:\\Users\\DELL\\Documents\\GitHub\\Marvelous-\\login\\icons\\splash.png")

    splash = QSplashScreen()
    splash.setPixmap(pixmap)

    QTimer.singleShot(7000, splash.close)
    QTimer.singleShot(7000, main.show)
    

    app.exec_()
 

def WorkSpace():
    work = Tk()
    work.title("Marvelous System - Work Area")
    work.geometry("1000x600")
    work.config(background="white")
    work.resizable(width=False, height=False)

   

    fundo = PhotoImage(file = "C:\\Users\\DELL\\Documents\\GitHub\\Marvelous-\\login\\icons\\Desktop.png")
    nan = PhotoImage(file = "C:\\Users\\DELL\\Documents\\GitHub\\Marvelous-\\login\\icons\\icon.png")
    

    LeftFrame = Frame(work, width=1000, height=600, bg="light steel blue", relief="raise")
    LeftFrame.pack(side=LEFT)

    LogoLabel = Label(LeftFrame, image=fundo, bg="light steel blue")
    LogoLabel.place(x=0, y=0)

    
    


    work.mainloop()

#criar janela 


       
def splash():
    app = QApplication ([])




    pixmap = QPixmap("C:\\Users\\DELL\\Documents\\GitHub\\Marvelous-\\login\\icons\\splash.png")

    splash = QSplashScreen()
    splash.setPixmap(pixmap)

    QTimer.singleShot(5000, splash.close)
   
                    
            
    splash.show()
    time_duration = 5
    time.sleep(time_duration)
    main()
    
   
def main():
    
    jan = Tk()
    jan.title("Salvatore - Acess Panel ")
    jan.geometry("700x300")
    jan.configure(background="white")
    jan.resizable(width=False, height=False)
    #configuar transparencia da janela  vvv
    jan.attributes("-alpha", 0.9)


    #==========caregando imagens
    logo = PhotoImage(file = "C:\\Users\\DELL\\Documents\\GitHub\\Marvelous-\\login\\icons\\backgroundlogin.png")
    logo1 = PhotoImage(file = "C:\\Users\\DELL\\Documents\\GitHub\\Marvelous-\\login\\icons\\backgroundregister.png")

    #======widgets=======
    LeftFrame = Frame(jan, width=700, height=300, bg="light steel blue", relief="raise")
    LeftFrame.pack(side=LEFT)

    LogoLabel = Label(LeftFrame, image=logo, bg="light steel blue")
    LogoLabel.place(x=0, y=0)

  

    UserEntry = ttk.Entry(LeftFrame, width=30)
    UserEntry.place(x=240, y=150)


    PassEntry = ttk.Entry(LeftFrame, width=30, show="•")
    PassEntry.place(x=240, y=185)


    def Login():
        User = UserEntry.get()
        Pass = PassEntry.get()

        DataBaser.cursor.execute("""
        SELECT * FROM Users 
        WHERE (User = ? and Password = ? )
        """, (User, Pass))
        print("selecionou")
        VerifyLogin = DataBaser.cursor.fetchone ()
        try:
            if (User in VerifyLogin and Pass in VerifyLogin):
                messagebox.showinfo(title="Login Info", message="Acess confirmed. Welcome!")
                jan.destroy()
                WorkSpace()
                

                
        except:
            messagebox.showinfo(title="Login Info", message="Incorrect username or password!check if the account  is existin!")
        

    #button
    LoginButton = ttk.Button(LeftFrame, text="Login", width=20, command=Login)
    LoginButton.place(x=180, y=230)

    def Register():
        '''
        LogoLabe2 = Label(LeftFrame, image=logo1, bg="light steel blue")
        LogoLabe2.place(x=0, y=0)
        '''
        #removendo widgets de login
        LoginButton.place(x=1000)
        RegisterButton.place(x=1000)
        #inserindo widgets de cadastro 
       
        NomeEntry = ttk.Entry(LeftFrame, width=30)
        NomeEntry.place(x=240, y=80)

        EmailEntry = ttk.Entry(LeftFrame, width=30)
        EmailEntry.place(x=240, y=115)


        def RegisterToDataBaser():
            Name = NomeEntry.get()
            Email = EmailEntry.get()
            User = UserEntry.get()
            Pass = PassEntry.get()

            if (Name == "" and Email == "" and User == "" and Pass =="" or Name == "" or Email == "" or User == "" or Pass == ""):
                messagebox.showerror(title= "Register Error", message="All fields are required! ")
            else:
                DataBaser.cursor.execute("""
                INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            
                """,(Name, Email, User, Pass))
                DataBaser.conn.commit()
                messagebox.showinfo(title="Register Info", message="Register Sucessfull")


        #criando botons
        Register = ttk.Button(LeftFrame, text="Register", width=20, command=RegisterToDataBaser)
        Register.place(x=340, y=230)

        def BackToLogin():
            #removendo widgets de cadastro
            
            NomeEntry.place(x=1000)
           
            EmailEntry.place(x=1000)
            Register.place(x=1000)
            Back.place(x=1000)
            LoginButton.place(x=180)
            RegisterButton.place(x=340)

        Back= ttk.Button(LeftFrame, text="Back", width=15, command=BackToLogin)
        Back.place(x=200, y=230)


    RegisterButton = ttk.Button(LeftFrame, text="Register", width=20, command=Register)
    RegisterButton.place(x=340, y=230)




    jan.mainloop()
    
splash()
