def longestDigitsPrefix(inputString):

    array=[]
    if (inputString[0].isalpha==True or inputString[0]==" "):
        newString=''.join(array)
        print(newString)
        return(newString)
    for val in inputString:
        print(type(val))
        while(val.isdigit==True):
            array.append(val)
            print(array)
    print(array)

#Declarations
s1="123aa1"

#Function Calls
longestDigitsPrefix(s1)
