def addBorder(picture):

    def insertAsterisk(string):
        seq=[]
        for n in string:
            seq.append(n)
        seq.insert(0,"*")
        seq.append("*")
        string=''.join(seq)
        return(string)

    for i in range(len(picture)):
        picture[i]=insertAsterisk(picture[i])

    #z=["*"*(len(picture[0]))]*(len(picture)+2)
    picture.insert(0,"*"*(len(picture[0])))
    picture.append("*"*(len(picture[0])))

    print("picture=",picture)


#declarations
test1=["abc","ded"]
test2=["a"]
test3=["abc","def","ghi","jkl"]


#function calls
addBorder(test1)
#addBorder(test2)
#addBorder(test3)
