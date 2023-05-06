# Title: Project for Programming and Scripting
# Author: Orla Dowling


#This python file is to perform analysis on the Iris Data set
# Andrew should be able to run this code 

# First I am going to import the libraries that will help me anaylse 
# and visualise the data set 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# I opened the data set from http://archive.ics.uci.edu/ml/datasets/Iris repository using VS code
#I created a file called in my pands project folder called iris 


filename = 'iris.txt'

col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']

df =  pd.read_csv(filename, names = col_names) 

#df = dataframe
# this will read the data in csv format, and pass in column names as an argument

# use the df.head() and df.tail() function to see first and last 5 row
#print to output

print(df.head())
print(df.tail())
print(df.dtypes)







# we will then base all of our analysis from this table.

