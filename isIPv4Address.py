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

    #split up the octets
    def separateOctets(input):
        return()
    #Unit Test - verify input is valid octets
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


    a=convertArray(inputString)
    print(a)
    indices = [i for i, x in enumerate(inputString) if x == "."]
    print(indices)

    #print(verifyBlank(inputString))
    #print(verifyAlpha(inputString))
    #print(verifyLimit(inputString))


#declarations
test="172.16.254.1"
test2=""
test3="172.a.13.34"
test4="300"


#function call
isIPv4Address(test)
#isIPv4Address(tes2)
#isIPv4Address(tes3)
#isIPv4Address(tes4)
