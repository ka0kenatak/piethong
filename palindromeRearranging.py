def palindromeRearranging(inputString):
    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1



#declarations
test1="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"

#function calls
palindromeRearranging(test1)
