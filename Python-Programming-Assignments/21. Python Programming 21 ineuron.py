#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ques 1) Write a function that takes a list and a number as arguments. Add the number to the end of the list, 
# then remove the first element of the list. The function should then return the updated list.


# In[2]:


def next_in_line(list_:list, number:int):
    list_.append(number)
    return list_[1:]


# In[3]:


next_in_line([1,2,3], 4)


# In[4]:


# Ques 2) Create the function that takes a list of dictionaries and returns the sum of people's budgets.


# In[5]:


def get_budgets(budget_dict:list):
    return sum(person["budget"] for person in budget_dict)


# In[6]:


get_budgets([{"name": "John", "age": 21, "budget": 23000 },
{ "name": "Steve", "age": 32, "budget": 40000 },
{ "name": "Martin", "age": 16, "budget": 2700 }])


# In[7]:


# Ques 3) Create a function that takes a string and returns a string with its letters in alphabetical order.


# In[8]:


def alphabet_soup(string):
    return "".join(sorted(string))


# In[9]:


alphabet_soup("hello")


# In[10]:


alphabet_soup("hacker")


# In[11]:


# Ques 4) Suppose that you invest $10,000 for 10 years at an interest rate of 6% compounded monthly.
# What will be the value of your investment at the end of the 10 year period?
# Create a function that accepts the principal p, the term in years t, the interest rate r, and the number of compounding 
# periods per year n. 
# The function returns the value at the end of term rounded to the nearest cent.


# In[12]:


def compound_interest(p, t, r, n):
    amount = p * (1 + r/n) ** (n*t)
    return round(amount, 2)


# In[13]:


compound_interest(100, 1, 0.05, 1)


# In[14]:


compound_interest(3500, 15, 0.1, 4)


# In[15]:


# Ques 5) Write a function that takes a list of elements and returns only the integers.


# In[16]:


def return_only_integer(list_:list):
    int_list = []
    for item in list_:
        if type(item) == int:
            int_list.append(item)
    return int_list


# In[17]:


return_only_integer([9, 2, "space", "car", "lion", 16])


# In[18]:


return_only_integer(["hello", 81, "basketball", 123, "fox"])

