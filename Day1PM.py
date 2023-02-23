# Databricks notebook source
print("Hello World")

# COMMAND ----------

#stings
machine_name = "AKEA L"

print(machine_name)

#booleans
bool1 = True
bool2 = False

print(bool2)
    
#integer
int1 = 4296
int2 = 1657

print(int1 , int2)

#float
float1 = 28.8
    
print(float1)

#list
list1 = [30,33,36,42,28]
list_products = ["AKEA", "ORT", "DELTA LINE"]
    
print(list1)
print(list_products)

# COMMAND ----------

number1 = input("please enter a number")
number2 = input("enter a second")

print(int(number1) + int(number2))

# COMMAND ----------

varName = "variable"
var2name = 12

var2name += -2

print(var2name)

# COMMAND ----------

num1 = 19
num2 = 96

print(num1 < num2) #less thank
print(num1 == num2) #equal too
print(num1 != num2) #not equal too
print(num1 == num2 or 10 > 11)
print(num1 == num2 and 10 > 11)
if num1 > num2:
    print("first number is greater") #indented, so will have to meet conditions
elif num1 == num2:
    print("the numbers are equal") # indented, so will have to meet conditions
else:
    print("second number is even greater") #indented, so will have to meet conditions
print("second number is better") #will run regardless


# COMMAND ----------

#TASK

#ask for  two numbers to be input, then display the larger of the t

number1 =input("please enter first number")
number2 = input("Please enter second number")

print(number1 > number2)

# COMMAND ----------

#TASK

#write some code that will output to the screen if the year you were born was a leap year

inputYear = input("What year were you born?")
    
print(int(inputYear) % 4 == 0)

if(int(inputYear) % 4 == 0):
    print("Born on a leap year partner")
else :
    print("Not born on a leap year")

# COMMAND ----------

#           1 2 3 4 5 6 7 8 9
products = [1,2,3,4,5,6,7,8,9]

print(products[0])
print(products[1])
print(products[2])
print(products[3])
print(products[4])
print(products[5])
print(products[6])
print(products[7])
print(products[8])

for counter in range(9): #creates a range from count above
    print(counter)
    
for coutner in range(4,9): #creates a range in the specific range
    print(counter)
    
print(list(range(5))) #creates a range function

for counter in range(9): #creates a counter with products counter inside
    print(counter, products[counter])

for counter in range(len(products)):
    print(counter, products[coutner])

# COMMAND ----------

count = 1
while count < 10:
    print(count)
    count =+ 1
    break


# COMMAND ----------

password = "letmein1!"

entry = False

while entry != password:
    entry = input("Please enter your password")
    
print("Its about time")

# COMMAND ----------

guess = False
while guess != "Jack":
    guess = input("Guess my name")
print("Well done")


# COMMAND ----------

while True:
    guess = input("Guess my name")
    if guess != "Jack":
        print("Wrong")
        continue
    print("Correct")
    break

# COMMAND ----------

# Ask the user to enter a series of numbers 
# Create a total by adding each number to the last
# Stop adding numbers when the user types zero
# Print out the total at the end 

total = 0
while True:
    guess  =input("next number?...")
    if(int(guess) == 0):
       break
    else:
       total +=int(guess)
       print("Current total: ", total)

    




# COMMAND ----------

def convert_to_kg(number):
    convert_to_kgNumber = number // 2.2
    return convert_to_kgNumber

    def outputter(num):
        print(num)
        
numToDivide = 100

answer = convert_to_kg(numToDivide)

print("100lbs to KG is: ", answer)

# COMMAND ----------

def convert_to_celcius(number):
    convert_to_celcius = (number - 32)*(5/9)
    return convert_to_celcius

    def outputter(num):
        print(num)
        
numToMultiply = 100

answer = convert_to_celcius(numToMultiply)

print("32f to C is: ", answer)

# COMMAND ----------

#list = [1,2,3,4,5,6,7,8,9,10] # user generated list

input_sum = sum(user_input) #sum
input_average = input_sum / len(user_input) # average
for number in user_input:
    print(number)
    if number == input_average
        print("Num is equal to average")
    elif number < input_average
        print("Num is less than average")
    else:
        print("Num is greater than average")


# COMMAND ----------

#Sequential Steps

x = 2
print(x)
x = x + 2
print(x)

# COMMAND ----------

#Conditional Steps

x = 5
if x < 10:
    print("Smaller")
if x > 20:
    print("Bigger")
print("Finis")

# COMMAND ----------

#Repeated Steps

n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blast off!")

# COMMAND ----------

#Multiplication Steps

hours = 37.5
wage = 12.5
pay = hours * wage
print(pay)

# COMMAND ----------

#Expressions   #+ Add   #- Subtract   #* Multiply   #/ Divide   #** Power   #% Remainder

xx = 2
xx = xx + 2
print(xx)

yy = 440 * 12
print(yy)

zz = yy / 1000
print(zz)

jj = 23
kk = jj % 5
print(kk)

print(4 ** 3)

# COMMAND ----------

#Order of evaluation

x = 1 + 2 ** 3 /4 *5    #It will do 2**3 first (power), then /4 (divide) as its before *5 (multiply) , then *5 (multiply) , then +1 (Addition)
print(x)

# COMMAND ----------

#Turn integer to floating point

print(float(99) + 100)

# COMMAND ----------

#integer division

print(10 / 2)
print(9 / 2)
print(99 / 100)
print(10.0 / 2.0)

# COMMAND ----------

#Changing a string to an integer

sval = "123"
ival = int(sval)
print(ival +1)


# COMMAND ----------

#User Input

Jack = input("Who are you?")
print("Welcome", Jack)

# COMMAND ----------

#Converting User input - Elevator example US to Europe

inp = input("Europe Floor?")
usf = int(inp) + 1
print("US Floor", usf)

# COMMAND ----------



# COMMAND ----------

#Roll the Dice Simulator

#write a program that simulates rolling a dice, which randomly chooses between 1 - 6, print and ask to roll again?

import random #Imports random library
repeat = True
while repeat:
    print("You rolled",random.randint(1,6)) #Assigns a value between 1 & 6 and shows me the number with the comment "You rolled"
    print("Do you want to roll again? Y/N") #Ask me if I want to roll again with a Y or N answer
    repeat = "Y" in input() #If Y is said, it will look and re-roll the "Dice", if no it will complete the command 
    

# COMMAND ----------

#Guess the number 

#Create a program that will guess the number between 1 - 10, tell you if you are too high, low or got it correct

import random #Import random library
correct_number = random.randint(1, 10) #Assign random value between 1-10
guess = int(input("Guess the secret number between 1-10: ")) #This allows the user to guess what the number could be

while guess != correct_number: 
    if guess < correct_number:
        print("Sorry, your guess is too low.") #Prints message if number is too high
    else:
        print("Sorry, your guess is too high.") #Prints message if number is too low
        
#It will keep looping until correct number is given
    
    guess = int(input("Guess the secret number between 1-10: ")) #This will ask to try to guess again
 
print("You guessed the number!") #This will show when the correct number is guessed

# COMMAND ----------

#Mad Libs Generator



print("Hello, and welcome to my little Mad Libs game.")

playing= input("Lets play\n")

if playing.lower() != "yes":
    quit()
    
    print("Okay, let get it on:\n")
    
noun1 = input("What is your name?")
noun2 = input("What is your Friend's name")
noun3 = input("Enter another Friend's name")
place = input("Enter place name")
adjective1 = input("Enter an adjective")
adjective2 = input("Enter another adjective")
adjective3 = input("Enter one more adjective")
adverb1 = input("Enter an adverb")
adverb2 = input("Enter another adverb")

#print story

print(
    "One day\t" + noun1 + " went to " + place + ". "
    "He felt deflated, even though the scenery was " + adjective1 + ". "
    "He decided to invite his two friends " + noun2 + " and " + noun3 + ". "
    "When they came, they told " + noun1 + " something " + adjective2 + " had happened. "
    + noun1 + " went there very " + adverb1 + ". "
    "When he came he found out that his other friend was falling off the cliff. "
     + noun1 + " said inside, he was feeling "  + adjective3 + ". "
     + noun1 + " managed to save him."
    " After that they had a " + adverb2 + " celebration."
    " They all laughed.")

# COMMAND ----------

answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]

print("Welcome to my adventure game! Let's begin!")
print("You are lost in the Forest and you discover an abandoned Cabin.")
print("Will you enter the Cabin?. (Yes / No)")

ans1 = input(">>")

if ans1 in answer_yes:
    print("\nYou see a shadow figure hiding in the corner of a poorly lit room. Do you approach? (Yes / No)\n")

    ans2 = input(">>")

    if ans2 in answer_yes:
        print("\nTurns out it was just a fiendly Hunter. they looked after you and took you back home safely. Congratulations!")

    elif ans2 in answer_no:
        print("\You startled the Hunter staying in the Cabin and he attacked you. Game over!")

    else:
        print("\nYou typed the wrong input. GOODBYE!")

elif ans1 in answer_no:
    print("\nYou come across a sleeping bear. Do you try to sneak past it? (Yes / No)\n")

    ans3 = input(">>")

    if ans3 in answer_yes:
        print("\nDispite your bext efforts. He woke up and attacked you. Better luck next time!")

    elif ans3 in answer_no:
        print("\nCongratulations! You stud your ground and scared the bear off and made it to safety!")

    else:
        print("\nYou typed the wrong input. The adventurer starved in the wilderness. Try again.")

else:
    print("\nYou typed the wrong input. The adventurer starved in the wilderness. Try again.")

# COMMAND ----------


