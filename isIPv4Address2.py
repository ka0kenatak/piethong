def isIPv4Address(inputString):

    if inputString.find(".") == -1:
        print("this string does not have a period")
        return False
    else:
        print("this string has a period")
        newString=inputString.split(".")
        print(newString)
        for i in newString:
            if i.isdigit()==True
            print("this string has a letter")
                return False
        return True


#Declarations
test1="172.156.134.144"
test2="abd.dbc.sdf.234"
test3="1.1.1.1.1"
test4="300"


#Function calls
isIPv4Address(test2)
