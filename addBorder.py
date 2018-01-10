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

    z=["*"*(len(picture[0]))]*(len(picture)+2)

    for n in picture:
    #z.insert(1,picture[0])
        z.append(n)

    print("picture=",picture)
    print("z = ",z)


#declarations
test1=["abc","ded"]
test2=["a"]
test3=["abc","def","ghi","jkl"]


#function calls
addBorder(test1)
#addBorder(test2)
#addBorder(test3)
