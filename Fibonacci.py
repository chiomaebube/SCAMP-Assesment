# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 01:33:51 2020

@author: USER
"""


number = int(input("Enter number: "))
#number = X
#n = number


def fibonacci(number):
    if number <= 1:
        return number
    else:
        result = (number - 1) + (number - 2)
        return result


for i in range(number):
    print(fibonacci(i))