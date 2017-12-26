#functions definitions
def reverseParentheses(s):
    a,b=s.index('('),s.index(')')
    print(a,b)
    newString=(s[a+1:b])
    newList=[]
    for n in newString:
        newList.append(n)
    newList.reverse()
    print(newList)
    return(newString)


#declarations
test="a(bc)de"

#funcation calls
print(reverseParentheses(test))

#print statements
print("test string is",test)
