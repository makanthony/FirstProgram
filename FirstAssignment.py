# -*- coding: utf-8 -*-
"""
Spyder Editor

First Assignment: sum of first 100 integers
8/15/22
Anthony Mak

"""

import numpy as np
list100 = np.linspace(1, 100, 100, dtype=int)
listSum = sum(list100)
print('List of numbers is: {}' .format(list100))
print('Sum of first 100 integers is: {}' .format(listSum))

loopSum=0
for i in range(101):
    loopSum += i
print('Sum of first 100 integers is: {}' .format(loopSum))