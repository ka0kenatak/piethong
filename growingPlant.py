def growingPlant(upSpeed, downSpeed, desiredHeight):

    height=0
    count=1
    delta=upSpeed-downSpeed
    while(height+delta < desiredHeight):
        height+=upSpeed
        if(height >= desiredHeight):
            return(count)
        height-=downSpeed
        count+=1

#Declarations
u1=100
d1=10
h1=910


#Function Calls
growingPlant(u1,d1,h1)
