#!/usr/bin/env python
# coding: utf-8

# Ques 1) Write a Python Program to Find the Factorial of a Number?

# In[1]:


# taking the input of a number
num = int(input("Enter a number for calculating factorial: "))

# calculating the factorial
factorial = 1 # this is for initializing the variable
for i in range(1, num+1):
    factorial = factorial*i
print(f"Factorial of - {num} is {factorial}")


# Ques 2) Write a Python Program to Display the multiplication Table?

# In[2]:


# taking the input
num = int(input("Enter a number to display it's table: "))

# making the table and printing the table
for i in range(1, 11):
    print(num*i)


# Ques 3) Write a Python Program to Print the Fibonacci sequence?

# In[3]:


# first initializing the first two numbers 
num1 = 0
num2 = 1
count = 0
# taking the input for the range 
num = int(input("Enter a positive number "))

# creating the sequence
if num <= 0:
    print("Please enter a positive integer")
elif num == 1:
    print(f"Fibonacci sequence upto {num} is:")
    print(num1)
else:
    print(f"Fibonacci sequence upto {num} is:")
    while count < num:
        print(num1)
        nth = num1 + num2
        # update values
        num1 = num2
        num2 = nth
        count += 1


# Ques 4) Write a Python Program to Check Armstrong Number?

# In[4]:


# taking the input to check if it is a armstrong number or not
num = int(input("Enter a number: "))

# calculating the length of the input
length = len(str(num))

# initializing the variables
add = 0

# checking the number
temp = num
while temp > 0:
    digit = temp % 10
    add += digit ** length
    temp //= 10

# printing the results

if num == add:
    print(f"Yes! {num} is a armstrong number")
else:
    print(f"No! {num} is not a armstrong number")


# Ques 5) Write a Python Program to Find Armstrong Number in an Interval?

# In[5]:


# finding Armstrong numbers in between 1 to 1000

# initializing the variable
add=0

# calculating
for num in range(1, 1001):
    length = len(str(num))
    add = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        add += digit ** length
        temp //= 10

    if num == add:
        print(num)  


# Ques 6) Write a Python Program to Find the Sum of Natural Numbers?

# In[6]:


# taking the input
num = int(input("Enter a range: "))

if num < 0:
    print("Enter a positive number")
else:
    add = 0
   # use while loop to iterate until zero
    while(num > 0):
        add += num
        num -= 1
    print("The sum is", add)

