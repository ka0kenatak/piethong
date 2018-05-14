def isIPv4Address(inputString):

    def convertArray(input):
        list=[]
        for i in input:
            list.append(i)
        return(list)

    #unit tests
    def unitTest1(input):
        if not input:
            return False
        else:
            return True


    a=[]
    a=convertArray(inputString)
    print(a)
    indices = [i for i, x in enumerate(inputString) if x == "."]
    print(indices)





#declarations
test1="172.16.254.1"
test2="172162541"
test3=""


#function call
isIPv4Address(test3)
