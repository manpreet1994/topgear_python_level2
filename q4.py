#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 12:44:27 2020

@author: manpreet
"""

def custom_counter(str1, str2):
    counter=0
    for curr_cursor in range(len(str1)):
        for y in range(len(str2)):
            if str2[y] == str1[curr_cursor]:
                if str2 == str1[curr_cursor:curr_cursor+len(str2)]:
                    counter+=1
            else:
                break
    return counter
    

def program4(inputstr1, inputstr2):
    if len(str2)>len(str1):
        return 0
    else:
        return custom_counter(inputstr1, inputstr2)


print("write a python proram to count the occurences of string two in string one. your python program should read the strings from input example:"
+ "\n input:"
+'\n stringone = "KSCDCDC"'
+'\n stringtwo = "CDC"'
+'\n output: 2")')

print("Enter string one: ")
str1 = input()

print("Entered string two: ")
str2 = input()

print("Count of occurance of str2 in str1 is ", program4(str1, str2))


#counter = 0
#str1 = "ABCDEFEFEFEFE"
#str2 = "EFE"
#
#if len(str2)<= len(str1):
#    pass
#
#
#for curr_cursor in range(len(str1)):
#    for y in range(len(str2)):
#        if str2[y] == str1[curr_cursor]:
#            if str2 == str1[curr_cursor:curr_cursor+len(str2)]:
#                counter+=1
#        else:
#            break
#            
   
        