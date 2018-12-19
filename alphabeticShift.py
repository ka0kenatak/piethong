def alphabeticShift(inputString):


    #for val in inputString:
    for i in range(len(inputString)):
        print("val is",inputString[i])
        #print("val is",val)
        #print("ASCII is",ord(val)+1)
        #print("new letter",chr(ord(val)+1))
        #inputString=inputString.replace(val,chr(ord(val)+1),1)
        inputString[i]='a'
        print(inputString)

    print(inputString)

#Declarations
str1="abcdef"


#Functional calls
alphabeticShift(str1)
