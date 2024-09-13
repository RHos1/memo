# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 12:32:42 2022

@author: recha
"""

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import pandas as pd
import csv
import subprocess
import os
import hashlib

#Defines the main properties of the login interface root window 
login = tk.Tk()
login.title('mémo - Login')
login.geometry('925x500+300+200')
img = tk.PhotoImage(file = r'C:\Users\recha\Desktop\mémo\PythonComponents\Logo2.png')
login.tk.call('wm','iconphoto', login._w,img)
login.configure(bg='#fff')
#prevents the login root window from being resized.
login.resizable(False,False)

#Stores an image under the identifier image1 using the photoimage method 
image1 = PhotoImage(file ='Login_.png')
#Displays the image stored in the identifier image1
Label(login, image=image1, bg='white').place(x=50,y=50)

#creates a frame that will be used to contain different labels
frame = Frame(login, width=350, height=350, bg="white")
frame.place(x=480, y=70)

#Displays the header for the Login menu
heading=Label(frame,text='Sign in',fg='#57a1f8' , bg='white', font=('Microsoft Yahei Ui Light',23,'bold'))
heading.place(x=100,y=5)

def save_username():
    #Creates a dataframe containing a user's username with the corresponding column name
    usernames = pd.DataFrame([[username]], columns = ['Username'])
    #Writes the dataframe to a csv file 
    usernames.to_csv('Logins.csv',mode='a', index=False, header=False)





def signup():
    login.destroy()
    os.system('python register.py')
    
def openmainmenu():
    login.destroy()
    os.system('python mainmenu.py')    
    
 #Deletes all the characters stored in the username entry field when a user hovers over the username entry field
def on_username(e):
    usernameentry.delete(0, 'end')
#Deletes all the characters stored in the password field entry when a user hovers over the password entry field
def on_password(e):
    passwordentry.delete(0, 'end')    


def validate_logindetails():
   global outputdata
   global username
   #Retrieves the data a user has inputted in the usernameentry field using a getter method.
   username = usernameentry.get()
   #Retrieves the data a user has inputted in the passwordentry field using a getter method.
   password = passwordentry.get()
   passwordkey = hashlib.sha1(password.encode())
   passwordhash = passwordkey.hexdigest()
   #Initialises the values of username and password
   if username == 'Username':
       username = ''
   if password == 'Password':
       password = ''
   
   if username == '':
       messagebox.showerror("Login Error!", "Username field is empty!")
   if password == '':
       messagebox.showerror("Login Error!", "Password field is empty!")
   
   #Searches for the value of the username a user has inputted from the AccountDetails csv file.
   with open('AccountDetails.csv', 'rt') as f:
   #Defines a csv file reader 
       usernamesearch = csv.reader(f,delimiter =',')
       #Searches through each row of the AccountDetails csv file
       for row in usernamesearch:
   #Searches for the the value of the username in the first row because that is where the usernames are written.
           if username == row[0]:
  #Used to validate whether a username is stored in the Accountdetails csv file
              usernamevalidation = "True"
           else:
               usernamevalidation = "False"
              
   
    #Searches for the value of the hash for the password a user has inputted from the AccountDetails csv file.
   with open('AccountDetails.csv', 'rt') as f:
       passwordsearch = csv.reader(f,delimiter =',')
       for row in passwordsearch:
           if passwordhash == row[1]:
    #Searches for values in the second column where the passwordhashes are stored on the Account details database.
              passwordvalidation = "True"
           else:
               passwordvalidation = "False" 
            
               

                           
  #Checks if both the password and the username a user has inputted is stored in the Accountdetails csv file. 
   if passwordvalidation == "True" and usernamevalidation == "True":
       messagebox.showinfo("Login Successful!", "Welcome back to mémo!")
       save_username()
       
       openmainmenu()
   else:
       messagebox.showerror("Login Error!", "Either your password or username is incorrect!")
 
  
              
  
              
           
                   
#Creates a user entry field to store the username value  a user has inputted
usernameentry = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei Ui Light',11))
usernameentry.place(x=30,y=80)
usernameentry.insert(0,'Username')
usernameentry.bind('<FocusIn>', on_username)

#Frame used to store the header
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#Creates a password entry field to store the password value a user has inputted
passwordentry = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei Ui Light',11),show='*')
passwordentry.place(x=30,y=150)
passwordentry.insert(0,'Password')
passwordentry.bind('<FocusIn>', on_password)

#Creates a frame used to contain the passwordentry field
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#Creates a button that will allow users to register an account
Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0, command= validate_logindetails).place(x=35,y=204)
label =Label(frame,text="Don't have an account?",fg='black', bg='white',font=('Microsoft Yahei UI Light',9))
label.place(x=75,y=270)

signup = Button(frame,width=7,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup)
signup.place(x=215,y=270)

login.mainloop()