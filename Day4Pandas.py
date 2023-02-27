# Databricks notebook source
import pandas as pd

# COMMAND ----------

df = pd.DataFrame({ #creates a table that shows a, b & c in colums and the numbers matching the letter underneath
    'a' : [1,2,3],
    'b' : [4,5,6],
    'c' : [7,8,9],
}, index = [1,2,3])
print(df)

df2 = pd.DataFrame( # creates a table that shows a, b & c in colums and numbers matching the letter underneath but in a different format
    [[1,2,3],[4,5,6],[7,8,9]],
    index=[1,2,3],
    columns = ['a', 'b', 'c'])
print(df2)

# COMMAND ----------

#This example reads a .csv file and describes the data on it so it is easier to read
tipsData = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

print(tipsData.describe())
print("space")
print(tipsData.isnull().sum())

# COMMAND ----------

tipsData.groupby(['day']).count() #find out how many are on each day as  a count

# COMMAND ----------

tipsData.groupby(['day']).sum() #find out the sum on each day

# COMMAND ----------

totaltip = tipsData.groupby(['day']).sum()['tip'] #filters out to show the tips per day
totalbill = tipsData.groupby(['day']).sum()['total_bill'] #filters out to show the total_bill per day

print(totaltip, totalbill)

# COMMAND ----------

totaltip = tipsData.groupby(['day']).sum()['tip']
totalbill = tipsData.groupby(['day']).sum()['total_bill']

tipdaypercentage = (100 * totaltip / totalbill) #Tuens to tips to a percentage of the total_bill
tipdaypercentage = tipdaypercentage.to_frame('tip(%)').reset_index()

print(tipdaypercentage)

# COMMAND ----------

#Data Frame with integers

pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}) # creates the below based off yes and no being column headers and the values, being put in the columns and rows

# COMMAND ----------

#Date Frame with strings and additing row titles

pd.DataFrame({'Jack':['I loved it', 'It was meh'], 
              'Dave':['It was amazing', 'I hated it']},
              index=['Product A', 'Product B'])

# COMMAND ----------

#Series

print(pd.Series([1,2,3,4,5]))

# COMMAND ----------

#Series with assigned row labels

print(pd.Series ([60,120,180], index=['2018 Sales', '2019 Sales', '2020 Sales'], name = 'Product A'))

# COMMAND ----------

#iloc where its asking for colum 2, row 3

df = pd.DataFrame({ 
          #0,1,2
    'a' : [1,2,3], #0
    'b' : [4,5,6], #1
    'c' : [7,8,9], #2
}, index = [1,2,3])
print(df.iloc[1,2])

# COMMAND ----------

#loc where it is asking for everything in row 'a'

df = pd.DataFrame({ 
          #0,1,2
    'a' : [1,2,3], #0
    'b' : [4,5,6], #1
    'c' : [7,8,9], #2
}, index = [1,2,3])
print(df.loc[:, 'a'])

# COMMAND ----------

#loc where it is asking for everything in column 1
df = pd.DataFrame({ 
          #0,1,2
    'a' : [1,2,3], #0
    'b' : [4,5,6], #1
    'c' : [7,8,9], #2
}, index = [1,2,3])
print(df.loc[1, :])

# COMMAND ----------


