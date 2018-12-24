def growingPlant(upSpeed, downSpeed, desiredHeight):

    height=0
    count=0
    delta=upSpeed-downSpeed
    while(height < desiredHeight):
        count+=1
        height+=delta
    print(count)

#Declarations
u1=100
d1=10
h1=910


#Function Calls
growingPlant(u1,d1,h1)
