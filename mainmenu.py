# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 19:46:02 2022

@author: recha
"""
import tkinter as tk 
from tkinter import *
import subprocess
from PIL import ImageTk, Image
import os
import pandas as pd


userdata = pd.read_csv('AccountDetails.csv')
# reads from the AccountDetails csv file.
dataframe = pd.DataFrame(userdata)
currentuser = dataframe['Username'].iloc[-1]







def close_mainmenu():
    #closes the mainmenu root window 
    mainmenu.destroy()
    
def textdeckprogress():
    execfile('userprogress.py')

def imagedeckprogress():
    execfile('imageflashcardprogress.py')
    
def open_guide():
    os.system('python Guide.py')

def textdeck():
    subprocess.call(['python', 'TextDeck.py'])

def display_imagetext():
    subprocess.call(['python', 'imageflashcard.py'])    

def open_about():
    #Opens a toplevel window when the open method is executed
    about = Toplevel(mainmenu)
    about.geometry("800x663")
    about.title("About mémo")
    img = tk.PhotoImage(file = r'C:\Users\recha\Desktop\mémo\PythonComponents\Logo2.png')
    about.tk.call('wm','iconphoto', about._w,img)
    about.resizable(False,False)
    #Creates a canvas that will be used to display an image
    canvas = Canvas(about)
    canvas.pack()
    logo = tk.PhotoImage(file='Logo4.png')
    canvas.create_image(100,100,image=logo)
    #Displays the logo in the canvas
    canvas.place(x=300, y=0)
    canvas.image = logo
    frame = Frame(about, width=800, height=500,bg='#f0f0f0')
    frame.place(x=0, y=150)
    #Creates multiple labels used to display the text in the about toplevel window
    textlabel1 = Label(about,text='mémo is a flashcard software used for French. It is a free open source software.', fg='black', bg='#f0f0f0', font=('Segoe UI' ,10))
    textlabel1.place(x=20, y=160)
    textlabel2 = Label(about,text='Version 1.5.1 (xq21210b)', fg='black', bg='#f0f0f0', font=('Segoe UI' ,10))
    textlabel2.place(x=20, y=190)
    textlabel3 = Label(about,text='Python 3.9.13 Anaconda3 (2022.10) Spyder 5.2.2 ', fg='black', bg='#f0f0f0', font=('Segoe UI' ,10))
    textlabel3.place(x=20, y=220)
    textlabel4 = Label(about,text='Written by Rechad Hossaini', fg='black', bg='#f0f0f0', font=('Segoe UI' ,10))
    textlabel4.place(x=20, y=250)
    #The okbutton closes the about toplevel window when it is clicked.
    okbutton = Button(about, text='OK', height=1,width=5, bg='#e1e1e1',command=about.destroy)
    okbutton.place(x=754,y=635)   
   
    #Exit button stored in the about top level window which will close the about top level window when clicked.


 
    
    
    #The function guide will open a new Toplevel window which will be used to display a help log on how to use the program.
    
    

 
         
mainmenu = tk.Tk()
mainmenu.title('mémo- Main Menu')
mainmenu.geometry('1800x864')
mainmenu.state('zoomed')
img = tk.PhotoImage(file = r'C:\Users\recha\Desktop\mémo\PythonComponents\Logo2.png')
mainmenu.tk.call('wm','iconphoto', mainmenu._w,img)
mainmenu['background'] = '#fff'
usernamedisplay=Label(text= currentuser + "'s Session", fg='black', bg='#fff',font=('Segoe UI',10, 'bold'))
usernamedisplay.place(x=500, y=20)

#Creates the headers that will be displayed in the main menu 
Heading=Label(text='Deck', fg='black', bg='#fff', font=('Segoe UI',10, 'bold'))
Heading.place(x=500,y=50)
Heading2=Label(text='Review', fg='black', bg='#fff', font=('Segoe UI',10, 'bold'))
Heading2.place(x=900,y=50)


#Creates the frame to store the deck list
frame=Frame(mainmenu, width=500,height=350,bg="#fff")
frame.place(x=500,y=70)

#Creates a menu
menu1 = Menu(mainmenu)
mainmenu.config(menu=menu1)

#Creates the menu bar with the header 'file'
file_menu = Menu(menu1, tearoff=False)
menu1.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=close_mainmenu)

#Creates the menu bar with the header tools
tools_menu = Menu(menu1,tearoff = False)
menu1.add_cascade(label = "Tools", menu=tools_menu)
tools_menu.add_command(label="TextDeck Progress", command=textdeckprogress)
tools_menu.add_command(label="ImageDeck Progress", command=imagedeckprogress)

#Creates the menu bar with the header Help
help_menu = Menu(menu1, tearoff = False)
menu1.add_cascade(label = "Help", menu=help_menu)
#Executes the command guide when clicked
help_menu.add_command(label="Guide", command=open_guide)
#Adds a seperate menu in the menu bar
help_menu.add_separator()
#Executes the command open when the about menu bar is clicked
help_menu.add_command(label="About", command=open_guide)








#Displays the names of the decks users can study
Deckname1=Label(frame,text='mémo vocabulary deck',fg='black', bg='#fff',font=('Segoe UI',10))
Deckname1.place(x=0,y=0)
Deckname2=Label(frame,text='mémo image deck',fg='black', bg='#fff',font=('Segoe UI',10))
Deckname2.place(x=0,y=25)
reviewbutton1 = Button(mainmenu, text="Review",height=1,width=5, command=textdeck)
reviewbutton1.place(x=900,y=70)
reviewbutton2 = Button(mainmenu,text="Review",height=1,width=5, command= display_imagetext)
reviewbutton2.place(x=900,y=95)

#Exit button is used to close the main menu root window by executing the close_mainmenu function when it is clicked
exitbutton = Button(mainmenu, text="Exit",height=1,width=5, command=close_mainmenu)
exitbutton.place(x=700,y=720)

mainmenu.mainloop()
