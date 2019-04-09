import pandas as pd #1st step :pip install pandas 
import numpy as np  #pip install numpy
import matplotlib.pyplot as plt #pip install matplotlib
import seaborn as sns #pip install seaborn
#import os
#%matplotlib inline
#***************PHASE-I*************#
#*********Data Collection And Pre-processing*******#

UsedCarData=pd.read_csv('OLX_Car_Data_CSV.csv',delimiter=',',encoding="ISO-8859-1")#Reading data from CSV file 
#print(UsedCarData.head()) #Used to print 5 data rows
#print(UsedCarData.describe(include="all")) #describe() method returns many mathematical operations
#print(UsedCarData.loc[:,('Brand','Year')]) #loc() methods selected rows
#print(UsedCarData.columns)  #Return column names
#print(UsedCarData.dtypes) #types of columns ie int , float , object etc
#print(UsedCarData.info) 

missing_data = UsedCarData.isnull() #checking for Null values bool type 
#print(missing_data.head(10)) 
#for column in missing_data.columns.values.tolist(): #print the total count of null (True)and not null(False) 
 # print(column," :")                                 #values
  #print(missing_data[column].value_counts())
  #print(" ")

avg_year = UsedCarData["Year"].astype("float").mean(axis=0)    #Returns the mean(avg) of the column   
#print("Avg Of Kms Driven",avg_year)                               #"Year"
UsedCarData["Year"].replace(np.nan,avg_year,inplace=True) #Replace Null values with avg Year                                                                                in the column

avg_kms_driven = UsedCarData["KMs Driven"].astype("float").mean(axis=0) #Returns the mean(avg) of the column   
#print("Avg Of Kms Driven",avg_kms_driven)                               #"KMs Driven"
UsedCarData["KMs Driven"].replace(np.nan,avg_kms_driven,inplace=True) #Replace Null values with avg km driven                                                                                in the column

UsedCarData.dropna(subset={"Brand","Condition","Fuel","Model","Registered City","Transaction Type"},axis=0,inplace=True)#Delete the NUll data 
UsedCarData.reset_index(drop=True,inplace=True) #Reset index
UsedCarData.replace("",np.nan,inplace=True)
#print(UsedCarData)

#***************PHASE-II*************#
#*********Visualization and Data Analysis**********#
print(UsedCarData['Fuel'].value_counts())
brand=UsedCarData.groupby('Brand').Price.sum()
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
ax1.set_xlabel('Brand')
ax1.set_ylabel('Increase in Price')
ax1.set_title("Brand Vs Price")
brand.plot(kind='bar')

cond=UsedCarData.groupby('Condition').Price.sum()
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
ax1.set_title("Condition Vs Price")
cond.plot(kind='pie')


#var=UsedCarData.groupby('Model').Price.sum()
#fig=plt.figure()
#ax1 = fig.add_subplot(1,1,1)
#ax1.set_xlabel('Model')
#ax1.set_ylabel('Price')
#ax1.set_title("Model Vs Price")
#var.plot(kind='line')

#print(UsedCarData['Condition'].value_counts())
#var=UsedCarData.groupby('Condition').Year.sum()
#fig=plt.figure()
#ax1 = fig.add_subplot(1,1,1)
#ax1.set_xlabel('Condition')
#ax1.set_ylabel('Year')
#ax1.set_title("Condition Vs Year")
#var.plot(kind='bar')UsedCarData.loc[:,('Brand','Year')]

sns.relplot(x='Year',y='Price',kind="line",data=UsedCarData.loc[:,('Year','Price')])
plt.show()