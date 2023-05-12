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
import sklearn as sk



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

# to work with each species type separately
# split the three species within the df 
#variable created for eachtype
# code adapted from [9] 


setosa=df[df['Species']=='Iris-setosa']
versicolor=df[df['Species']=='Iris-versicolor']
virginica=df[df['Species']=='Iris-virginica']


# compute satistical summary for each species type 
#variable will be in string format
setosa = str(setosa.describe())
versicolor = str(versicolor.describe())
virginica = str(virginica.describe())


# write the variable *(stats for each species) a file iris_species.txt 
with open('iris_species.txt', 'w') as f: # automatically closes
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



#Correlation between variables. Code from [13]

print(df.corr(method='pearson'))


###



#Multivariate Analysis: code from [15]
#I tried to create a pair plot with the following code
# each time I ran the code it went into a loop 
# and I had to ctl + C to abort in the terminal
#Couldn't figure out what was wrong

#sns.pairplot (df, hue = 'Species')

#plt.show()
#plt.close()
 

#Linear Regression model
seaborn.regplot code taken from [16,17]


#plot the regplot, pass x ans y variables as strings, line-kws ( pass arhuments for line in Dict
# colour, transparancy, with of line)

# From the correlation coeffient 
# plot the variables that showed the strong positive correltion petal length and width 
sns.regplot(x=df["Petal_Length"], y=df["Petal_Width"], line_kws={"color":"green","alpha":0.7,"lw":5})
plt.show()#
plt.savefig(regplot_petal)
#plot the variables that showed the least correlation correltion petal length and width 
sns.regplot(x=df["Sepal_Width"], y=df["Sepal_Length"], line_kws={"color":"red","alpha":0.7,"lw":5})

plt.show()



# box plots code from [19] 
# combining x and y arguments to plot multiple box  of petal length by species

fig, ax = plt.subplots(1, figsize=(10, 10)) # change size of plot 
sns.boxplot(data=df, x="Species", y = "Petal_Length" )
plt.show()




# combining x and y arguments to plot multiple box  of sepa; length by species

fig, ax = plt.subplots(1, figsize=(10, 10)) # change size of plot 
sns.boxplot(data=df, x="Species", y = "Sepal_Length" )
plt.show()


#plt.close()

# MACHINE LEARNING code adapted from [20] using Sklearn
#Supervised  machine learning


# Import necessary libraries

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#Code adapted from [20, 21]

# Split the data into training and testing sets, 
# # i.e. 70 % training dataset and 30 % test datasets test-size 0.3
X_train, X_test, y_train, y_test = train_test_split(df.drop('Species', axis=1), df['Species'], test_size=0.3, random_state=42)

# Create a random forest classifier model
rfc = RandomForestClassifier()

# # Training the model on the training dataset
# fit function is used to train the model using the training sets as parameters
rfc.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = rfc.predict(X_test)

# Evaluate the model's accuracy 
accuracy = accuracy_score(y_test, y_pred)
# output to 2 decimal places and muliple by 100 for %
print("Accuracy: {:.2f}%".format(accuracy*100))




 
