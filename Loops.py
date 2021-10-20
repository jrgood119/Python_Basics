#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Basic loops

students = ["Adam", "Ben", "Charles", "David", "Emily", "Frannie", "Gloria", "Hadley"]
for name in students:
    print(name)


# In[2]:


for letter in "Kentucky":
    print(letter)


# In[3]:


for x in range(1,21):
    if x %2 == 0:
        print("{} is even".format(x))
    else:
        print("{} is odd".format(x))
        
# expanded loop
num = [1,2,20,3,4,5,6,7,8,9,10,100,11,12,13,14,15,16,25]
is_even = []
is_odd = []
greater_than_16 = []

for x in num:
    if x %2 == 0 and x < 17:
        is_even.append(x)
    elif x %2 !=0 and x < 17:
        is_odd.append(x)
    else:
        greater_than_16.append(x)

print("Even numbers are", is_even)
print("Odd numbers are", is_odd)
print("Greater than 16 numbers are", greater_than_16)


# In[4]:


i = 1
while i < 10:
    print(i)
    i += 1
    
# expanded
i = 1
while i < 10:
    print(i)
    i += 1
else:
    print("i is now greater than 9")


# In[5]:


start = 0
end = []
total = 0

while start < 100:
    start += 1
    end.append(start)

total = sum(end)
print(total)


# In[6]:


a = 10
b = 20
c = 30

if a > b and a > c:
    print("a is the greatest value")
elif a < b and a > c:
    print("b is the greatest value")
else:
    print("c is the greatest value")

