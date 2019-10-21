#**********************************************************************
# Find out the sum of occured digit in given strings
#**********************************************************************

import os
import re
import string


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

            

    


if (__name__ == "__main__"):
    valueString = '1Abc32def34jklm980'
    string_digit_sum(valueString)