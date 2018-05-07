def arrayMaximalAdjacentDifference(inputArray):
    m=0
    for i in range(len(inputArray)-1):
        if(abs(inputArray[i]-inputArray[i+1])>m):
            m=abs(inputArray[i]-inputArray[i+1])
    return(m)
