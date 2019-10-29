
def find_duplicate_element ():
    inPutList = ["10", "20", "30", "40", "50", "10", "20", "60", "60"]
    outPutList = []
    lengthOfInputList = len(inPutList)
    for k in range(lengthOfInputList):
        j = k + 1
        for i in range (j, lengthOfInputList):
            if (inPutList[k] == inPutList[i]):
                #print (inPutList[k])
                outPutList.append(inPutList[k])
            
    
    print (outPutList)
        
def remove_duplicate_element ():
    inPutList = ["10", "20", "30", "40", "50", "10", "20", "60", "60"]
    #outputList = set (inPutList) # Removing element using set data set
    #print (outputList)
    outputList = []
    lenOfList = len(inPutList)
    for i in inPutList:
        if (i not in outputList):
            outputList.append(i)
    print (outputList)

if (__name__ == "__main__"):
    find_duplicate_element ()
    remove_duplicate_element ()