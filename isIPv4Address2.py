def isIPv4Address(inputString):

    if inputString.find(".") == -1:
        print("this string does not have a period")
        return False
    else:
        newString=inputString.split(".")
        print(newString)
        for i in newString:
            if i.isdigit()==False:
                print("this string has letters")
                return False
            elif (int(i) < 0 or int(i) > 255):
                print("octets are invalid")
                return False
            elif (len(newString) !=4):
                print("too many octets")
                return False
        return True


#Declarations
test1="172.156.134.144"
test2="abd.dbc.sdf.234"
test3="1.1.1.1.1"
test4="300"
test5="304.124.306.305"


#Function calls
isIPv4Address(test1) #True
isIPv4Address(test2) #False
isIPv4Address(test3) #False
isIPv4Address(test4) #False
isIPv4Address(test5) #False
