def areSimilar(a, b):
    a.sort()
    b.sort()
    print("a=",a,"b=",b)
    if (a == b):
        return(True)
    else:
        return(False)



#declarations
test8a=[4, 6, 3]
test8b=[3, 4, 6]

test10a=[832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
test10b=[832, 570, 148, 998, 533, 561, 455, 147, 894, 279]

#function calls
areSimilar(test8a,test8b)
areSimilar(test10a,test10b)
