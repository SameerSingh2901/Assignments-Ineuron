#!/usr/bin/env python
# coding: utf-8

# Question 1)
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# 
# Following are the fixed values of C and H:
# C is 50. H is 30.
# 
# D is the variable whose values should be input to your program in a comma-separated
# sequence.

# In[1]:


import math

# Function to calculate Q
def calculate_Q(D):
    C = 50
    H = 30
    Q = math.sqrt((2 * C * D) / H)
    return Q

# getting input of comma-separated values
D_values = input("Enter comma-separated sequence of D values: ").split(",")

# Calculate and print Q for each D value
for D in D_values:
    D = float(D.strip())
    Q = calculate_Q(D)
    print(f"The value of Q for D = {D} is {Q}")


# Question 2:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
# element value in the i-th row and j-th column of the array should be i*j.
# 
# Note: i=0,1.., X-1; j=0,1,Y-1.

# In[2]:


# Get input values for X and Y
X = int(input("Enter the value for X: "))
Y = int(input("Enter the value for Y: "))

# Initialize the 2-dimensional array
array = [[0 for j in range(Y)] for i in range(X)]

# Populate the array using the formula i*j
for i in range(X):
    for j in range(Y):
        array[i][j] = i * j

# Print the array
for row in array:
    print(row)


# Question 3:
# Write a program that accepts a comma separated sequence of words as input and prints the
# words in a comma-separated sequence after sorting them alphabetically.

# In[3]:


# Get input sequence of words
word_sequence = input("Enter a comma-separated sequence of words: ")

# Split the words and remove leading/trailing whitespaces
words = [word for word in word_sequence.split(",")]

# Sort the words alphabetically
sorted_words = sorted(words)

# Print the sorted words in a comma-separated sequence
sorted_sequence = ", ".join(sorted_words)
print("Sorted sequence of words:", sorted_sequence)


# Question 4:
# Write a program that accepts a sequence of whitespace separated words as input and prints
# the words after removing all duplicate words and sorting them alphanumerically.

# In[4]:


# Get input sequence of words
word_sequence = input("Enter a whitespace-separated sequence of words: ")

# Split the words and remove leading/trailing whitespaces
words = word_sequence.split()

# Remove duplicate words
unique_words = list(set(words))

# Sort the unique words alphanumerically
sorted_words = sorted(unique_words)

# Print the sorted words
print("Sorted sequence of words:", " ".join(sorted_words))


# Question 5:
# Write a program that accepts a sentence and calculate the number of letters and digits.

# In[5]:


sentence = input("Enter a sentence: ")

letter_count = 0
digit_count = 0

for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print("Number of letters:", letter_count)
print("Number of digits:", digit_count)


# Question 6:
# A website requires the users to input username and password to register. Write a program to
# check the validity of password input by users.
# 
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
#                               
# Your program should accept a sequence of comma separated passwords and will check them
# according to the above criteria. Passwords that match the criteria are to be printed, each
# separated by a comma.

# In[6]:


import re

# Function to check password validity
def check_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[$#@]", password):
        return False
    return True

# Get input sequence of passwords
passwords = input("Enter a comma-separated sequence of passwords: ").split(",")

# Check and print valid passwords
valid_passwords = [password for password in passwords if check_password(password)]
valid_passwords_str = ", ".join(valid_passwords)
print("Valid passwords:", valid_passwords_str)

