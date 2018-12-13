def arrayReplace(inputArray, elemToReplace, substitutionElem):

    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            inputArray.remove(elemToReplace)
            inputArray.insert(i,substitutionElem)
    return(inputArray)

#Declarations
a1=[1,3,1]
a2=1
a3=2

#Function calls
arrayReplace(a1, a2, a3)
