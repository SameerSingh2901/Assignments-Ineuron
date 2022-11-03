#!/usr/bin/env python
# coding: utf-8

# Ques 1) Write a Python program to print "Hello Python"?

# In[1]:


print("Hello Python")


# Ques 2) Write a Python program to do arithmetical operations addition and division?

# In[2]:


a = 2
b = 7
# program for addition
add = a+b
print(add)

# program for division
div = a/b
print(div)


# Ques 3) Write a Python program to find the area of a triangle

# In[3]:


height = int(input("Enter the height"))
base = int(input("Enter the base"))

# calculating the area of triangle
area = 0.5 * (base*height)
print(area)


# Ques 4) Write a Python program to swap two variables?

# In[4]:


first_num = int(input("Enter First Number"))
second_num = int(input("Enter Second Number"))

#swapping the variables using a third dummy variable
change = first_num
first_num = second_num
second_num = change

# printing the results
print(f"The value of first number after swapping is {first_num}")
print(f"The value of second number after swapping is {second_num}")


# Ques 5) Write a Python program to generate a random number?

# In[5]:


# for generating random number in python we use random library
import random

# generating a random number from 0 to 100
print(random.randint(0,100))

