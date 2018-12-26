def knapsackLight(value1, weight1, value2, weight2, maxW):

    maxValue=0
    remainingWeight=0
    if (weight1+weight2<=maxW):
        return(value1+value2)
    elif (weight1 > maxW and weight2 > maxW):
        return(0)
    elif (weight1 > maxW):
        return(value2)
    elif (weight2 > maxW):
        return(value1)
    elif (value1 > value2):
        return(value1)
    return(value2)


#Declarations
v1=10
w1=5
v2=6
w2=3
mw=8

#Function Calls
knapsackLight(v1,w1,v2,w2,mw)
