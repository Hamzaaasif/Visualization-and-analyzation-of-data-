import pandas as pd 
import numpy as np  
import matplotlib.pyplot as plt 
import seaborn as sns 

#***************PHASE-I*************#
#*********Data Collection And Pre-processing*******#

UsedCarData=pd.read_csv('OLX_Car_Data_CSV.csv',delimiter=',',encoding="ISO-8859-1")#Reading data from CSV file 
print(UsedCarData.head()) #Used to print 5 data rows
print(UsedCarData.describe()) #describe() method returns many mathematical operations
print(UsedCarData.loc[:,('Brand','Year')]) #loc() methods selected rows
print(UsedCarData['Brand'].value_counts())
print(UsedCarData.columns)  #Return column names
print(UsedCarData.dtypes) #types of columns ie int , float , object etc
print(UsedCarData.info) 

missing_data = UsedCarData.isnull() #checking for Null values bool type 
print(missing_data.head(10)) 
for column in missing_data.columns.values.tolist(): #print the total count of null (True)and not null(False) 
  print(column," :")                                 #values
  print(missing_data[column].value_counts())
  print(" ")

avg_year = UsedCarData["Year"].astype("float").mean(axis=0)    #Returns the mean(avg) of the column   
print("Avg Of Year",avg_year)                               #"Year"
UsedCarData["Year"].replace(np.nan,avg_year,inplace=True) #Replace Null values with avg Year  
avg_kms_driven = UsedCarData["KMs Driven"].astype("float").mean(axis=0) #Returns the mean(avg) of the column   
print("Avg Of Kms Driven",avg_kms_driven)                               #"KMs Driven"
UsedCarData["KMs Driven"].replace(np.nan,avg_kms_driven,inplace=True) #Replace Null values with avg km driven  
UsedCarData.dropna(subset={"Brand","Condition","Fuel","Model","Registered City","Transaction Type"},axis=0,inplace=True)#Delete the NUll data 
UsedCarData.reset_index(drop=True,inplace=True) #Reset index
UsedCarData.replace("",np.nan,inplace=True)
print(UsedCarData)

#***************PHASE-II*************#
#***Grpah Brand Vs Price****
print(UsedCarData['Fuel'].value_counts())
print(UsedCarData['Registered City'].value_counts())
#****Graph Condition Vs Price***
fig=plt.figure()
sns.barplot(x='Condition',y='Price',hue="Condition",data=UsedCarData.loc[:,('Condition','Price')])
#****Graph Fuel Vs Price***
sns.relplot(x='Fuel',y='Price',kind="line",data=UsedCarData.loc[:,('Fuel','Price')])
#****Graph Year Vs Price***
sns.relplot(x='Year',y='Price',kind="line",data=UsedCarData.loc[:,('Year','Price')])
#****Graph Condition Vs Year***
var=UsedCarData.groupby('Condition').Year.sum()
fig=plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Condition')
ax1.set_ylabel('Year')
ax1.set_title("Condition Vs Year")
var.plot(kind='bar')
fig=plt.figure()
#****Graph Brand Vs Price***
g=sns.barplot(x='Brand',y='Price',data=UsedCarData.loc[:,('Brand','Price')])
for item in g.get_xticklabels(): item.set_rotation(90)
plt.show()