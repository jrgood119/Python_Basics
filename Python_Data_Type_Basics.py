#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python Basics

# String
Name = "JT"

# Integer
Age = 28

# Float
Height = 70.5

# List
Suits = ["gray", "blue", "navy"]

# Tuple
Distance = (1.2,2.8,2.0,3.1,1.7,2.0)

# Dictionary
Schooling = {"MBA": "WGU", "Bachelors": "Park University", "Associates": "Air University"}

# Boolean
Male = True


# In[2]:


# Formatted print
print(f"My name is {Name} and I am {Age} years old.\nI stand {Height} inches tall.")


# In[3]:


# Strings
# Disignated with '' or ""

S = "Brutus is a chocolate lab"

# Can be indexed

print(S[5])
print(S[0:22:2])
lab = S.index("lab")
print(lab)

# Convert to upper or lowercase

U = S.upper()
C = S.lower()
print(U)
print(C)


# In[4]:


# Integer and Float
# Integers are whole numbers, flumbers utilize decimal points

Day = 15
Tomorrow = 16
Friday = 17
Time = 12.5
One_Hour = 13.5
Two_Hour = 14.5

# Can be used to compare

Comp = Day > Tomorrow
Compare = One_Hour == Two_Hour
print(Comp)
print(Compare)

# Can be used with math

Result = Day + Friday
Watch = Time * One_Hour
print(Result)
print(Watch)


# In[5]:


# Lists
# Can use strings, integers, floats, booleans, tuples, dictionaries

Example = ["Apple", 1, 4.7, False, ("Yes", "No"), {"Name": "Man"}]
print(Example)

# Can be appendeded and popped

L = [1,11,2,22,3,33,4,44,5,55,6,66,7,77,8,88,9]
L.append(99)
print(L)
L.pop(8)
print(L)

# Can be indexed

print(L[1:4])

# Can be copied

M = L.copy()
print(M)


# In[6]:


# Tuple
# Immutable

Client1 = ("ABCD", 12345, "Lake Example, USA")
Client2 = ("ZYX", 9876, "Somewhere Else, USA")
print(Client1)


# In[7]:


# Dictionary
# Presented in key:value pairs and can be reffered to by key name

Player = {"Name": "Chase Claypool", "Team": "Pittsburgh Steelers", "Position": "Wide Receiver", "College": "Notre Dame"}
print(Player)
print(Player["College"])


# In[8]:


# Boolean
# True or False

A = 15
B = 50

if B > A:
    print("B is greater than A")
else:
    print("A is greater than B")

