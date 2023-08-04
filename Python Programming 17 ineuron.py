#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ques 1) Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided 
# by c from the range a, b inclusive.


# In[2]:


def evenly_divisible(a, b, c):
    list_ = [num for num in range(a, b+1) if num%c == 0]
    return sum(list_)


# In[3]:


evenly_divisible(1, 10, 20)


# In[4]:


evenly_divisible(1, 10, 2)


# In[5]:


# Ques 2) Create a function that returns True if a given inequality expression is correct and False otherwise.


# In[6]:


def correct_signs(string):
    inequalities = string.split()

    for i in range(1, len(inequalities), 2):
        operator = inequalities[i]
        left_operand, right_operand = float(inequalities[i - 1]), float(inequalities[i + 1])
        if operator == '>':
            if left_operand <= right_operand:
                return False
        elif operator == '<':
            if left_operand >= right_operand:
                return False
        else:
            raise ValueError(f"Invalid operator '{operator}' in the expression.")

    return True


# In[7]:


correct_signs("3 < 7 < 11")


# In[8]:


correct_signs("13 > 44 > 33 > 1")


# In[9]:


# Ques 3) Create a function that replaces all the vowels in a string with a specified character.


# In[10]:


def replace_vowels(input_string, specified_vowel):
    vowels = 'aeiouAEIOU'
    new_string = "".join(specified_vowel if char in vowels else char for char in input_string)
    return new_string


# In[11]:


replace_vowels("the aardvark", "#")


# In[12]:


replace_vowels("minnie mouse", "?")


# In[13]:


# Ques 4) Write a function that calculates the factorial of a number recursively.


# In[14]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# In[15]:


factorial(5)


# In[16]:


factorial(3)


# In[17]:


# Ques 5) Create a function that computes the hamming distance between two strings.


# In[18]:


def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must have equal length.")
    
    distance = sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))
    return distance


# In[19]:


hamming_distance("abcde", "bcdef")


# In[20]:


hamming_distance("strong", "strung")

