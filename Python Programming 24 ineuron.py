#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ques 1) Create a function that takes an integer and returns a list from 1 to the given number, where:
# 1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
# 2. If the number cannot be divided evenly by 4, simply return the number.


# In[2]:


def amplifier(integer):
    num_list = []
    if integer >= 1:
        for i in range(1, integer+1):
            [num_list.append(i*10) if i%4 == 0 else num_list.append(i)]
    return num_list


# In[3]:


amplifier(4)


# In[4]:


amplifier(3)


# In[5]:


amplifier(25)


# In[6]:


# Ques 2) Create a function that takes a list of numbers and return the number that&#39;s unique.


# In[7]:


def unique(num_list):
    num_count = {}
    for num in num_list:
        num_count[num] = num_count.get(num, 0) + 1

    for num, count in num_count.items():
        if count == 1:
            return num


# In[8]:


unique([3, 3, 3, 7, 3, 3])


# In[9]:


unique([0, 0, 0.77, 0, 0])


# In[10]:


unique([0, 1, 1, 1, 1, 1, 1, 1])


# In[11]:


# Ques 3) Your task is to create a Circle constructor that creates a circle with a radius provided by an argument. 
# The circles constructed must have two getters getArea() (PIr^2) and getPerimeter() (2PI*r) which give both respective 
# areas and perimeter (circumference).
# For help with this class, I have provided you with a Rectangle constructor which you can use as a base example.


# In[12]:


import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return round(math.pi * self.radius ** 2)

    def getPerimeter(self):
        return round(2 * math.pi * self.radius)


# In[13]:


circle = Circle(11)


# In[14]:


circle.getArea()


# In[15]:


circy = Circle(4.44)
circy.getPerimeter()


# In[16]:


# Ques 4) Create a function that takes a list of strings and return a list, sorted from shortest to longest.


# In[17]:


list1 = ['asam', 'ash', 'kdjkk']


# In[18]:


type(list1[1])


# In[19]:


def sort_by_length(str_list):
    for item in str_list:
        if type(item) != str:
            raise ValueError("Elements of list should be string")            
    return sorted(str_list, key=len)


# In[20]:


sort_by_length(["Google", "Apple", "Microsoft"])


# In[21]:


sort_by_length(['Leonardo', 'Michelangelo', 'Raphel', 'Donatello'])


# In[22]:


sort_by_length(['Turing', 'Einstein', 'Jung'])


# In[23]:


# Ques 5) Create a function that validates whether three given integers form a Pythagorean triplet. 
# The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.


# In[24]:


def is_triplet(num1, num2, num3):
    num1, num2, num3 = sorted([num1, num2, num3])
    return num1**2 + num2**2 == num3**2


# In[25]:


is_triplet(3,4,5)


# In[26]:


is_triplet(13,5,12)


# In[27]:


is_triplet(1,2,3)

