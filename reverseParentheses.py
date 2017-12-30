#functions definitions
def reverseParentheses(s):
    if s.find('(') > 0:
        a,b=s.index('('),s.index(')')
    else:
        return(s)

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
test1="a(bc)de"
test2="a(bcdefghijkl(mno)p)q"
test3="Where are the parentheses?"

#funcation calls
#reverseParentheses(test1)
reverseParentheses(test2)
#reverseParentheses(test3)


#print statements
#print("test string is",test1)
print("test string is",test2)
