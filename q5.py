#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:16:54 2020

@author: manpreet
python assignment level 2



Level 2 assignment:
-------------------

program 1:

write a python program using regex or by any other method to check
if the credit card number given is valid or invalid. your python program should read the credit card number from input

A valid credit card number from xyz Bank has the following rules

It must start with 3,4,5
It must contain exactly 16 digits
It must only consist of digits (0-9)
It may have digits in groups of , separated by one hyphen "-"
It must NOT use any other separator like ' ' , '_', etc
It must NOT have 4 or more consecutive repeated digits

Examples:
input: 
4253625879615786
output:
valid

input:
5122-2368-7954-3214
output:
valid

input:
42536258796157867  
output: 
invalid -  #17 digits in card number is not allowed

input:
4424444424442444   
output: 
invalid #Consecutive digits are repeating 4 or more times not allowed

input:
5122-2368-7954 - 3214   
output:
invalid:  #Separators other than '-' not allowed




program 2:

write a python program to output the following 
look and say sequence of numbers. It should print
up to 10 numbers

1
11
21
1211
111221
312211
13112221
1113213211
31131211131221



program 3

convert the given roman number in to decimal number.
The syntax of roman number is given below
write the python program using functools

I   1
V   5
X   10
L   50
C   100
D   500
M   1000

example:
input: XL
output: 40


program 4

write a python proram to count the occurences of string two in 
string one. your python program should read the strings from input

example:
input:
stringone = "KSCDCDC"
stringtwo = "CDC"
output: 2


program 5

write a python program to reverse the words in a given sentence as given below. your python program should read the sentence from input

example:
input:    "python programming is awesome"
output:   "awesome is programming python"





"""
def program5(inputstring): 

    temp_list = inputstring.split(" ")
    temp_list = list(reversed(temp_list))
    
    return temp_list

print("write a python program to reverse the words in a given sentence as given below. your python program should read the sentence from input")
print("Enter your string :")
inputstr = input()
print("output = ",program5(inputstr))

