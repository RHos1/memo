# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 14:36:57 2022

@author: recha
"""


from tkinter import *
import subprocess
import tkinter as tk
#imports the library tkinter which will allow me to use the pre-programmed objects of tkinter.
loginmenu = tk.Tk()
#Creates a root window with the name window
loginmenu.title('mémo - Login Menu')
# stores the image Logo2 under the identifier icon using the PhotoImage method
icon = tk.PhotoImage(file = r'C:\Users\recha\Desktop\mémo\PythonComponents\Logo2.png')
#Outputs the Logo as an Icon on top of the loginmenu rootwindow.
loginmenu.tk.call('wm','iconphoto', loginmenu._w,icon)
loginmenu.geometry('300x250')
loginmenu.resizable(False,False)
#Sets the background colour of the loginmenu root window to the specified hex colour
loginmenu['background']='#76b5c5'

def login():
     loginmenu.destroy()
     subprocess.call(['python','login.py'])
     #the function 'login' will open the python file 'login.py' which will allow users to login to the program.
     

def open_register():
    loginmenu.destroy()
    subprocess.call(['python','register.py'])
#the subprocess method will open the external 'register' python file within the Login Menu when the
    
Label(text = "mémo", bg = "#76b5c5", width = "300", height = "2", font = ("Microsoft Yahei Ui Light", 16, 'bold')).pack()
registerbutton = Button(loginmenu, text ="Register", height = "2", width = "20", command=open_register).pack()
Label(text ="", bg="#76b5c5").pack()
Loginbutton = Button(loginmenu, text ="Login",height="2", width="20", command = login).pack()
loginmenu.mainloop()
#Runs the Tkinter event loop which will allow the window root window to be displayed when the code is executed.








