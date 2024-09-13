# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 12:14:58 2023

@author: recha
"""
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from random import randint
import pandas as pd


images = ['banane','chat','chien','ecole','fromage','lait','pomme','restaurant','vache','voiture']
arraylength = len(images)

tries = 0 
easy = 0
medium = 0 
difficult = 0


#Runs instructions when the program is closed 
def close_imageflashcard():
    print('Session Ended')
#Creates a dataframe containing the progress a user has made with the image flashcards 
    dataframe = pd.DataFrame([[easy,medium,difficult]], columns = ['Easy','Medium','Difficult'])
#Outputs the dataframe to a csv file 
    dataframe.to_csv('imageflashcardprogress.csv',mode='a',index=False, header=False)
    imageflashcard.destroy()

def output_results():
#Creates a dataframe containing the progress a user has made with the image flashcards 
   dataframe = pd.DataFrame([[easy,medium,difficult]], columns = ['Easy','Medium','Difficult'])
#Outputs the dataframe to a csv file 
   dataframe.to_csv('imageflashcardprogress.csv',mode='a',index=False, header=False)
   #Runs the imageflashcardprogress python file 
   execfile('imageflashcardprogress.py')
















#Validates the user's input
def validate_answer():
    global tries
    global selectedimage
    global arraylength
    answer = answerfield.get().lower()

#Checks if the user's answer is equal to the name of the image file 
    if answer == selectedimage:
        messagebox.showinfo("Congratulations!",  answer + " is the correct answer!")
#Removes the image that was answered correctly from the images array 
        images.pop(randomnumber)
        tries +=1 
#Increments the value of tries
        arraylength = len(images)
        print (arraylength)
        nextimage()
        difficultylevels()
        answerfield.delete(0,END)
        tries = 0 
    
    #Checks if the answer field is left empty
    elif answer == "":
        messagebox.showerror("Syntax Error!", "User Entry is empty!")
        answerfield.delete(0,END)
    #Checks if the user's answer is not equal to the actual answer.
    elif answer != selectedimage:
        messagebox.showerror("Input Error!", answer + " is not the correct answer!")
        answerfield.delete(0,END)
        tries +=1    
        
#Calculates the number of easy,medium and difficult cards a user has studied      
def difficultylevels():
    global tries
    global easy
    global difficult
    global medium
    
#Used to calculate the difficulty level of each flashcard using the number of attempts a user has made
    if tries <=2:
        easy +=1
    if tries > 2 and tries <=4:
        medium +=1
    if tries >4:
        difficult += 1
#Outputs the number of easy,medium and difficult cards a user has studied 
    print('Easy:',easy, 'Medium:' ,medium, 'Difficult:',difficult,)
    

imageflashcard = Tk()
imageflashcard.title('mémo - Image Flashcard')
imageflashcard.geometry("500x500")

icon = tk.PhotoImage(file = r'C:\Users\recha\Desktop\mémo\PythonComponents\Logo2.png')
imageflashcard.tk.call('wm','iconphoto', imageflashcard._w,icon)
imageflashcard.resizable(False,False)



    

#Generates a random number for an index position in the images array


def nextimage():
    global selectedimage
    global randomnumber
    global image
    global showimage
    try:

#Randomly generates a number in the range of the length of the images array        
        randomnumber = randint(0,arraylength-1)
        selectedimage = images[randomnumber]
        #Stores the file location of an image from the image folder to display as a flashcard.    
        randomimage = "Images/" + selectedimage + ".jpg"
        image = ImageTk.PhotoImage(Image.open(randomimage))
        showimage = Label(imageflashcard, image=image)
        showimage.place(x=100,y=30)
#Prevents the randint error halting the execution of the program.
    except:
       #Removes the widgets from the rootwindow when the user has studied all the flashcards
       answerfield.destroy()
       answerbutton.destroy()
       showimage.destroy()
       instructions.destroy()
       textlabel = Label(imageflashcard, text="You have completed all flashcards from the textdeck.")
       textlabel.place(x=100,y=20)
       submitscore = Button(text="Submit Score",command=close_imageflashcard)
       submitscore.place(x= 240, y=400)
       

#Creates an answer input box
answerfield = Entry(imageflashcard,font=('Helvetica', 18))
answerfield.place(x=110, y=350)

#Displays a text label that will tell the user to write the French word for what is in the picture 
instructionslabel = Label(imageflashcard, text="Write what you see in French.")
instructionslabel.place(x=145, y=440)

#Creates a button that registers the user's question
answerbutton = Button(text="Answer", command=validate_answer)
answerbutton.place(x=195, y=400)

#Validates the answer


imageflashcard.protocol("WM_DELETE_WINDOW", close_imageflashcard)



#Displays the images to generate an image flashcard




#Creates the Frame that will store the images



nextimage()

imageflashcard.mainloop()