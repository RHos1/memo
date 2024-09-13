# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 21:01:39 2023

@author: recha
"""
import tkinter as tk
from tkinter import *
import pandas as pd 
import matplotlib
import matplotlib.pyplot as plt

import numpy as np

#Converts the data from the Logins csv file into a dataframe
userdata = pd.read_csv('Logins.csv')
dataframe = pd.DataFrame(userdata)
#The currentuser idenfifier stores the most recent username entry in the Accountdetails csv file
currentuser = dataframe['Username'].iloc[-1]



csvfilereader = pd.read_csv('userprogress.csv')
#Converts the data stored in the userprogress csv file to a dataframe to allow for more efficient data searching.
dataframe = pd.DataFrame(csvfilereader)
#Reads the cell from the last row of the Easy column
easy = dataframe['Easy'].iloc[-1]
medium = dataframe['Medium'].iloc[-1]
difficult = dataframe['Difficult'].iloc[-1]
#Reads the data from the last row

#Stores the number of easy,medium, and difficult flashcards using a numpy array
difficulty_levels = np.array(['Easy','Medium','Difficult'])
numbers = np.array([easy,medium,difficult])

plt.xlabel('Difficulty Level')
plt.ylabel('Number Of Flashcards')
#Displays the current user's username as the title of the graph
plt.title(currentuser+"'s" + " progress")
#Plots a bar with the column names and the number of each flashcard difficulty level
plt.bar(difficulty_levels,numbers)






