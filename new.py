def test(sequence):
	print("sequence is =",sequence)
	#print("sequence[0][1] =",sequence[0][1])
	#print("sequence[1][0] =",sequence[1][0])
	print("length of sequence[0] =",len(sequence[0]))
	print("element of sequence[0][1] =",sequence[0][1])

def commonCharacterCount(s1, s2):
    com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
    return sum(com)

#declarations
f=open('test.txt')
s=[[1,2,3],[4,5,6]]
array=[1]*4
array2=[]
array3=[3,4,5]
a1="abcaa"
a2="xyzbaca"

#print statements
print("f.read()=",f.read())
#uncomment to re-read lines from text.txt
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
