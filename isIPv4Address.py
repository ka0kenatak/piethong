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
        
    #Unit Test - verify input is valid octave
    def verifyLimit(input):
        x=int(input)
        if 0 <= x <= 255:
            return(True)
        else:
            return(False)


    def convertArray(input):
        list=[]
        for i in input:
            list.append(i)
        return(list)


    '''a=convertArray(inputString)
    print(a)
    indices = [i for i, x in enumerate(inputString) if x == "."]
    print(indices)'''

    print(verifyBlank(inputString))
    print(verifyAlpha(inputString))
    print(verifyLimit(inputString))


#declarations
test="172.16.254.1"
test1=""
test2="172.a.13.34"
test3="300"


#function call
isIPv4Address(test3)
