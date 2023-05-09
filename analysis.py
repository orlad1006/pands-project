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


filename = 'iris_dataset.data'

col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']

df =  pd.read_csv(filename, names = col_names) 

#df = dataframe
# this will read the data in csv format, and pass in column names as an argument

# use the df.head() and df.tail() function to see first and last 5 row
#print to output

#print(df.head())
#print(df.tail())
#print(df.dtypes)
# summary of variables 
#with open('iris.txt', 'w') as f:
#     # Opens files without having to use the close() function, write mode
   # f.write(df.describe().to_string())  # Converts summary data to a string and writes it to a .txt file

#print(df.describe)

#with open('iris_species.txt', 'w') as f:
    #f.write(df.value_counts("Species").to_string())  # how may species and coount of eac, write to .txt file

# separated the three species within the df 
'''
setosa=df[df['Species']=='Iris-setosa']
versicolor=df[df['Species']=='Iris-versicolor']
virginica=df[df['Species']=='Iris-virginica']


# compute satistical summary for each species type 
#variable will be in string format
setosa = str(setosa.describe())
versicolor = str(versicolor.describe())
virginica = str(virginica.describe())


# write the variable *(stats for each species) a file iris_species.txt 
with open('iris_species.txt', 'w') as f:
    f.write("\n SETOSA DETAILS \n") # heading one new line
    f.write(setosa)
    f.write("\n VERSICOLOR DETAILS\n") # heading one new line
    f.write(versicolor)
    f.write("\n VIRGINICA DETAILS\n") # heading one new line
    f.write(virginica)



# Histogram for each variable - all data together, not species specific
# code taken from [7] for histogram


# 1st sepal lenght

plt.figure(figsize = (10, 7)) # change width and height of figure
x = df["Sepal_Length"]

plt.hist(x, bins = 20, color = "green")
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_cm")
plt.ylabel("Count")

plt.savefig("Hist Sepal length.png")


# 2nd Sepal width 

plt.figure(figsize = (10, 7)) # change width and height of figure
x = df["Sepal_Width"]

plt.hist(x, bins = 20, color = "blue")
plt.title("Sepal Width in cm")
plt.xlabel("Sepal_Width_cm")
plt.ylabel("Count")

plt.savefig("Hist Sepal width.png")


# 3rd Petal Lenght

plt.figure(figsize = (10, 7)) # change width and height of figure
x = df["Petal_Length"]

plt.hist(x, bins = 20, color = "red")
plt.title("Petal Length in cm")
plt.xlabel("Petal_Length_cm")
plt.ylabel("Count")

plt.savefig("Hist Petal Length.png")


# 4th Petal Width 

plt.figure(figsize = (10, 7)) # change width and height of figure
x = df["Petal_Width"]

plt.hist(x, bins = 20, color = "yellow")
plt.title("Petal Width in cm")
plt.xlabel("Petal_Width_cm")
plt.ylabel("Count")

plt.savefig("Hist Petal Width.png")




#5th species 

plt.figure(figsize = (10, 7)) # change width and height of figure
x = df["Species"]

plt.hist(x, bins = 10, color = "orange")
plt.title("Species of Iris")
plt.xlabel("Species")
plt.ylabel("Count")

plt.savefig("Hist Species.png")

plt.show()


# Scatter plot of each pair of variable using Seaborn Package - Code taken from [10,11]

# pair : Sepal lenght vd width 
# pair : Petal Lenght vs Width


sns.scatterplot(data=df, x='Sepal_Length', y='Sepal_Width', hue='Species', legend = 'auto')# differentiate between the three species in each scatter plot by colour/hue. Could also use
#size and style of dot, legend placed in automatic best location
plt.savefig("Scatterbox_Sepal.png")

'''
sns.scatterplot(data=df, x='Petal_Length', y='Petal_Width', hue='Species', legend ='auto') # differentiate between the three species in each scatter plot by colour/hue. Could also use
#size and style of dot.
plt.savefig("Scatterbox_Petal.png")








