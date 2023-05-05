# Title: Project for Programming and Scripting
# Author: Orla Dowling


#This python file is to perform analysis on the Iris Data set
# Andrew should be able to run this code 

# First I am going to import the programs that will help me anaylse
# the data set 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# to download the data set and add to my git hub respository

filename = 'IrisDataSet.txt'    # df stands for dataframe
df = pd.read_csv(filename)      # this will read the data in csv format from the .txt 


# we will then base all of our analysis from this table.

