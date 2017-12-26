#functions definitions
def reverseParentheses(s):
    a,b=s.index('('),s.index(')')
    print("a and b =",a,b)

    oldString=(s[a+1:b])
    print("oldString =",oldString)

    newString=oldString[::-1]
    print("newString =",newString)

    print((s.replace(oldString,newString)))
    print("s =",s)

    '''newList=[]
    for n in newString:
        newList.append(n)
    newList.reverse()'''

    #print("newList =",newList)
    #return(s.replace(oldString,newString))


#declarations
test="a(bc)de"

#funcation calls
reverseParentheses(test)

#print statements
print("test string is",test)
