def extractEachKth(inputArray, k):

    count=0
    newArray=[]
    for i in range(len(inputArray)):
        count+=1
        if (count%k!=0):
            newArray.append(inputArray[i])
    return(newArray)


#Declarations
l1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k1=3
#Function Calls
extractEachKth(l1,k1)
