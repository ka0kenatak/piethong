def test(sequence):
	print("sequence is =",sequence)
	#print("sequence[0][1] =",sequence[0][1])
	#print("sequence[1][0] =",sequence[1][0])
	print("length of sequence[0] =",len(sequence[0]))
	print("element of sequence[0][1] =",sequence[0][1])


s=[[1,2,3],[4,5,6]]

array=[1]*4
print("array1=",array)

array2=[]
print("array2=",array2)

array3=[3,4,5]
print("array3 =",array3)

print("max element of array3 is",max(array3))


print("Is 1 > 3",1>3)


#f=open('/Users/fillanes/test.txt')
f=open('test.txt')
print(f.read())

f.seek(0)
print(f.readlines())

def commonCharacterCount(s1, s2):
    com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
    return sum(com)

a1="abca"
a2="xyzbac"
print("a1=",a1)
print("a2=",a2)
print(a1.count(a2))
print(a2.count(a1))
print(set(a1))
print(set(a2))
