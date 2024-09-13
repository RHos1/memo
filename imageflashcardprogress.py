# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 09:32:17 2023

@author: recha
"""

import pandas as pd 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Creates a csv file reader that reads the data from the Accountdetails csv file
csvreader = pd.read_csv('Logins.csv')
#Converts the data from the Accountdetails csv file into a dataframe
dataframe = pd.DataFrame(csvreader)
#Retrieves the value of the last username that is stored in the Accountdetails csv file
currentuser = dataframe['Username'].iloc[-1]

#Creates a csvfile reader 
csvfile = pd.read_csv('imageflashcardprogress.csv')
dataframe = pd.DataFrame(csvfile)
#Reads the data from the specificied csv file and converts it to a dataframe that can be read from efficiently.
easy = dataframe['Easy'].iloc[-1]
medium = dataframe['Medium'].iloc[-1]
difficult = dataframe['Difficult'].iloc[-1]
#assigns the value of each identifier as the value stored in the last row under each column.

#Data that will be outputted when generating a bar chart using matplotlib
Difficulty = np.array(['Easy','Medium','Difficult'])
Numbers = np.array([easy,medium,difficult])

#Assigns the header names of the x and y axis and the title 
plt.xlabel('Difficulty Level')
plt.ylabel('Number of Flashcards')
#Displays the current user's username on the bar chart title 
plt.title(currentuser +"'s" + " progress")
plt.bar(Difficulty,Numbers)