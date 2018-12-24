def absoluteValuesSumMinimization(a):

    temp=1000000000
    #print("a=",a)
    for x in a:
        result=0
        for i in range(len(a)):
            result+=abs(a[i]-x)
            #print("abs(",i,"-",x,")=",result)
        #print("total result with element",x,"is",result)
        if (result < temp):
            temp=result
            r=x
    #print("smallest result is with element",r)
    return(r)

#Declarations
l1=[2,4,7]

#Function Calls
#absoluteValuesSumMinimization(l1)
