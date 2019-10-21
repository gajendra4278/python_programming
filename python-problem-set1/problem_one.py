#************************************************************************************************************
# Find out the sum of occured digit in given strings
# 1.1 ==> if two or more digit is consecutive then treat as a one digit accoring to that make addition logic
#************************************************************************************************************

import os
import re
import string
import re


def string_digit_sum (inputString):
    splitBySpace = list(inputString)
    lengthOfList = len(splitBySpace)
    #print (lengthOfList)
    numricList = []
    for x in (splitBySpace):
        if x.isdigit():
            y=int(x)
            numricList.append(y)
    print ("Sum of List is", sum(numricList))


def consecutive_add (inputString):
    splitBysequence = re.compile("[a-z]|[A-Z]").split(inputString)
    #splitBysequence = re.split(r"\c", inputString)
    #splitByEscape = inputString.split("[a-z]|[A-Z]")
    numricList = []
    for x in (splitBysequence):
        if x.isdigit():
            y=int(x)
            numricList.append(y)
    print ("Sum of List is By Using Second Condition", sum(numricList))
    

            

    


if (__name__ == "__main__"):
    valueString = '1Abc32def34jklm980'
    string_digit_sum(valueString)
    consecutive_add(valueString)