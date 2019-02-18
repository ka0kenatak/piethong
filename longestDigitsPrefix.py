def longestDigitsPrefix(inputString):

    array=[]
    newArray=[]

    for val in inputString:
        array.append(val)
    for i in array:
        if i.isdigit()==True:
            newArray.append(i)
        if i.isdigit()==False:
            newString=''.join(newArray)
            return(newString)

#Declarations
s1="123aa7"

#Function Calls
longestDigitsPrefix(s1)
