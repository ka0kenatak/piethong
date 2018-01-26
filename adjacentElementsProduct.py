def adjacentElementsProduct(inputArray):
    
    length = len(inputArray)
    f = length -1
    a=-1001
    for i in range(0,f):
        if (inputArray[i]*inputArray[i+1] > a):
            a = inputArray[i]*inputArray[i+1]
        print(a)
    return(a)
