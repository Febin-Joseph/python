#1.)Create a list called numbers containing the first five even numbers.
#Access and print the last element of the numbers list.
#Modify the third element of the list to be '10'.

numbers = [2,4,6,8,10]
print("the last element in the list ", numbers[4])
numbers[3] = 10
print(numbers)

#2.) Create a dictionary called grades that maps the names of students to their respective grades 
# (e.g., 'Alice': 85, 'Bob': 92).
#Access and print the grade of the student named 'Bob'.

grade = {
    'Alice' : 85,
    'Bob' : 73,
    'Mark' : 90
}

print(grade['Bob'])
print(grade)


#MUCH MORE ON LISTS
#LIST METHODS
numbers = [1,2,3,4]

numbers.append(5)
print(numbers)

#3.)Write a function that takes two lists as input and merges them into a single sorted list.

merged_list = []

def merge_func():
    list1 = [11,2,4]
    list2 = [6,10,5]
    merged_list = list1 + list2
    merged_list.sort()
    print(merged_list)

merge_func()

#4.)Removing Duplicates: Write a function that takes a list as input and returns a new list with duplicates removed 
# while preserving the order of the elements.

new_list = []

def remove_duplicates():
    numbers = [1,4,5,3,4,2,6,5]
    removed_dup_numbers = list(set(numbers))
    print(removed_dup_numbers)

remove_duplicates()

# 5.)List Data Cleanup:
# You are given a list of strings containing numbers. Write a function to clean
# up the list by converting all the numeric strings into integers and removing
# any non-numeric strings. Return the cleaned-up list.

new_list = []


def list_cleanUp():
    myList = ["12", "abc", "34", "xyz", "56"]
    for integer in myList:
        try:
            new_integer = int(integer)
            new_list.append(new_integer)

        except ValueError:
            None

    return new_list


print(list_cleanUp())


#You are given two lists as input, and you need to find the common elements 
# between the two lists, without any duplicates. Your task is to write a
#  function that takes these two lists as input and returns a new list 
# containing the common elements.

#BREAKDOWN FOR THE TASK 

#Initialize an empty list to store the common elements.
#Loop through the elements of one list (e.g., list1).
#For each element, check if it exists in the other list (e.g., list2).
#If the element is found in list2 and not already in the common elements list, add it to the common elements list.
#Return the common elements list as the result.



def find_common_elements(list1, list2):
    common_list = []
    for element in list1:
        if element in list2 and element not in common_list:
            common_list.append(element)
    return common_list

print(find_common_elements([1,2,3,4], [3,4,5,6]))

#List Rotation
#Write a function that takes a list of numbers and an integer k as input and
#  rotates the list to the right by k steps. The rotation should be done 
# in-place, meaning you modify the original list.


def list_rotation(num, k):
    if not num:
        return num
    k = k % len(num)
    new_list = num[-k:] + num[:-k]

    return new_list

list = [1,2,3,4,7]
K_value = 2
result = list_rotation(list, K_value)
print(result)

#Even Numbers: Given a list of numbers, create a new list containing only 
# the even numbers using list comprehension

list_of_num = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [even for even in list_of_num if even %  2 == 0]
print(even_numbers)


#Character Frequency: Given a list of strings, create a new list containing 
# a dictionary that represents the frequency of each character in each string 
# using list comprehension.




                                #TUPLES


#1.)Create a tuple called numbers containing the first five odd numbers.
#Access and print the third element of the numbers tuple.

numbers = (1,3,5,7,9)
print(numbers[3])

#2.)Given a tuple of numbers, write a function that returns the sum of all 
# the elements in the tuple


total = 0

def sum_of_all(num):
        global total
        for number in num:
            total += number

        return total

print(sum_of_all((1,2,3,4,5)))


#Write a Python program that takes a list of tuples as input. Each tuple 
# contains a student's name (string) and their scores (tuple of integers). 
# The program should find and print the name of the student with the highest
#  total score.


def topper_calculation(score, students):
    top_score = list(score)

    top_score.sort(reverse=True)
    top_score = top_score[0]

    index_of_score = score.index(top_score)

    topper_student_name = students[index_of_score]


    return top_score, topper_student_name


score = (7,9,8,6,5)
students = ("alice", "mark", "john", "peter", "musk")
top_score,topper_student_name = topper_calculation(score, students)
print(f"the topper is {topper_student_name} who owns {top_score} marks out of 10")



#Nested Tuples:
#reate a tuple named contacts containing contact information for two people. 
# Each person's contact information should be in the format (name, email, phone).
#  Print the tuple and then access and print the phone number of the second person.

person1 = ("febin", "@gmail", 7561)
person2 = ("achu1", "12@gmail", 9947)

persons =(person1, person2)

for person in persons:
    name, email, phone = person
    print(f"name: {name} email: {email} phone: {phone}")

print(persons[0][2])
print(person2[2])

#Create a dictionary called fruits_stock with the following fruits and their 
# respective quantities: 'apple' (5), 'banana' (3), 'orange' (7).
#Access and print the quantity of 'orange' from the fruits_stock dictionary.
#Use the keys() method on fruits_stock and print the result.
#Use the values() method on fruits_stock and print the result.
#Use dictionary comprehension to create a new dictionary called double_stock with 
# the same fruits as keys and the double of their quantities as values.

fruits_stock = {
    'apple' : 5,
    'banana' : 3,
    'orange' : 7
}

print(fruits_stock.get('orange'))

print(fruits_stock.items())

double_stock = {fruits: quantity * 2 for fruits, quantity in fruits_stock.items()}
print(double_stock)

#Implement a function called find_max that takes three numbers as parameters and returns 
# the largest one.

value = [11,13,5,17,19,12,34,11]

def find_max_value(nums):
    if not nums:
        print("please enter some values ")
    else:
        print(nums)
        sorted_value = sorted(nums, reverse=True)
        print(sorted_value)
        higher_value = sorted_value.pop(0)
        print(f"the greater value is {higher_value}")

    
find_max_value(value)

