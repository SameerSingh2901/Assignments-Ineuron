#!/usr/bin/env python
# coding: utf-8

# Ques 1) Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[1]:


# taking the input 
number = int(input("Enter a number"))

# checking the number
if number == 0:
    print(number, "is zero.")
elif number>0:
    print(number, "is positive")
elif number<0:
    print(number, "is negative")


# Ques 2) Write a Python Program to Check if a Number is Odd or Even?

# In[2]:


# taking the input 
number = int(input("Enter a number"))

# checking the number
if number%2 == 0:
    print(number, "is a even number")
else:
    print(number, "is a odd number")


# Ques 3) Write a Python Program to Check Leap Year?

# In[3]:


# taking the input of the year
year = int(input("Enter the year: "))

#checking the year if it is leap year or not
if year%400 == 0 or year%100 != 0 and year%4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


# Ques 4) Write a Python Program to Check Prime Number?

# In[4]:


#taking the input
num = int(input("Enter a number: "))

#checking the number if it is prime or not
if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
            else:
                print(num, "is a prime number")
                break
else:
    print(num, "is not a prime number")


# Ques 5) Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[5]:


for num in range (1, 10000):  
    if num > 1:  
        for i in range (2, num):  
            if (num % i) == 0:  
                break  
        else:  
            print (num)  

