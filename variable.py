#PRINT NAME
name = "febin"
print(name)

#SUM
num1 = 10
num2 = 20
result = num1 + num2
print(result)

#USER INPUT
name = input("enter your name ")
age = int(input("enter age "))
print("you name is",name,"your age is",age)

#FLOAT TO INTEGER
num = 10.6432
result = int(num)
print(result)


#Identity and Equality
x = [1,2,3]
y = [1,2,3]
z = y
print(z is y)
print(x is y)
print(x == y)

#ALL ARITHMETIC OPERATIONS
num1 = int(input("Enter number one "))
num2 = int(input("Enter number two"))

print("addition",num1 + num2)
print("substraction",num1 - num2)
print("Multipilcation",num1 * num2)
print("Division",num1 / num2)
print("Modulus",num1 % num2)
print("exponential",num1 ** num2)

#CHECKING GIVEN NUMBER IS EVER OR NOT
num = int(input(" enter a number "))
if num % 2 == 0:
    print("given number is even")
else :
    print("given number is odd")

#CHECKING GIVEN NUMBER IS POSITIVE NEGATIVE OR ZERO
num = int(input("enter a number"))

if(num > 0) :
    print(num,"is a positive number")
elif (num < 0) :
    print(num,"is a negative number")
else :
    print("entered num is zero")


#Write a program that takes an integer as input from the user and checks if it is a positive number less than 100.
#  Use logical operators to combine the conditions.

num = int(input("enter a number "))

if not(num < 0 or num >= 100) :
      print("the entered number is greater than zero and less than 100")
elif(num > 100) :
    print("number is greater han 100")
elif(num == 0) :
     print("number is zero")
else:
     print("num is negative")


#SHOPING CART
item1 = 120
print(item1)
item1 += 10
print(item1)
item1 += 20
print(item1)

#Write a program that calculates the grade for a given score.
#90 or above: "A"
#80-89: "B"
#70-79: "C"
#60-69: "D"
#Below 60: "F

inpt = int(input("enter your grade "))
if(inpt >= 90) :
    print("A")
elif(inpt >=80 and inpt<=89) :
    print("B")
elif(inpt >=70 and inpt<=79) :
    print("C")
elif(inpt >=60 and inpt<=69) :
    print("D")
elif(inpt < 60) :
    print("F")

## Exercise 3: Calculate the sum of numbers in a list numbers = [10, 20, 30, 40, 50]

numbers = [10, 20, 30, 40, 50]

sum = 0

for num in numbers :
    sum += num
    total = sum
    print(total)


#SUM USING FOR IN LOOP

def calculate_sum(sum_of_numb):
    total_sum = 0
    for sums in sum:
        total_sum += sums
    return total_sum
    
sum = [1, 2, 3, 4, 5]
result = calculate_sum(sum)
print(result)


#FINDING VOWELS
vowels = "aeiou"
count = 0

inpt = input("enter a string ")
inpt = inpt.lower()

for char in inpt:
    if char in vowels:
        count += 1

print(count)

#Create a while loop that runs indefinitely 
# until the user enters a positive integer

while True:
    inpt_num = int(input("enter a possitive number "))
    if inpt_num > 0:
      print("entered a possitive number")
      break
    else:
       print("please enter a positive number")

#Write a program that generates random numbers between 1 and 10 until a 
# randomly generated number is equal to 7. Count the number of 
# attempts it took to generate the number 7 and print the count

import random

count = 0

while True:
    random_num = random.randint(1,10)
    count += 1

    if random_num == 7:
        break

print("number found at ",count)

#Write a program that simulates a simple guessing game. The program should
#  generate a random number between 1 and 10 and repeatedly ask the user to 
# guess the number. Provide feedback to the user if their guess is too high 
# or too low. Once the user guesses the correct number, print a congratulatory
#  message along with the number of attempts it took

import random


random_num = random.randint(1,3)
attempt = 0

while True:
    attempt += 1
    guess = int(input(" enter a number between 1 - 10 "))

    if guess == random_num:
        print("Congratulations! You guessed the number", random_num, "in", attempt, "attempts.")
        break
    elif guess > random_num:
        print("your too high")
    else:
        print("you are too low")

#Write a program that prompts the user to enter a series of numbers.
#  The program should calculate the sum of the entered numbers, but if the user
#  enters a negative number, the program should stop taking input and print 
# the final sum.

sum = 0

while True:
    inpt = int(input(" enter the number wnat to sum "))
    if inpt < 0:
        break

    sum += inpt

print(sum)

#Write a program that prompts the user to enter two numbers. The program should handle the following exceptions:

#If the user enters non-numeric input, display an error
#message: "Error: Invalid input. Please enter a valid 
#number."
#If the user attempts to divide by zero, display an error 
# message: "Error: Cannot divide by zero."
#If the user enters valid numbers, calculate and display 
# the result of dividing the first number by the second 
# number.

try:
    num1 = int((input("enter number one ")))
    num2 = int(input("enter number two "))

    result = num1 / num2
    print("the division is ",result)

except ZeroDivisionError:
    print("the number cannot be divided using 0")
except ValueError:
    print("entera valid number ")