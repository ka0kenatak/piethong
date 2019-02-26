def digitDegree(n):

    count=0
    while (n > 10):
        count+=1
        newString=str(n)

        newArray=[]
        for i in newString:
            newArray.append(i)

        newNumber=0
        for val in newString:
            newNumber+=int(val)

    #Print Statements
        print("n=",n)
        print("newString=",newString)
        print("newArray=",newArray)
        print("newNumber=",newNumber)

        if newNumber > 9:
            count+=1
            #digitDegree(newNumber)
            #return(count)
            print(newNumber)
            print(count)

        print("count is",count)
        return(count)

    print("count is",count)
    return(count)
#Declarations
n1=5
n2=100
n3=91
n4=99

#Function Calls
#digitDegree(n1)
#digitDegree(n2)
#digitDegree(n3)
#digitDegree(n4)
