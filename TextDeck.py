# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 13:21:54 2023

@author: recha
"""
from tkinter import *
import tkinter as tk 
from random import randint 
from tkinter import messagebox
import pandas as pd
import csv
import os

textdeck = tk.Tk()
textdeck.title('mémo - Text Deck')
textdeck.geometry('550x410')
icon = tk.PhotoImage(file = r'C:\Users\recha\Desktop\mémo\PythonComponents\Logo2.png')
textdeck.tk.call('wm','iconphoto', textdeck._w,icon)
textdeck.resizable(False,False)

    





#The 2D array word list stores the words that will be displayed in the Flashcards
#The first row stores the french word and the second row stores the word in English
wordlist = [((" Fille"),  ("Girl")),
            ((" Garçon"),  ("Boy")),
            ((" Femme"),  ("Woman")),
            (("Homme"),  ("Man")),
            (("Monsieur"),  ("Mister")),
            (("Mademoiselle"),  ("Miss")),
            (("Le marché"),  ("Market")),
            (("La plage"),  ("Beach")),
            (("Les Magasins"),  ("Shops")),
            (("L'auberge"),  ("Hostel")),
            (("Centre commercial"),  ("Shopping mall")),
            (("L'église"),  ("Church")),
            (("L'ambassade"),  ("Embassy")),
            (("Boulangerie "),  ("Bakery")),
            (("Pain"),  ("Bread")),
            (("Fromage"),  ("Cheese")),
            (("Viande"),  ("Meat")),
            (("Vin"),  ("Wine")),
            (("Thé"),  ("Tea")),
            (("Eau"),  ("Water")),
            (("Café"),  ("Coffee"))
]    

#Counts the number of rows in the wordlist array
wordlistlength = len(wordlist)

#Keeps track of the hints generated
hinter = ""
hintcount = 0
tries = 0
messagedisplayed = 0
easy = 0 
medium = 0 
difficult = 0


def display_results ():
#Creates a dataframe that stores the number of each flashcard difficulty alongside the corresponding difficulty name.
    userprogress = pd.DataFrame([[easy,medium,difficult]], columns = ['Easy','Medium','Difficult'])
    userprogress.to_csv('userprogress.csv',mode='a',index=False, header = False)
    #Destroys the textdeck rootwindow and opens the userprogress python file 
    execfile('userprogress.py')






#The hint method will generate a hint everytime the hint button is clicked
def generate_hint():
    global hintcount
    global hinter
    if hintcount < len(wordlist[randomnumber][1]):
        #Will output a letter from the english translation of the French output everytime the hint button is pressed.
         hinter = hinter + wordlist[randomnumber][1][hintcount]
         hintlabel.config(text=hinter)
         #Increments the value of the hintcount everytime the hint button is clicked
         hintcount +=1

def display_nextflashcard():
    
    
    
    global randomnumber
    #Randomly generates a number in the range of the length of the wordlist array.
    randomnumber = randint(0,wordlistlength-1)
    #Updates label with a French word
    frenchword.config(text=wordlist[randomnumber][0])
    hinter = ""

    #Reset Hint Value
    
    

    
   
    
def validate_answer():
    global wordlistlength
    #Allows the value of the length of the wordlist array to be updated outside of the submit subroutine 
    global hinter, hintcount
    global tries
    global randomnumber
    global difficult
    global easy
    global medium
    #Capitalises the value stored in the userentry input field
    answer = userentry.get().capitalize()
    print(answer)
    
    
    
        
    #Checks if the user input is equal to the english translation of the French word
    if answer == wordlist[randomnumber][1]  :
        messagebox.showinfo("Congratulations!", "That answer is correct.")
        tries +=1 
        print(tries)
        
        #Clears the answerlabel
        answerlabel.config(text="")
        #Clears all the characters stored in the user entry input field
        userentry.delete(0, END)
        #Clears all the contents of hintlabel 
        hintlabel.config(text="")
        wordlist.pop(randomnumber)
        hinter = ""
        hintcount = 0
        tries = 0
        #The pop method will remove the French word the user has answered correctly
        try:
            wordlistlength = len(wordlist)
            print(wordlistlength)
            randomnumber = randint(0,wordlistlength-1)
        #Updates label with a French word
            frenchword.config(text=wordlist[randomnumber][0])
        #The except conditional branch will prevent the randint error from occuring.
        except:
            print("")
            textdeck.destroy()
            dataframe = pd.DataFrame([easy,medium,difficult], columns = ['Easy','Medium','Difficult'])
            dataframe.to_csv('userprogress.csv',mode='a', index=False, header = False)
            frenchword.destroy()
            answerlabel.destroy()
            userentry.destroy()
            submitbutton.destroy()
            hintbutton.destroy()
            hintlabel.destroy()
            textlabel = Label(textdeck, text="You have completed all flashcards from the textdeck.")
            textlabel.place(x=100,y=20)
            resultsbutton = Button(text="Results ",command=display_results)
            resultsbutton.place(x=200,y=50)
            
            
            
        # Measures the difficulty of each flashcard
        if tries <= 2:
            easy += 1
        
        elif tries > 2 and tries <= 4:
            medium += 1
        
        elif tries > 4:
            difficult += 1
        #Outputs the number of each difficulty level of flashcards
        print ('Difficult:',difficult, 'Easy:',easy, 'Medium',medium )

       
        
    #Checks if the user input is equal to the correct answer
    elif answer != wordlist[randomnumber][1]:
        messagebox.showerror("Try Again!.", "That answer is incorrect.")
        tries +=1
    
        
        
    if answer == "":
         answerlabel.config(text=f"Please input an answer")
    
#Executes the instructions that will be executed when the program is closed using the windows 'X' button
def close_textdeck():
    print('Session Ended')
    #Creates a panda dataframe storing the user's progress with the flashcards and the corresponding column names
    userprogress = pd.DataFrame([[easy,medium,difficult]], columns = ['Easy','Medium','Difficult'])
    #Writes the contents of the dataframe to the userprogress csv file
    userprogress.to_csv('userprogress.csv',mode='a',index=False, header = False)
    #Closes the TextDeck rootwindow
    textdeck.destroy()
    

        
         
#Stores the Frenchword a user will be tested on        
frenchword = Label(textdeck, text="", font=("Helvetica", 20))
frenchword.pack(pady=50)


answerlabel = Label(textdeck, text="")
answerlabel.pack(pady=20)

#Input field used to store the user's answer to the flashcard
userentry = Entry(textdeck, font=("Helvetica", 18))
userentry.pack(pady=20)

#Frame used to store the position of the navigation buttons
buttonframe = Frame(textdeck)
buttonframe.pack(pady=20)

#Button used to submit an answer
submitbutton = Button(buttonframe, text="Submit",command=validate_answer)
submitbutton.grid(row=0, column=0, padx=20)


#Button used to generate a hint for the user
hintbutton = Button(buttonframe, text="Hint", command = generate_hint)
hintbutton.grid(row=0, column=2, padx=20)

#Label used to output a hint for the user 
hintlabel = Label(textdeck, text="")
hintlabel.pack(pady=15)


display_nextflashcard()
#Executes the instructions in the close_textdeck method when the windows close program event occurs
textdeck.protocol("WM_DELETE_WINDOW", close_textdeck)

textdeck.mainloop()
    
    
    
    
   