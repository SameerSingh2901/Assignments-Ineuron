#!/usr/bin/env python
# coding: utf-8

# Ques 1) Write a Python Program to Find LCM?

# In[1]:


def lcm(num1, num2):
    try:
        # choose the greater number
        if num1 > num2:
            greater = num1
        else:
            greater = num2

        while(True):
            if((greater % num1 == 0) and (greater % num2 == 0)):
                lcm = greater
                break
            greater += 1
        return lcm
    except Exception as e:
        print(e, "/n Please try again")


# In[2]:


lcm(4, 7)


# Ques 2) Write a Python Program to Find HCF?

# In[3]:


def hcf(num1, num2):
    try:
        if num1 > num2:
            smaller = num2
        else:
            smaller = num1
        for i in range(1, smaller+1):
            if((num1 % i == 0) and (num2 % i == 0)):
                hcf = i 
        return hcf
    except Exception as e:
        print(e, "/n Please try again")


# In[4]:


hcf(54, 24)


# Ques 3) Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

# In[5]:


# Python program to convert decimal into other number systems
dec_num = 7

print("The decimal value of", dec_num, "is:")
print(bin(dec_num), "in binary.")
print(oct(dec_num), "in octal.")
print(hex(dec_num), "in hexadecimal.")


# Ques 4) Write a Python Program To Find ASCII value of a character?

# In[6]:


"""
ASCII stands for American Standard Code for Information Interchange.
It is a numeric value given to different characters and symbols, for computers to store and manipulate. 
For example, the ASCII value of the letter 'S' is 83.
"""
val = 'Z'
print("The ASCII value of '" + val + "' is", ord(val))


# Ques 5) Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

# In[7]:


class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def dosum(self):
        try:
            added_sum = self.num1 + self.num2
            return added_sum
        except Exception as e:
            print(e)
    def domul(self):
        try:
            mul = self.num1*self.num2
            return mul
        except Exception as e:
            print(e)
    def dodiv(self):
         try:
            div = self.num1/self.num2
            return div
         except Exception as e:
            print(e)
    def dosub(self):
         try:
            sub = self.num1-self.num2
            return sub
         except Exception as e:
            print(e)


# In[8]:


num = calculator(8,2)


# In[9]:


num.dodiv()


# In[10]:


num.domul()


# In[11]:


num.dosub()


# In[12]:


num.dosum()

