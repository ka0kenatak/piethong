def depositProfit(deposit, rate, threshold):

    balance=deposit
    count=0
    while (balance < threshold):
        balance+=balance*(rate/100)
        count+=1
        print(balance)
    return(count)

#Declarations
d1=100
r1=20
t1=170

#Function Calls
#depositProfit(d1,r1,t1)
