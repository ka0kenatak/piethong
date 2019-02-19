def longestDigitsPrefix(inputString):

    array=[]
    newArray=[]
    count=0

    for val in inputString:
        array.append(val)

    for i in array:
        count+=1
        print("count=",count)
        print(len(array))
        if i.isdigit()==True:
            newArray.append(i)
        if (i.isdigit()==False or count==len(array)):
            newString=''.join(newArray)
            return(newString)

#Declarations
s1="123aa7"
s2="0123456789"

#Function Calls
#longestDigitsPrefix(s1)
longestDigitsPrefix(s2)
