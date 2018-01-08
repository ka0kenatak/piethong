def addBorder(picture):
    #z=[""]*(len(picture[0])+2)
    for i in picture:
        picture.insert("*",0)
        picture.insert("*",-1)
    print("picture=",picture)
    #return(picture)



#declarations
test1=["abc","ded"]
test2=["a"]


#function calls
addBorder(test1)
addBorder(test2)
