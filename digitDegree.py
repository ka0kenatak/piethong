def digitDegree(n):

    newString=str(n)

    newArray=[]
    for i in newString:
        newArray.append(i)

    newNumber=0
    for val in newArray:
        newNumber+=int(val)

    #Print Statements
    print("n=",n)
    print("newString=",newString)
    print("newArray=",newArray)
    print("newNumber = ",newNumber)

    if newNumber > 10:
        digitDegree(newNumber)


#Declarations
n1=100
n2=91
n3=10


#Function Calls
#digitDegree(n1)
digitDegree(n2)
#digitDegree(n3)
