def isIPv4Address(inputString):

    indices = [i for i, x in enumerate(inputString) if x == "."]

    print(indices)





#declarations
test1="172.16.254.1"

#function call
isIPv4Address(test1)
