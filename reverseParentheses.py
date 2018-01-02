#functions definitions
#Chris' solution
def XXreverseParentheses(s):
   def flip(seq, begin, end):
       return seq[:begin]+seq[begin+1:end][::-1]+seq[end+1:]
   p_index_stack = []
   i = 0
   while i < len(s):
       if s[i] == '(':
           p_index_stack.append(i)
       elif s[i] == ')':
           s = flip(s,p_index_stack.pop(),i)
           print("s=",s)
           i -= 2
       i += 1
   return s


def reverseParentheses(s):
    if s.find('(') > 0:
        b=s.index(')')

        tmpList=[]
        a=0
        for i in range(len(s)):
            if s[i] == '(':
                tmpList.append(i)
                print(tmpList)
        a=max(tmpList)


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
        #newList.remove('(')
        #newList.remove(')')
        newList.pop(a)
        newList.pop(b-1)
        print(newList)

        z=''.join(newList)
        print("z = ",z)
        reverseParentheses(z)
    else:
        print(s)

    #print("mas is ",max(s.index(')')))


#declarations
test1="a(bc)de"
test2="a(bcdefghijkl(mno)p)q"
test3="Where are the parentheses?"
test6="abc(cba)ab(bac)c"
test7="The ((quick (brown) (fox) jumps over the lazy) dog)"


#funcation calls
#reverseParentheses(test1)
#reverseParentheses(test2)
#reverseParentheses(test3)
#XXreverseParentheses(test2)
#XXreverseParentheses(test6)
#XXreverseParentheses(test7)

#print statements
#print("test string is",test1)
print("test string is",test2)
