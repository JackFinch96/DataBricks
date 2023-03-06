# Databricks notebook source
#Create a line graph to show the Company profit per month with titles
import pandas as pd #imports pandas
import matplotlib.pyplot as plt #imports matplotlibs

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv") #reads the saved excel sheet
profitList = df ['total_profit'].tolist() #
monthList  = df ['month_number'].tolist() #assigns the month_number data from the sheet to monthlist
plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
plt.xlabel('Month number') #makes x-axis title say Month number
plt.ylabel('Profit in dollar') #makes y-axis title say Profit in dollar
plt.xticks(monthList) #lists the months in numbers on the x-axis
plt.title('Company profit per month') #gives the line chart a title of Company profit per month
plt.yticks([100000, 200000, 300000, 400000, 500000]) #Creates the y-axis start from 100000, but ends at 500000. Makes the data easier to read
plt.show() #Asks to show the graph that has been created

# COMMAND ----------

#Create a line graph to show the Company profit per month with titles, dashed graph, with markers
import pandas as pd #imports pandas
import matplotlib.pyplot as plt #imports matplotlibs

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv") #reads the saved excel sheet
profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist() #assigns the month_number data from the sheet to monthlist

plt.plot(monthList, profitList, label = 'Profit data of last year', 
      color='r', marker='o', markerfacecolor='k', 
      linestyle='--', linewidth=3)
      
plt.xlabel('Month Number') #makes x-axis title say Month number
plt.ylabel('Profit in dollar') #makes y-axis title say Profit in dollar
plt.legend(loc='lower right') #asks to show the legend and display it at the lower right
plt.title('Company Sales data of last year') #gives the line chart a title of Company sales data of last year
plt.xticks(monthList) #lists the months in numbers on the x-axis
plt.yticks([100000, 200000, 300000, 400000, 500000]) #Creates the y-axis start from 100000, but ends at 500000. Makes the data easier to read
plt.show() #Asks to show the graph that has been created

# COMMAND ----------

#Create multiple line graphs to indicate the data for each product
import pandas as pd #imports pandas
import matplotlib.pyplot as plt   #imports matplotlibs

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv") #reads the saved excel sheet
monthList  = df ['month_number'].tolist() #assigns the month_number data from the sheet to monthlist
faceCremSalesData   = df ['facecream'].tolist()
faceWashSalesData   = df ['facewash'].tolist()
toothPasteSalesData = df ['toothpaste'].tolist()
bathingsoapSalesData   = df ['bathingsoap'].tolist()
shampooSalesData   = df ['shampoo'].tolist()
moisturizerSalesData = df ['moisturizer'].tolist()

plt.plot(monthList, faceCremSalesData,   label = 'Face cream Sales Data', marker='o', linewidth=3)
plt.plot(monthList, faceWashSalesData,   label = 'Face Wash Sales Data',  marker='o', linewidth=3)
plt.plot(monthList, toothPasteSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, bathingsoapSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, shampooSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, moisturizerSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)

plt.xlabel('Month Number') #Puts x-axis label Month NUmber
plt.ylabel('Sales units in number') #Puts y-axis label Sales units in number
plt.legend(loc='upper left') #Creates legend and puts it in the upper left
plt.xticks(monthList) #lists the months in numbers on the x-axis
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000]) #lists values on the y-axis
plt.title('Sales data') #Asks to show title saying Sales Data
plt.show() #Asks to show the graph that has been created

# COMMAND ----------

#Create a scatter graph for tooth paste data
import pandas as pd #imports pandas
import matplotlib.pyplot as plt  #imports matplotlibs

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv") #reads the saved excel sheet
monthList  = df ['month_number'].tolist() #assigns the month_number data from the sheet to monthlist
toothPasteSalesData = df ['toothpaste'].tolist()
plt.scatter(monthList, toothPasteSalesData, label = 'Tooth paste Sales data')
plt.xlabel('Month Number') #Puts x-axis label Month Number
plt.ylabel('Number of units Sold') #Puts y-axis label Number of units Sold
plt.legend(loc='upper left') #Creates legend and puts it in the upper left
plt.title(' Tooth paste Sales data') #Createst title Tooth paste Sales data
plt.xticks(monthList) #lists the months in numbers on the x-axis
plt.grid(True, linewidth= 1, linestyle="--")
plt.show() #Asks to show the graph that has been created

# COMMAND ----------

#create a dual bar chart for face cream and face wash sales data
import pandas as pd #imports pandas
import matplotlib.pyplot as plt #imports matplotlibs

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv") #reads the saved excel sheet
monthList  = df ['month_number'].tolist() #assigns the month_number data from the sheet to monthlist
faceCremSalesData   = df ['facecream'].tolist() #assigns the facecream data from the sheet to faceCremSalesData
faceWashSalesData   = df ['facewash'].tolist() #assigns the facewash data from the sheet to faceWashSalesData

plt.bar([a-0.25 for a in monthList], faceCremSalesData, width= 0.25, label = 'Face Cream sales data', align='edge') #creates the face cream sales data
plt.bar([a+0.25 for a in monthList], faceWashSalesData, width= -0.25, label = 'Face Wash sales data', align='edge') #creates the face wash sales data
plt.xlabel('Month Number') #Puts x-axis label Month Number
plt.ylabel('Sales units in number') #Puts y-axis label Sales units in number
plt.legend(loc='upper left') #creates legend and locates it in the upper left
plt.title(' Sales data') #creates title of Sales data

plt.xticks(monthList) #lists the months in numbers on the x-axis
plt.grid(True, linewidth= 1, linestyle="--") #creates a dashed grid with a 1 width
plt.title('Facewash and facecream sales data') #creates title Facewash and facecream sales data
plt.show() #Asks to show the graph that has been created

# COMMAND ----------

#create bar chart for bathing soap data with lined grid
import pandas as pd #imports pandas
import matplotlib.pyplot as plt #imports matplotlibs

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv") #reads the saved excel sheet
monthList  = df ['month_number'].tolist() #assigns the month_number data from the sheet to monthlist
bathingsoapSalesData   = df ['bathingsoap'].tolist() #assigns the bathingsoap data from the sheet to bathingsoapSalesData
plt.bar(monthList, bathingsoapSalesData) #asks for bar chart to eb monthlist at the x-axis and bathingsoapSalesData
plt.xlabel('Month Number') #creates x-axis as Month Number
plt.ylabel('Sales units in number') #creates y-axis as Sales units in number
plt.title(' Sales data') 
plt.xticks(monthList) #lists the months in numbers on the x-axis
plt.grid(True, linewidth= 1, linestyle="--") #creates a dashed grid with a 1 width
plt.title('bathingsoap sales data') #creates title bathingsoap sales data
plt.savefig('D:\Python\Articles\matplotlib\sales_data_of_bathingsoap.png', dpi=150) #asks to save the data in a .png image as a density of 150 dpi
plt.show() #Asks to show the graph that has been created

# COMMAND ----------

#create profit data bar chart
import pandas as pd #imports pandas
import matplotlib.pyplot as plt #imports matplotlibs

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv") #reads the saved excel sheet
profitList = df ['total_profit'].tolist() #assigns the total_profit from the sheet to profitlist
labels = ['low', 'average', 'Good', 'Best'] 
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000] #creates x-axis with profit range defined
plt.hist(profitList, profit_range, label = 'Profit data') #creates title Profit data
plt.xlabel('profit range in dollar') #creates x-axis title profit range in dollar
plt.ylabel('Actual Profit in dollar') #creates y-axis title Actual Profit in dollar
plt.legend(loc='upper left') #crates legend and puts it in the upper left
plt.xticks(profit_range) #lists profit range in the x-axis
plt.title('Profit data') #creates title Profit data
plt.show() #Asks to show the graph that has been created

# COMMAND ----------

#Create a pie chart from the imported data
import pandas as pd #imports pandas
import matplotlib.pyplot as plt #imports matplotlibs

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv") #reads the saved excel sheet
monthList  = df ['month_number'].tolist() #assigns the month_number from the sheet to monthlist

labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer'] #creates labels for each segment of the pie chart
salesData   = [df ['facecream'].sum(), df ['facewash'].sum(), df ['toothpaste'].sum(), #assigns multiple data points 
         df ['bathingsoap'].sum(), df ['shampoo'].sum(), df ['moisturizer'].sum()]
plt.axis("equal") #same length axis
plt.pie(salesData, labels=labels, autopct='%1.1f%%') #creates a pie chart from the data
plt.legend(loc='lower right') #creates legend and puts it in the lower right
plt.title('Sales data') #creates title Sales data
plt.show() #Asks to show the graph that has been created

# COMMAND ----------

#create 2 line charts
import pandas as pd #imports pandas
import matplotlib.pyplot as plt #imports matplotlibs

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv") #reads the saved excel sheet
monthList  = df ['month_number'].tolist() #assigns the month_number from the sheet to monthlist
bathingsoap   = df ['bathingsoap'].tolist() #assigns the bathingsoap from the sheet to bathingsoap
faceWashSalesData   = df ['facewash'].tolist() #assigns the facewash from the sheet to facewashsalesdata

f, axarr = plt.subplots(2, sharex=True) #makes 2 charts 
axarr[0].plot(monthList, bathingsoap, label = 'Bathingsoap Sales Data', color='k', marker='o', linewidth=3) #plots bathing soap data on chart 0
axarr[0].set_title('Sales data of  a Bathingsoap') #sets title of chart 0 to Sales data of a bathingsoap
axarr[1].plot(monthList, faceWashSalesData, label = 'Face Wash Sales Data', color='r', marker='o', linewidth=3) #plots facewash data on chart 1
axarr[1].set_title('Sales data of  a facewash') #sets title of chart 1 to Sales data of a facewash

plt.xticks(monthList) #lists the months in numbers on the x-axis
plt.xlabel('Month Number') #creates x-axis label Month Number
plt.ylabel('Sales units in number') #creates y-axis label Sales units in number
plt.show() #Asks to show the graph that has been created

# COMMAND ----------

#create stack plot
import pandas as pd #imports pandas
import matplotlib.pyplot as plt #imports matplotlibs

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv") #reads the saved excel sheet
monthList  = df ['month_number'].tolist() #assigns the month_number from the sheet to monthlist

faceCremSalesData   = df ['facecream'].tolist() #assigns the facecream from the sheet to facecremsalesdata
faceWashSalesData   = df ['facewash'].tolist() #assigns the facewash from the sheet to facewashsalesdata
toothPasteSalesData = df ['toothpaste'].tolist() #assigns the toothpaste from the sheet to toothpastesalesdata
bathingsoapSalesData   = df ['bathingsoap'].tolist() #assigns the bathingsoap from the sheet to bathingsoapsalesdata
shampooSalesData   = df ['shampoo'].tolist()#assigns the shampoo from the sheet to shampoosalesdata
moisturizerSalesData = df ['moisturizer'].tolist() #assigns the moisturizer from the sheet to moisturizersalesdata

plt.plot([],[],color='m', label='face Cream', linewidth=5) #plots face cream with magenta color and a line width of 5, with a label of face cream
plt.plot([],[],color='c', label='Face wash', linewidth=5) #plots face wash with cyan color and a line width of 5, with a label of face wash
plt.plot([],[],color='r', label='Tooth paste', linewidth=5) #plots tooth paste with red color and a line width of 5, with a label of tooth paste
plt.plot([],[],color='k', label='Bathing soap', linewidth=5) #plots bathing soap with black color and a line width of 5, with a label of bathing soap
plt.plot([],[],color='g', label='Shampoo', linewidth=5) #plots shampoo with green color and a line width of 5, with a label of shampoo
plt.plot([],[],color='y', label='Moisturizer', linewidth=5) #plots moisturizer with yellow color and a line width of 5, with a label of moisturizer

plt.stackplot(monthList, faceCremSalesData, faceWashSalesData, toothPasteSalesData, #stacks a plot of the above data with the corresponding colors
              bathingsoapSalesData, shampooSalesData, moisturizerSalesData, 
              colors=['m','c','r','k','g','y'])

plt.xlabel('Month Number') #creates x-axis label of Month Number 
plt.ylabel('Sales unints in Number') #creates y-axis label of Sales units in number
plt.title('Alll product sales data using stack plot') #creates tiel of Alll product sales data using stack plot
plt.legend(loc='upper left') #creates legend and locates it in the upper left
plt.show() #Asks to show the graph that has been created

# COMMAND ----------


