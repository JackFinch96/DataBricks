# Databricks notebook source
import numpy as np

# COMMAND ----------

my1darray = np.array([1,2,3])
print(my1darray)

my2darray = np.array([[1,2,3], [4,5,6]])
print(my2darray)

charArray1 = np.array([(1, 'a', 3.),(4,5,'zzz')], dtype='U21')
print(charArray1)

# COMMAND ----------

rows = 4
cols = 3
array1s = np.ones((rows, cols))
arrays5 = 5 * np.ones((rows,cols)) #turns array to number defined
arrays7 = np.full((rows,cols), 7) #turns array to number defined
print(arrays7)
print(arrays5)

# COMMAND ----------

samples = 5
step = 3
start = 10
stop = 25

np.arange(start, stop, step)
np.linspace(start, stop, samples)
np.eye(3)
np.random.random((2,3))
np.random.randint(0,10, (3,3))

# COMMAND ----------

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
a.ndim #dimension
a.shape #shape
a.size #size of data
a.dtype #data type
a[0, 1] #get me row zero, column1
a[1:] #give me everything from row 1 onwards
a[0:2, 1] #give me everything row 1-3, column 1
a[a < 9] # give me everything less than 9
np.diag(a) #gives diagonal results

# COMMAND ----------

a = np.array([[1,2], [4,5]])
b = np.array([[9,8] ,[6,5]])
summ1 = a.sum() #take array and give sum
summ2 = np.sum(a) #sum from  numpy directly

a + b  #addition of a+b
np.add(a, b) #another way of addition of a+b
a - b #subtraction of a-b
a * b #multiplication of a * b
a / b #division of a / b
np.exp(a) 
np.sqrt(a)
np.sin(a)
np.cos(a)
np.log(a)
display(a.dot(b))


# COMMAND ----------

# (0,3)
# |\
# | \
# |  \
# |___\(1.5, 0)
# (0,0)
A = np.array([0,0])
B = np.array([0,3])
C = np.array([1.5,0])

# A^2 + B^2 = C^2
# AB^2 = (ax - bx)^2 +(ay - ay)^2

BC = np.sqrt(AB**2 + AC**2)
from numpy import linalg as la
AB2 = la.norm(A-B)
AC2 = la.norm(A-C)
BC2 = la.norm(B-C)
print(BC2, BC)

# COMMAND ----------

import numpy as np
#import pyspark as ps

#use spark to read the txt file as a csv
dataRaw = spark.read.csv(path = "dbfs:/FileStore/IrisData/iris_head_num.txt")

# collect all the datda and store it in a np array
dataRaw = np.array(dataRaw.select("*").collect())

#seperate data from headers
header = dataRaw[0,:]
#select all rows except the firts, all columns except the 4th
data = dataRaw[1:, :4]
# convert data from string to float32
data = np.vstack(data.astype(np.float32))
#select the labels column
labels = np.vstack(dataRaw[1:,4].astype(np.int32))
#make an array of unique labels, and the number of labels total
labelsUn, labelsCount = np.unique(labels, return_counts = 1)
#this shows we have 3 different flowers un out dataset, with 50 samples each
display(labelsUn, labelsCount)

# COMMAND ----------

#find average, max, min, and standard deviation of each column per catagory

#number of rows (observations) and colums (attributes or features) of our data
nrows,ncols = np.shape(data) # > 150,4
#numbers of unique catagories
nclasses = len(labelsUn) # > 3
#initialise empty dfs into which we will update our statistics
average = np.zeros((nclasses,ncols))
maxi = np.zeros((nclasses,ncols))
mini = np.zeros((nclasses,ncols))
sd = np.zeros((nclasses,ncols))

for i in labelsUn: # > [1,2,3]
    #select indices of where in df matches current label
    indexes = np.reshape(labels==i,nrows)
    #push into empty arrays the calculated mean, min, max and standard deviation
    average[i-1,:] = np.mean(data[indexes,:], axis=0)
    maxi[i-1,:] = np.max(data[indexes,:], axis=0)
    mini[i-1,:] = np.min(data[indexes,:], axis=0)
    sd[i-1,:] = np.std(data[indexes,:], axis=0)
print(header)
print("averages")
print(average)
print("Maximum")
print(maxi)
print("Minimum")
print(mini)
print("Standard Deviation")
print(sd)
                                  
                                  


# COMMAND ----------

#make empty array to store outliers
outliers2sd = np.zeros((nclasses,ncols))
for i in labelsUn:
    #find indexes again
    indexes = np.reshape(labels==i,nrows)
    #select the data that matches the class
    classData = data[indexes,:]
    #for each column in this data
    for j in range(ncols):
        #find threasholds, high and low
        threasholdlow = average[i-1,j]-2*sd[i-1,j]
        threasholdhigh = average[i-2,j]+2*sd[i-1,j]
        #any data above or below
        remain = [x for x in classData[:,j] if(x > threasholdlow)]
        remain = [x for x in classData[:,j] if(x > threasholdhigh)]
        #calculate percentage of outliners
        outliers2sd[i-1,j] = 100 * (labelsCount[i-1] - len(remain)) / labelsCount[i-1]
        
print(header)
print(outliers2sd)
        


# COMMAND ----------

print(header)
print("averages")
print(average)
print("Maximum")
print(maxi)
print("Minimum")
print(mini)
print("Standard Deviation")
print(sd)
print("Outliers Percentage")
print(outliers2sd)

# COMMAND ----------

#Export to spark.csv file
#some variables for formatiing
decimals = 2
fmt = "%.2f"
fortmatf = ".csv"
import pandas as pd

#Our data is in all sorts of shapes now after collecting it
#Well put it together, format it and export it
species = np.array(['setosa','versicolor','viginica'])
#for each of the flowers in our df
for i in range(len(labelsUn)):
    #stack the statistics generates
    temp = np.vstack( [average[i,:], mini[i,:], maxi[i,:], sd[i,:], outliers2sd[i,:]]).T
                       
    #round the decimals to the nearest 2 places
    temp = np.around(temp,decimals)
    
    #cast numbers to string and format
    temp_str = np.char.mod(fmt, temp)
    #take header row and transpose it to be a column
    rows = np.array(header[:-1].astype("U"))[:, np.newaxis]
                       
    #put header column next to data
    rowsf = np.hstack((rows, temp_str))
    #make beauty header row for the csv
    headerf = [species[i],'mean','min','max','std','outliers2sd%']
    #cast to a pandas dataframe, to then be cast to spark dataframe
    pdDf = pd.DataFrame(rowsf, columns = [headerf])
    
    #cast to spark dataframe
    sparkDf= spark.createDataFrame(pdDf)
    #try to write out 4 csvs
    try: 
        sparkDF.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("dbfs:/FileStore/tables/irisTest/" + str(species[i]))
    except:
        #unless file already exists
        print("File already exists")
    
    #Read back file to make sure everything works
    display(spark.read.csv("dbfs:/FileStore/tables/irisTest/" + str(species[i])))

# COMMAND ----------


