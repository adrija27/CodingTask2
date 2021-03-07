#!/usr/bin/env python
# coding: utf-8

# In[22]:


def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
a=int(input("Enter the number: "))
if a<0:
    print("Wrong Input!\nEnter a positive number! ")
else:
    for i in range(a):
        print(fib(i))

