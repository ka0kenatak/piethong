def allLongestStrings(inputArray):

    def getLongestStringLength(sequence):
        biggestLength=0
        for i in range(len(sequence)):
            if(len(sequence[i]) >= biggestLength):
                biggestLength=len(sequence[i])
            else:
                pass
        return(biggestLength)

    if(len(inputArray)==1):
        return(inputArray)
    else:
        a=getLongestStringLength(inputArray)
        new_sequence=[]
        for i in range(len(inputArray)):
            if(len(inputArray[i])==a):
                new_sequence.append(inputArray[i])
            else:
                pass
        return(new_sequence)
