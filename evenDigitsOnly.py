def evenDigitsOnly(n):

    s=str(n)
    r=[]
    for i in s:
        r.append(int(i))

    print("value of n is",n)
    print("value of r is",r)

    for i in r:
        if i%2!=0:
            return(False)
    return(True)

#Declaration
num1=123456

#Function calls
evenDigitsOnly(num1)
