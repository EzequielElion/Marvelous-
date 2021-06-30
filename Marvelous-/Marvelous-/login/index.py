#importar bibliotecas 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser
#criar janela 
jan = Tk()
jan.title("Marvelous System - Acess Panel ")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
#configuar transparencia da janela  vvv
jan.attributes("-alpha", 0.9)


#==========caregando imagens
logo = PhotoImage(file = "C:\\Users\\DELL\\Documents\\GitHub\\Marvelous-\\login\\icons\\logot.png")

#======widgets=======
LeftFrame = Frame(jan, width=200, height=300, bg="light steel blue", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=400, height=300, bg="azure", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="light steel blue")
LogoLabel.place(x=20, y=60)

UserLabel = Label(RightFrame, text="Username", font=("Noto Serif", 20),bg="azure", fg="grey19")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=170, y=110)

PassLabel = Label(RightFrame, text="Password", font=("Noto Serif", 20),bg="azure", fg="grey19"  )
PassLabel.place(x=5, y=140)

PassEntry = ttk.Entry(RightFrame, width=30, show="•")
PassEntry.place(x=170, y=150)


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
    except:
        messagebox.showinfo(title="Login Info", message="Incorrect username or password!check if the account  is existin!")
    

#button
LoginButton = ttk.Button(RightFrame, text="Login", width=20, command=Login)
LoginButton.place(x=70, y=200)

def Register():
    #removendo widgets de login
    LoginButton.place(x=1000)
    RegisterButton.place(x=1000)
    #inserindo widgets de cadastro 
    NomeLabel = Label(RightFrame, text="Name", font=("Noto Serif", 20), bg="azure", fg="grey19")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=170, y=15)

    EmailLabel = Label(RightFrame, text="Email", font=("Noto Serif",20), bg="azure", fg="grey19")
    EmailLabel.place(x=5, y=50)

    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=170, y=60)


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
    Register = ttk.Button(RightFrame, text="Register", width=20, command=RegisterToDataBaser)
    Register.place(x=70, y=200)

    def BackToLogin():
        #removendo widgets de cadastro
        NomeLabel.place(x=1000)
        NomeEntry.place(x=1000)
        EmailLabel.place(x=1000)
        EmailEntry.place(x=1000)
        Register.place(x=1000)
        Back.place(x=1000)
        LoginButton.place(x=70)
        RegisterButton.place(x=210)

    Back= ttk.Button(RightFrame, text="Back", width=15, command=BackToLogin)
    Back.place(x=210, y=200)


RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=210, y=200)




jan.mainloop()