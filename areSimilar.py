'''def areSimilar(a, b):
    a.sort()
    b.sort()
    print("a=",a,"b=",b)
    if (a == b):
        return(True)
    else:
        return(False)'''


def areSimilar(a, b):

    left = None
    right = None
    isSim=True
    counter=0
    for i in range(len(a)):
        if a[i] != b[i]:
            counter+=1
        else:
            continue
        if counter==1:
            left = a[i]
            right = b[i]
        elif counter==2:
            if left == b[i] and right == a[i]:
                continue
            else:
                return False
        elif counter > 2:
            isSim=False
            break
    return isSim


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
