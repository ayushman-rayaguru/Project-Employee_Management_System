from tkinter import*
from PIL import ImageTk
import os
import subprocess
from tkinter import messagebox as mb
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Employee Management System - by Ayushman")
        self.root.geometry("800x600")
        self.root.resizable(False,False)
        #self.root.title("Employee DBMS")
        self.root.iconbitmap('E:/Ayush/CODING/code/Projects/DB prj/main/dbico.ico')
        # BG image
        self.bg = ImageTk.PhotoImage(file = "E:/Ayush/CODING/code/Projects/DB prj/img.jpeg")
        self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        # Login Frame
        Frame_login = Frame(self.root,bg = "white")
        Frame_login.place(x = 50,y=50,height=340,width = 500)
        title = Label(Frame_login,text="Login Here",font=("OpenSans-SemiBold",35,"bold"),fg="blue",bg="white").place(x=90,y=30)
        desc = Label(Frame_login,text=" Database login area",font=("Goudy old style",15,"bold"),fg="blue",bg="white").place(x=90,y=100)

        lbl_user = Label(Frame_login,text=" Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user = Entry(Frame_login,font=("times new roman",15),bg = "lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        
        lbl_pass = Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass = Entry(Frame_login,font=("times new roman",15),bg = "lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        forget_btn = Button(Frame_login,text="Forget Password?",cursor = "hand2",bg = "white",fg ="blue",bd = 0,font = ("times new roman",12)).place(x=90,y=280)

        Login_btn = Button(self.root,command =self.login_function ,cursor = "hand2",text="Login",bg = "white",fg ="blue",bd = 0,font = ("times new roman",20)).place(x=370,y=390,width = 180,height = 40)
    
    def change(self):
        self.root.destroy()

    def login_function(self):
        if (self.txt_pass.get() =="" or self.txt_user.get()==""):
            mb.showerror("Error","All fields are required",parent = self.root)
        elif (self.txt_pass.get() !="1234" or self.txt_user.get()!="Ayushman"):
            mb.showerror("Error","Invalid Username/Password",parent = self.root)
        else:
            mb.showinfo("Welcome","Welcome",parent = self.root)
            subprocess.call('second.py 1',shell = True)
            exit()


root=Tk()
obj = Login(root)
root.mainloop()