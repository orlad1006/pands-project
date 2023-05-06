# **PANDS PROJECT 2023**  


## **TABLES OF CONTENTS**  


  - [Project Brief](#project-brief)
  - [Iris Data Set Summary](#iris-data-set-iris-summary)
  - [Python](#python)
  - [Data Analysis](#data-analysis)
    - [Applications Used](#applications-used)
    - [Libraries Used](#libraries-used)
    - [Dataset Download and Import](#dataset-download-and-import)
    - [Summary of each variable](#summary-of-each-variable)
    - [Histogram of each variable type](#histogram-of-each-variable-type)
    - [Scatterplots of each Pair of Variables](#scatterplots-of-each-pair-of-variables)
  - [Further Analysis](#further-analysis)
    - [Unsupervised Learning](#unsupervised-learning)
    - [Application of knowledge into practice](#application-of-knowledge-into-practice)
  - [Conclusion](#conclusion)
- [References](#references)


## Project Brief:

**Problem statement:**

This project concerns the well-known Fisher’s Iris data set. You must research the data set
and write documentation and code in Python to investigate it.Research the data set online and 

[1] Reseach the data set and write a summary about it in your README.

[2] Download the data set and add it to your repository.

[3] Write a program called analysis.py that:

- outputs a summary of each variable to a single text file
- saves a histogram of each variable to png files
- outputs a scatter plot of each pair of variable
- performs other appropriate analysis  

Note: Imagine that this project is used to explain to work collagues what investigating a data set entails and how python can be use to do it.  


## Summary of Fisher's Iris Data Set.

![Alt text](iris.image.png)

A data set is any organised collection of data. The data set lists values for each of the variables and for each member of the dataset.  

The Fisher Iris Data Set is multivariate dataset . The data set  is the measurement of the length and width of both sepals and petals of three different species of the Iris flower (Setosa, Versicolor and Virginica) . In total there are 150 measurements. These measures were used to create a linear discriminate model to classify the species [1]. 

It is one of the most widely used data sets for mining data, exploratory data analtyics and testing machine learning alogorithims.  This is for several reasons: 
-   It is a simple and easy to understand  
-   The features of the dataset are well understood
-   The classification of the three species of Iris is well defined ans they can be discrimated between using the measurements of their petals and sepals

This makes it easy to work with in data science, especially for beginners. [2]

 
## PYTHON:  

Python is a popular multipurpose programming language created in 1991. It has many uses, mainly :  

-   web development e.g used on server to create web application 
-   software development e.g. rapid prototyping
-   mathematics e.g. handle big data and perform complex statisical analysis
-   system scripting e.g. write programs, manipulate, customize, and automate the facilities of an existing system

Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc) and has a simple syntax similar to the English language. This synthax allows developers to write write programs with fewer lines than some other programming languages.The code can be executed as soon as it is written as it runs on an interpreter system [4].



## DATA ANALYSIS

### Applications used  

**Anacona3 Python version 3.9.13**
Anaconda is an open source software package distribution of the Python programming language. The distribution includes data-science packages suitable for Windows, Linux, and macOS. I installed anaconda on my Windows machine to use the Python language to create code for this project which was very useful because of the inbuilt data science packages and libraries.  

**VSCODE version 1.78**  

Visual Studio code is a freeware source code editor which runs on your desktop and is available for Windows, macOS and Linux. It comes with built-in support for languages like JavaScript and has a system of extensions for other programming languages like Python. All the code for this project was written using VS Code.

**CMDER version 1.3.21**  

CMDER is an open source command prompt user interface for Windows machines. It is more popular that in built command prompt interfaces as it provides more graphical representtation.  I installed CMDER on my windows machine to clone my repository for the project from git hub and saved it to a folder on my Desktop.


**GITHUB version 3.74**  

GitHub is a website and cloud-based service that helps developers store and manage their code, as well as track and control changes to their code.  I used this application to store my code for this project aslong with the read.me file.  




### Libraries Used  

In VS code I imported the following libraries as tools to help me analyse and visuailse the Iris data set. A brief overview is provided below [5].    

**_Numpy_**  

NumPy is a Python module for numerical computation that can process large amounts of data and perform array computations. It can deal with  multi-dimensional arrays. It provides a wide range of mathematical functions for performing common operations such as addition, subtraction, multiplication, division, and more.


**_Matplotlib_**  

Matbotlib is a visualization package that is used to plot graphs and charts. It is frequently utilized for data analysis due to the charts and histograms that it generates that assist with communication of data. data to a non-technical person. It is useful for exploaratory data anaylysis in helping identift trends in the data. 


**_Pandas_**  

Pandas is a popular data science library processing and manipulating data set. It provides a range of functions for data manipulation, data analysis, and data visualization. 
 

**_Seaborn_**   

It is a  Matplotlib-based package used to make  high level visualizations for displaying statistical data. 


### Dataset Download and Import  

I downloaded the Iris dataset from the data folder on the UCI Machine Learning Respository[5]. The data was downloaded through vs code in csv format then saved in my pands-project folder on my desktop.  

I used the pandas library to import the csv file as a dataframe object.  A pandas DataFrame represents a rectangular table of data containing an ordered collection of columns and each column can have a different value type. The Iris data set contains four numerical columns for the petal and sepal measurements and one categorical column for the class or type of iris.

The pandas *read_csv* function loads delimited data from a file using the comma as the separator and creates a DataFrame object. There are many attributes and methods available that can be used on the dataframe object.  

*read_csv* has different options for specifying the column names to use. If column names are not passed to read_csv, by default it looks to the first row of the data and infers the column names from this row. In the care of iris data set from UCI the column names are not specified in csv format. Therefore I crated a script to name the columnd and passed it in as an argument to the *read_csv*.  

![Alt text](images/import%20dataset.png)





### Summary of each variable  






### Histogram of each variable type  






### Scatterplots of each Pair of Variables  






### Further Analysis  






### Unsupervised Learning  





### Application of knowledge into practice  





### Conclusion


# REFERENCES
[1]“Data Science Example - Iris dataset,” www.lac.inpe.br. http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html#:~:text=The%20Iris%20Dataset%20contains%20four  
[2]panData, “🐼 Unveiling the mysteries of the Iris dataset: A comprehensive analysis and Machine Learning…,” Medium, Mar. 16, 2023. https://levelup.gitconnected.com/unveiling-the-mysteries-of-the-iris-dataset-a-comprehensive-analysis-and-machine-learning-f5c4f9dbcd6d#:~:text=The%20Iris%20dataset%20is%20a%20popular%20dataset%20in%20data%20exploration (accessed May 06, 2023).
‌‌[3]“UCI Machine Learning Repository: Iris Data Set,” Uci.edu, 2019. https://archive.ics.uci.edu/ml/datasets/iris  
[4]w3Schools, “Introduction to Python,” W3schools.com, 2019. https://www.w3schools.com/python/python_intro.asp
‌[5]“Top 10 Python Libraries for Data Science Explained (2023),” FavTutor. https://favtutor.com/blogs/top-python-data-science-library
‌
‌
