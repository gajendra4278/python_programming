#---------------------------------------------------------------------------------------
# Find Smallest Strings which contains all charcter 
#Some More Program          
# 
#1. Program to print the pattern ‘G’
#2. Python | Print an Inverted Star Pattern
#3. python 3 | Program to print double sided stair-case pattern
#4. Print with your own font using Python !!
#5. Python program to convert time from 12 hour to 24 hour format
#6. https://www.geeksforgeeks.org/python-programming-examples/
#---------------------------------------------------------------------------------------
import os
import sys
import re
from collections import defaultdict

def find_smallest_substr (inputString):
    #print (inputString)
    lenofInput = len(inputString)
    lenOfUnique = len(set(inputString))
    curr_dict = defaultdict(lambda:0)
    count =0
    for i in range(lenofInput):
        curr_dict[inputString[i]] += 1
        if (curr_dict[inputString[i]] ==1 ):
            count += 1
    print ("Count Number is", count )
    if (count == lenOfUnique):
        print ("Will do it in future");
    

        
        

if (__name__ == "__main__"):
    valuedString = "aabcbcdbca"
    find_smallest_substr (valuedString)