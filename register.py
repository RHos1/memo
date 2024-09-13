# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 17:55:55 2022

@author: recha
"""
import hashlib

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import pandas as pd
import os

def on_enter(e):
    #Deletes all the characters stored in the username entry field starting from the first character
    usernameentry.delete(0,'end')



register = tk.Tk()
register.title('mémo - Register')
icon = tk.PhotoImage(file = r'C:\Users\recha\Desktop\mémo\PythonComponents\Logo2.png')
register.tk.call('wm','iconphoto', register._w,icon)
#Sets the resolution of the register root window
register.geometry('925x500+300+200')
#Sets the background colour of the register root window
register.configure(bg='#fff')
#Prevents users from resizing the resolution of the root window
register.resizable(False,False)
#Stores an image file under the identifier image1 using the photoimage method
image1 = tk.PhotoImage(file='SignUp1.png')
Label(register,image=image1,border=0,bg='white').place(x=50,y=90)

frame=Frame(register,width=350,height=390,bg='#fff')
frame.place(x=480,y=50)

#Displays Header for the sign up login interface
heading=Label(frame,text='Sign up',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)

#Entry field used for a user to input a username to register for their account
usernameentry = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
usernameentry.place(x=30,y=80)
#When the register menu is run, the string 'Username' will be stored in the userentry field
usernameentry.insert(0, 'Username')
#When a user hovers or clicks on the username field,the instructions in the on_enter method will be executed.
usernameentry.bind("<FocusIn>",on_enter)



Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


def Login():
    register.destroy()
    os.system('python login.py')
    
    
#The method validate_details will retrieve the values users have inputted in each user entry field using getter methods. 
def validate_details():
    username = usernameentry.get()
    print(username)
    #Returns the value inputted in the usernameentry input field and stores it under the identifier username
    password = passwordentry.get()
    #Returns the value inputted in the password input field and stores it under the identifier password 
    passwordkey = hashlib.sha1(password.encode())
    confirmpassword = confirmpasswordentry.get()
    passwordhash = passwordkey.hexdigest()
    #Converts the password value to a hash value by using the 'sha1' hashlib algorithm
    
    
    
    #Initialises the value of the username and the password identifiers 
    if username == "Username":
       username = ""   
    if password == 'Password': 
       password = ""  
    if confirmpassword == 'Confirm Password':
       confirmpassword = ""
    
    #Stores the length of the password and the username a user has inputted 
    passwordlength = len(password)
    usernamelength = len(username)
    
    
    
    #Checks if the username entry field is empty
    if username == "":   
        messagebox.showerror(title='Sign Up Error', message="Username field is empty!")
        usernamecheck = "False"
   #Checks if the username length is not in the specified range
    elif usernamelength < 5 or usernamelength > 21 :
         messagebox.showerror(title='Username is incorrect length', message="The Username has to be between 5 and 21 characters!") 
         usernamevalid = "False"
   #Checks if the username length is in the specified range
    elif usernamelength > 5 or usernamelength < 21:
         usernamevalid = "True"
   #Checks if the password entry field is empty 
    if password == "":
        messagebox.showerror(title='Sign Up Error', message="Password field is empty!")
        passwordvalid = "False"
      #Checks if the password length is in the specified range
    elif passwordlength < 5 or passwordlength > 21  :
        messagebox.showerror(title='Password is incorrect length', message="The password has to be between 5 and 21 characters!")   
        passwordvalid = "False"
    else:
        passwordvalid = "True"
    
    #Checks if the user's password value matches with their second password value 
    if confirmpassword != passwordvalue :
        messagebox.showerror(title='Sign Up Error', message="The passwords do not match!")
        passwordmatch = "False"
    else:
        passwordmatch = "True"    
    
   
    #Checks if the the password, username and passwordmatch values are true to allow a user to create an account    
    if passwordvalid == "True" and usernamevalid == "True" and passwordmatch == "True":
   #Outputs a messagebox congratulating the user for successfully registering their account.    
        messagebox.showinfo(title='Account Registered Successfully!', message="Welcome to mémo")
   #Defines a Dataframe userdatabase that stores the username and passwordhash of the user's registered details  
        userdatabase = pd.DataFrame([[username , password]], columns = ['Username', 'Password'])
   #Appends the contents of the userdatabase frame to the csv file 'AccountDetails'
        userdatabase.to_csv('AccountDetails.csv',mode='a', index=False, header=False)
    
            



                           
    
        
        
        
    
     
   
        
def on_enter(e):
    passwordentry.delete(0,'end')

# Creates an entry field used to allow a user to register their password
passwordentry = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11),show='*') 
#Hides the password entry value by converting the string values to asterisks

passwordentry.place(x=30,y=150)
passwordentry.insert(0, 'Password')
passwordentry.bind("<FocusIn>",on_enter)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


def on_enter(e):
    confirmpasswordentry.delete(0,'end')

# Creates a entry field used to verify a user's password.
confirmpasswordentry = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11),show='*')
#Hides the confirm password entry value by converting the string values to asterisks
confirmpasswordentry.place(x=30,y=220)
confirmpasswordentry.insert(0, 'Password')
confirmpasswordentry.bind("<FocusIn>",on_enter)



Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)


#Creates the register and Login Button used to allow users to either login or register a new account
registerbutton = Button(frame,width=39, pady=7, text='Sign up',bg='#57a1f8', fg='white',border=0 , command= validate_details).place(x=35,y=280)
loginbutton = Button(frame,width=7, text='Login',border=0,bg='white',cursor='hand2',fg='#57a1f8', command=Login)
loginbutton.place(x=180,y=320)
label = Label(frame,text="Already have an account?", fg='black',bg='white',font=('Microsoft Yahei Ui Light',9))
label.place(x=30, y=320)





      



































register.mainloop()