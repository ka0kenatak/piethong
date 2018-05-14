def isIPv4Address(inputString):

    #Unit Test - verify if input is blank
    def verifyBlank(input):
        if not input:
            return False
        else:
            return True
    #Unit Test - verify if input is only numerical
    def verifyAlpha(input):
        return(input.isdigit())

    def convertArray(input):
        list=[]
        for i in input:
            list.append(i)
        return(list)

    '''a=convertArray(inputString)
    print(a)
    indices = [i for i, x in enumerate(inputString) if x == "."]
    print(indices)'''

    print(verifyAlpha(inputString))




#declarations
test1="172.16.254.1"
test2="172162541"
test3=""
test4="172.a.13.34"


#function call
isIPv4Address(test4)
