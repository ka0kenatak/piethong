def digitDegree(n):


    newString=str(n)
    #print(newString)

    newArray=[]
    for i in newString:
        newArray.append(i)

    #print(newArray)
    newNumber=0
    for val in newArray:
        newNumber+=int(val)

    print(newNumber)

    if newNumber > 10:
        digitDegree(newNumber)
#Declarations
n1=100
n2=91

#Function Call
#digitDegree(n1)
digitDegree(n2)
