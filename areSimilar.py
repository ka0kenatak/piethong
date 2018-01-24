'''def areSimilar(a, b):
    a.sort()
    b.sort()
    print("a=",a,"b=",b)
    if (a == b):
        return(True)
    else:
        return(False)'''

'''def areSimilar(a, b):
    i=0
    j=0
    c=False

    while(i<len(a)-1):
        if(j>2):
            c=False
            print("c=",c)
            return(c)
        else:
            print("a[",i,"]=",a[i])
            print("b[",i,"]=",b[i])
            if(a[i]==b[i]):
                c=True
                i+=1
            else:
                j+=1
                b[i],b[i+1]=b[i+1],b[i]
    print("c=",c)'''

def areSimilar(a,b):
    j=0
    x=0
    def isNotEqual(c,d):



    for i in range(len(a)):
        while(x<2):
            while(a[i]!=b[j]):
                


#declarations
mytest1=[1,2,3,4,5,6,7]
mytest2=[1,3,2,5,4,6,7]

test8a=[4, 6, 3]
test8b=[3, 4, 6]

test10a=[832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
test10b=[832, 570, 148, 998, 533, 561, 455, 147, 894, 279]

#function calls
#areSimilar(mytest1,mytest2)
areSimilar(test8a,test8b)
areSimilar(test10a,test10b)
