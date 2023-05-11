import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# I opened the data set from http://archive.ics.uci.edu/ml/datasets/Iris repository using VS code
#I created a file called in my pands project folder called iris 


filename = 'iris_dataset.data'

col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']

df =  pd.read_csv(filename, names = col_names) 


sns.pairplot (df, hue='Species')

plt.show()