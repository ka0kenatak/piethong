def isBeautifulString(inputString):

    count = 0
    newArray=[]
    newArray2=[]
    #instead of for loop for newArray, use this:
    newArray=[i for i in inputString]
    #for i in inputString:
    #    newArray.append(i)

    print (newArray)
    newArray2=newArray.sort()
    print (newArray2)

#Declarations
s1="abcedfg"
s2="bbbaacdafe"
s3="aabbb"

#Function calls
isBeautifulString(s2)
