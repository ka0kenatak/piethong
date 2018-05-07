def checkPalindrome(inputString):
    length = len(inputString)
    x = int(length/2)
    if length/2 == int(length/2):
        #if inputString[:x] == inputString[x:length]:
        #    return (True)
        if inputString[:x] == inputString[:x-1:-1]:
            return (True)
        else:
            return(False)
    else:
        #if inputString[:x] == inputString[x+1:length]:
        #    return (True)
        if inputString[:x] == inputString[:x:-1]:
            return (True)
        else:
            return(False)
