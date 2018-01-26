def sortByHeight(a):
	trees=[]
	newList=[]
	for i in range(len(a)):
		if a[i]==-1:
			trees.append(i)
		else:
			newList.append(a[i])
	newList.sort()
	for n in trees:
		newList.insert(n,-1)
	return(newList)
