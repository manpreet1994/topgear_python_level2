#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 18:14:33 2020

@author: manpreet
"""

from functools import reduce

numerals = { 'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1 }
def program3(s):
        return reduce(lambda x, y: -x + y if x < y else x + y, map(lambda x: numerals.get(x, 0), s.upper()))
    
    
print("convert the given roman number in to decimal number.")

print("Enter roman number = ")
roman = input()

print("output in decimal = ", program3(roman))
    
    
