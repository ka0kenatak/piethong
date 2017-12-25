def test(sequence):
	print("sequence is =",sequence)
	#print("sequence[0][1] =",sequence[0][1])
	#print("sequence[1][0] =",sequence[1][0])
	print("length of sequence[0] =",len(sequence[0]))
	print("element of sequence[0][1] =",sequence[0][1])

def commonCharacterCount(s1, s2):
    com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
    return sum(com)

def isLucky(n):
	s = str(n)
	pivot = len(s)//2
	left, right = s[:pivot], s[pivot:]
	print(s)
	print(len(s))
	print(pivot)
	print(left,right)
	return sum(map(int, left)) == sum(map(int, right))

#declarations
f=open('test.txt')
num=123411
s=[[1,2,3],[4,5,6]]
array=[1]*4
array2=[]
array3=[3,4,5]
a1="abcaa"
a2="xyzbaca"

#function calls
test(s)
print(isLucky(num))

#print statements
print("f.read()=",f.read())
#uncomment to re-read lines from text.txt otherwise next methods return 0
#f.seek(0)
print("f.read()=",f.read())
print("f.readlines()=",f.readlines())
print("s=",s)
print("array1=",array)
print("array2=",array2)
print("array3 =",array3)
print("Is 1 > 3",1>3)
print("\n")
print("a1=",a1)
print("a2=",a2)
print("a1.count('a')=",a1.count('a'))
print("a2.count('x')=",a2.count('x'))
print("set(a1)=",set(a1))
print("set(a2)=",set(a2))
print("min(array3)=",min(array3))
print("min(s)=",min(s))
print("max(array3)=",max(array3))
print("max(s)=",max(s))

for i in set(a1):
	a=min(a1.count(i),a2.count(i))
	print("\na1.count(",i,")=",a1.count(i))
	print("a2.count(",i,")=",a2.count(i))
	print("min =",a)
