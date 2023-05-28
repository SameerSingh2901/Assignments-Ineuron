#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Ques 1)
Write a function that stutters a word as if someone is struggling to read it. 
The first two letters are repeated twice with an ellipsis ... and space after each, 
and then the word is pronounced with a question mark ?.

"""


# In[1]:


def shutter(st):
    if len(st)>2:
        shutter = st[:2] + '... ' + st[:2] + '... ' + st + '?'
    else:
        shutter = st + '... ' + st + '... ' + st + '?'
    return shutter


# In[2]:


st1 = "my name is sameer"
shutter(st1)


# In[ ]:


"""
Ques 2) 
Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.
"""


# In[3]:


def rad_to_deg(rad):
    deg = rad * 180 / 3.14159265359
    return round(deg, 1)


# In[4]:


rad_to_deg(7)


# In[ ]:


""" 
Ques 3) 
In this challenge, establish if a given integer num is a Curzon number. 
If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.

"""


# In[5]:


def check_curzon(num):
    if (2**num +1)%(2*num +1) == 0:
        return True
    else:
        return False


# In[6]:


check_curzon(14)


# In[ ]:


# Ques 4) Given the side length x find the area of a hexagon.


# In[7]:


import math
def area_hex(side):
    return ((3 * math.sqrt(3) * (side * side)) / 2)  


# In[8]:


area_hex(1)


# In[ ]:


"""
Ques 5)
Create a function that returns a base-2 (binary) representation of a base-10
(decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10)
010101001(2) = 1 + 8 + 32 + 128.

Going from right to left, the value of the most right bit is 1, now from that every bit to the left
will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).

""" 


# In[9]:


def dec_to_bi(decimal):
    decimal = int(decimal)
    binary = ""
    
    if decimal == 0:
        binary = "0"
    else:
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal = decimal // 2
    
    return binary


# In[10]:


decimal_number = input("Enter a decimal number: ")
binary_number = dec_to_bi(decimal_number)
print("Binary representation:", binary_number)

