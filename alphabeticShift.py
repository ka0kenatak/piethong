def alphabeticShift(inputString):

    newArray=[]
    for val in inputString:
        print("val is",val)
        newArray.append((chr(ord(val)+1)))
    newString=''.join(newArray)
    print(newString)

    newString2=newString.replace("{","a")
    return(newString2)

#Declarations
str1="abcdefz"


#Functional calls
alphabeticShift(str1)
