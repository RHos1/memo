# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:15:39 2023

@author: recha
"""
import tkinter as tk 
from tkinter import *
from PIL import ImageTk, Image

guide = tk.Tk()
guide.title("Guide")
icon = tk.PhotoImage(file = r'C:\Users\recha\Desktop\mémo\PythonComponents\Logo2.png')
guide.tk.call('wm','iconphoto', guide._w,icon)
#Stores images using the PhotoImage module
guideimage1 = ImageTk.PhotoImage(Image.open('guide1.jpg'))
guideimage2 = ImageTk.PhotoImage(Image.open('guide2.jpg'))
guide.resizable(False,False)

def display_nextimage(imagenumber):
    #Changes the values of these identifiers outside of the method display_nextimage
    global imagedisplayer
    global backbutton
    global nextbutton
    
    #Removes the previous image displayed in the imagedisplayer label.
    imagedisplayer.grid_forget()
    imagedisplayer = Label(image=imagelist[imagenumber-1])
    #Changes the image value by passing the value of a different image when a specific button is clicked.
    nextbutton =Button(guide, text =">>", command=lambda: display_nextimage(imagenumber+1))
    backbutton = Button(guide, text="<<", command=lambda: display_previousimage(imagenumber-1))
    
    
    if imagenumber == 2:
        nextbutton =Button(guide, text =">>", state=DISABLED)
    
     
    backbutton.grid(row=1, column=0)
    nextbutton.grid(row=1, column=1)
    #Defines the position of the imagedisplayer label
    imagedisplayer.grid(row=0, column=0, columnspan=3)
    

    
#The method nextimage contains the instructions that will be executed when the nextbutton is clicked 

    
    
def display_previousimage(imagenumber):
    #Changes the values of these identifiers outside of the method previousimage
    global imagedisplayer
    global backbutton
    global nextbutton
    
    
    imagedisplayer.grid_forget()
    imagedisplayer = Label(image=imagelist[imagenumber-1])
    nextbutton =Button(guide, text =">>", command=lambda: display_nextimage(imagenumber+1))
    backbutton = Button(guide, text="<<", command=lambda: display_previousimage(imagenumber-1))
    
    if imagenumber == 1:
        backbutton = Button(guide, text="<<", state=DISABLED)
    
    
    imagedisplayer.grid(row=0, column=0, columnspan=3)
    backbutton.grid(row=1, column=0)
    nextbutton.grid(row=1, column=1)
    
    





#The method previous image contains the instructions that will be executed when the backbutton is clicked 
   


    

#Stores the guideimages in an array
imagelist = [guideimage1, guideimage2]



imagedisplayer = Label(image=guideimage1)

#Buttons used to navigate between the guide images
backbutton = Button(guide, text="<<", state=DISABLED)
#The lambda function passes a value to the buttons
nextbutton =Button(guide, text =">>", command=lambda: display_nextimage(2))
backbutton.grid(row=1, column=0)
nextbutton.grid(row=1, column=1)

 
guide.mainloop()