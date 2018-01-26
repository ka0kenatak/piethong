def commonCharacterCount(s1, s2):
    
    def convertStringToList(string):
        sequence=[]
        for i in range(len(string)):
            sequence.append(string[i])
        sequence.sort()
        return(sequence)
    
    
    new_s1=convertStringToList(s1)
    new_s2=convertStringToList(s2)
    
    l=0
    s=0
    if(len(new_s2) > len(new_s1)):
        tmp=new_s1
        new_s1=new_s2
        new_s2=tmp
    
    print("new_s1=",new_s1,"\nnew_s2=",new_s2)

    l=len(new_s1)
    s=len(new_s2)
    
    count=0
    for i in range(l):
        for j in range(s):
            if(new_s1[i]==new_s2[j]):
                print("new_s1[",i,"]=",new_s1[i],"\nnew_s2[",j,"]=",new_s2[j])
                count+=1
                new_s2[j]=0
                new_s1[i]=1
                #print(new_s1[i],new_s2[j])
            else:
                pass
    return(count)
