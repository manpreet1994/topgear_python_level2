#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:18:13 2020

@author: manpreet
"""

import re

def check_consecutive(credit_card_no):
    valid = True
    
    if credit_card_no.find("-") == -1:
        for x in range(len(credit_card_no)-3):
            for r in range(1,4):
                if credit_card_no[x]==credit_card_no[x+r]:
                    valid= False
                    break
        
        return valid
    
    else:
        return check_consecutive(credit_card_no.replace("-",""))
        
def program1(credit_card_no):
    regex_patt = "^[3+4+5][0-9]{3}-*[0-9]{4}-*[0-9]{4}-*[0-9]{4}$"
    x = re.findall(regex_patt, credit_card_no)
    if len(x)>0:
        return "valid" if check_consecutive(credit_card_no) else "invalid"
    else:
        return "invalid"
    

print ("""write a python program using regex or by any other method to check \n if the credit card number given is valid or invalid. your python program should read the credit card number from input \n A valid credit card number from xyz Bank has the following rules \n It must start with 3,4,5 \n It must contain exactly 16 digits \n It must only consist of digits (0-9) \n It may have digits in groups of , separated by one hyphen "-" \n It must NOT use any other separator like ' ' , '_', etc \n It must NOT have 4 or more consecutive repeated digits""")

print ("\n Enter a credit card number")
creditno = input()
print(program1(creditno))