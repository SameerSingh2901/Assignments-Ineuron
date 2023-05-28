#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ques 1) Write a Python program to find words which are greater than given length k?


# In[2]:


def len_words(li, k):
    for words in li:
        if len(words) > k:
            print(words)


# In[3]:


li_words = ['sameer', 'aman', 'riddhi', 'priyanshu', 'nirmal']

len_words(li_words, 4)


# In[4]:


# Ques 2) Write a Python program for removing i-th character from a string?


# In[5]:


def rem_char(st, c):
    b_st = st[:c]
    f_st = st[c+1:]
    
    return b_st+f_st


# In[6]:


st = 'sameer is a data science student'
rem_char(st, 10)


# In[7]:


# Ques 3) Write a Python program to split and join a string?


# In[8]:


def split_string(string):
    list_string = string.split(' ')

    return list_string

def join_string(list_string):
    string = " ".join(list_string)

    return string


# In[9]:


# Splitting a string
list_string = split_string("sameer is a science student")
print(list_string)


# In[10]:


# Join list of strings into one
new_string = join_string(list_string)
print(new_string)


# In[11]:


# Ques 4) Write a Python to check if a given string is binary string or not?


# In[12]:


def bi_check(string):
    
    p = set(string)
    
    s = {'0', '1'}

    if s == p or p == {'0'} or p == {'1'}:
        print("Yes")
    else:
        print("No")


# In[13]:


string = "101010000111"

bi_check(string)


# In[14]:


# Ques 5) Write a Python program to find uncommon words from two Strings?


# In[15]:


def find_uncommon(st1, st2):
    set1 = set(st1.split(' '))
    set2 = set(st2.split(' '))
    
    if(set1 ^ set2):
        print('Uncommon words are:', str(set1 ^ set2))


# In[16]:


st1 = "my name is sameer"
st2 = "sameer is a data science student"

find_uncommon(st1, st2)


# In[17]:


# Ques 6) Write a Python to find all duplicate characters in string?


# In[18]:


def find_common(st1, st2):
    set1 = set(st1.split(' '))
    set2 = set(st2.split(' '))

    if (set1 & set2):
        print(set1 & set2)
    else:
        print("No common elements")


# In[19]:


find_common(st1, st2)


# In[20]:


# Ques 7) Write a Python Program to check if a string contains any special character?


# In[21]:


def sp_char(st):
    sp_charlist = '[@_!#$%^&*()<>?/\|}{~:]'
    for char in st:
        if char in sp_charlist:
            return "This string contain special characters"
        else:
            continue
    return "This string doesn't have special characters"


# In[22]:


sp_st = "Hii! my name is sameer."
sp_st1 = "Hii my name is sameer"
sp_char(sp_st)

