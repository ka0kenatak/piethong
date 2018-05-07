def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if(max(yourLeft,yourRight)==max(friendsLeft,friendsRight) and min(yourLeft,yourRight)==min(friendsLeft,friendsRight)):
        return(True)
    else:
        return(False)


#declarations
test1a=10
test1b=15
test1c=10
test1d=15



#function calls
areEquallyStrong(test1a,test1b,test1c,test1d)
