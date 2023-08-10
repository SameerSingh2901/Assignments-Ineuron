#!/usr/bin/env python
# coding: utf-8

# Ques 1) Write a Python program to convert kilometers to miles?

# In[1]:


# first taking the input of kilometers
kilo = int(input("Enter kilometers"))

#converting kilometers to miles
miles = kilo/1.609

print(f"{kilo} km in miles will be {miles} miles")


# Ques 2) Write a Python program to convert Celsius to Fahrenheit?

# In[2]:


# first taking the input of celcius
cel = int(input("Enter the celcius temperature"))

#converting celcius to fahrenheit
faren = (cel * 9/5) + 32

print(f"{cel} celcius to fahrenheit is {faren}")


# Ques 3) Write a Python program to display calendar?

# In[3]:


# to display calendar in python we use 'calendar' library

# importing calendar module
import calendar

# taking the input of year and month
year = int(input("Enter year: "))
month = int(input("Enter month: "))

# display the calendar
print(calendar.month(year, month))


# Ques 4) Write a Python program to solve quadratic equation?

# In[4]:


# import complex math module  
import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
# calculate the discriminant  
d = (b**2) - (4*a*c)  


# solving the equations
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  

  
# printing the results
print(f"The solution are {sol1} and {sol2}")   


# Ques 5) Write a Python program to swap two variables without temp variable?

# In[5]:


# taking the input of first and second number
number1 = int(input("Enter first number"))
number2 = int(input("Enter second number"))

#swapping the variables
number1, number2 = number2, number1

#printing the results
print(f"First number after swapping is {number1}")
print(f"Second number after swapping is {number2}")

