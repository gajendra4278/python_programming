import os
import re
import sys



inputString = "This is my name but i am not blah blah blah.."
sampleDict = {}
for i in (inputString):
    keys = sampleDict.keys()
    values= sampleDict.values()
    if (i in keys):
        sampleDict[i] += 1  # sampleDict[i] = sampleDict[i] +1
    else:
        sampleDict[i] = 1

print (sampleDict)
#-------------------Count of Input Char From the Strings -----------------------
#count = 0 
#charValue = 'b' 
#for i in range (len(inputString)):
#    if (inputString[i] == charValue):
#        count  = count +1
#print (count)
#********************************************************************************

#----------------- We can use varibale.count("a") -------------------------------
