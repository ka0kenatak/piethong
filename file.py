#functions definitions
def reverseParentheses(s):
    a,b=s.index('('),s.index(')')
    print("a and b =",a,b)

    oldString=(s[a+1:b])
    print("oldString =",oldString)

    newString=oldString[::-1]
    print("newString =",newString)

    returnString=s.replace(oldString,newString)
    print("returnString =",returnString)

    newList=[]
    for n in returnString:
        newList.append(n)
    newList.remove('(')
    newList.remove(')')
    print(newList)

    z=''.join(newList)
    print(z)


#declarations
test="a(bc)de"

#funcation calls
reverseParentheses(test)

#print statements
print("test string is",test)
