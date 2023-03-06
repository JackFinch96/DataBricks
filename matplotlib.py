# Databricks notebook source
import matplotlib.pyplot as plt
import numpy as np

# COMMAND ----------

y

# COMMAND ----------

y = np.linspace(-1, 1, 5)
y2 = np.linspace(-2, 2, 5)
x = np.arange(5)
fig = plt.figure()
ax = fig.subplots()
line1 = ax.plot(x,y)
line2 = ax.plot(x,y2)

# COMMAND ----------

number_rows = 3
number_columns = 2
fig2 = plt.figure()
ax2 = fig2.subplots(number_rows, number_columns)
ax2[2,1].plot(x,y)
ax2[1,0].plot(x,y)

# COMMAND ----------

y1 = np.arange(0,110,10)
y2 = np.random.random(11)
x = np.arange(11)
fig, ax = plt.subplots(2,2) #plots in a 2x2 grid
ax[0,0].plot(x,y1) #plots line graph
ax[0,1].scatter(x,y2) #plots scatter graph
ax[1,0].bar(x,y1) #plots bar chart
ax[1,1].barh(x,y1) #plots horizontal barchart

# COMMAND ----------

x = np.arange(0, 4*np.pi, 0.05)
ycos = np.cos(x)
ysin = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, ycos, 'b-', label="cos(x)")
ax.plot(x, ysin, 'r--', label="sin(x)")
ax.set_title("Triganomic Functions")
ax.set_xlabel("0 to 4 Pi")
ax.set_ylabel("cos(x) and cos(y)")
ax.legend()

# COMMAND ----------

fig, ax = plt.subplots(1,2)

ax[0].axhline(0.3, color='red')
ax[0].axhline(0.4, linestyle='--', color='blue')
ax[0].axhline(0.5, color='cyan', linewidth=10)
ax[0].axhline(0.6, linestyle=':', xmin=0.25, xmax=0.75, color=('orchid'))
ax[0].axhline(0.7, xmin=0.25, xmax=0.75, color=(0.1, 0.2, 0.5, 0.3))
              
ax[1].axvline(0.3, color='red')
ax[1].axvline(0.4, linestyle='--', color='blue')
ax[1].axvline(0.5, color='cyan', linewidth=10)
ax[1].axvline(0.6, linestyle=':', ymin=0.25, ymax=0.75, color=('orchid'))
ax[1].axvline(0.7, ymin=0.25, ymax=0.75, color=(0.1, 0.2, 0.5, 0.3))

#set x-axis and y-axis limits
ax[0].set_ylim(0.1, 0.9)
ax[1].set_xlim(0.1, 0.9)
#set title to figure and subplots
fig.suptitle("Horizontal and vertical lines", fontsize=14)
ax[0].set_title('Horizontal lines', fontstyle='italic')
ax[1].set_title('Vertical lines', color='green', fontname='Arial')
      

# COMMAND ----------

x = np.array([2,4,6,7,4,2,5,7,8,9,4,2,1])
y = np.array([7,5,4,1,6,7,8,1,9,5,9,3,5])
fix, ax = plt.subplots(1,3)
ax[0].scatter(x,y)
ax[0].set_title('default')
ax[1].scatter(x,y, 50, marker='+')
ax[1].set_title('size=50, style = +')
crosses = ax[2].scatter(x,y, 200, marker='+', linewidth=3)
bullets = ax[2].scatter(x,y, 50, marker='o', color='black')
bullets.set_edgecolors('red')
bullets.set_linewidth(1.5)
ax[2].set_title('mixed')

# COMMAND ----------

z = np.array([0,1,4,3,5,1,2,5,7,5,9,8,5])
fig = plt.figure()
ax = np.array([fig.add_subplot(1,3,1, projection='3d'),
               fig.add_subplot(1,3,2, projection='3d'),
               fig.add_subplot(1,3,3, projection='3d')])
ax[0].scatter(x,y,z)
ax[0].set_title('default')
ax[1].scatter(x,y,z, s=50, marker='+')
ax[1].set_title('size = 50, style = +')
crosses = ax[2].scatter(x,y,z,s=200, marker='+', linewidth=3)
bullets = ax[2].scatter(x,y,z, s=50, marker='o', color='black')
bullets.set_edgecolors('red')
bullets.set_linewidth(1.5)
ax[2].set_title('mixed')


# COMMAND ----------

#Bar Plot Exercise
people = ["Student A", "Student B"]
studentA = np.array([90,50,80,40])
studentB = np.array([75,45,60,95])
x = np.arange(len(studentA))
#Figure
fig, ax = plt.subplots(1,2)
#plots
ax[0].bar(x, studentA, width=0.3)
ax[1].bar(x, studentB, width=0.3)

#Aesthetics
for i in range(len(ax)):
    ax[i].set_ylim([0,100])
    ax[i].set_title(people[i])
    ax[i].set_xlabel("Exercise")
    ax[i].set_ylabel("Mark (%)")
    ax[i].set_xticks([0,1,2,3])
    ax[i].set_xticklabels(["Ex1", "Ex2", "Ex3", "Ex4"])
    

# COMMAND ----------

#Bar Plot, Grouped
fig, ax = plt.subplots()
width = 0.3
s1bars = ax.bar(x - width/2, studentA, width, label='Student A')
s2bars = ax.bar(x + width/2, studentB, width, label='Student B')

ax.set_title('Student Performance')
ax.legend()
ax.set_xticks([0,1,2,3])
ax.set_xticklabels(["Ex1", "Ex2", "Ex3", "Ex4"])
ax.set_ylim([0,100])
ax.set_xlabel("Exercise")
ax.set_ylabel("Mark (%)")

for i in range(len(studentA)):
    s2bars[i].set_linewidth(3.5)
    s2bars[i].set_linewidth(3.5)
    if studentA[i] < 50:
        s1bars[i].set_edgecolor('red')
    if studentB[i] < 50:
        s2bars[i].set_edgecolor('red')
