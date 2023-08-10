#!/usr/bin/env python
# coding: utf-8

# Ques 1) Write a Python Program to Display Fibonacci Sequence Using Recursion?

# In[1]:


def recur_fibo(n):  
    if n <= 1:  
        return n  
    else:  
        return(recur_fibo(n-1) + recur_fibo(n-2))  

nterms = int(input("How many terms? ")) 

# check if the number of terms is valid  
if nterms <= 0:  
    print("Plese enter a positive integer")  
else:  
    print("Fibonacci sequence:")  
    for i in range(nterms):  
        print(recur_fibo(i)) 


# Ques 2) Write a Python Program to Find Factorial of Number Using Recursion?

# In[2]:


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)

num = int(input("Enter a number: "))

# check if the number is negative
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))


# Ques 3) Write a Python Program to calculate your Body Mass Index?

# In[3]:


def BMI(height, weight):
    BMI = weight / (height/100)**2 
    print("Your Body Mass Index is", BMI)

    if BMI <= 18.5:  
        print("Oops! You are underweight.")  
    elif BMI <= 24.9:  
        print("Awesome! You are healthy.")  
    elif BMI <= 29.9:  
        print("Eee! You are over weight.")  
    else:  
        print("Seesh! You are obese.")


# In[4]:


height = float(input("Enter the height in cm: "))  
weight = float(input("Enter the weight in kg: "))  

bmi = BMI(height, weight)


# Ques 4) Write a Python Program to calculate the natural logarithm of any number?

# In[5]:


import math

# log with base e
number =  int(input("Enter a number: "))
print (f"Natural logarithm of {number} is : ")
print (math.log(number))


# In[6]:


# log with base
number =  int(input("Enter a number: "))
base = int(input("Enter the base: "))
print (f"Logarithm base {base} of {number} is : ")
print (math.log(number, base))


# Ques 5) Write a Python Program for cube sum of first n natural numbers?

# In[7]:


def cube_sum(nterms):
    sum1 = 0
    cube = 0
    for i in range(1,nterms+1):
        sum1 = sum1+i
    print(sum1)
    cube = sum1**3
    return cube


# In[8]:


cube_sum(5)

