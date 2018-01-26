def almostIncreasingSequence(sequence):

    a=True
    if len(sequence) <= 2:
        return True

    def IncreasingSequence(s):
        if len(s) == 2:
            if s[0] < s[1]:
                return True
        else:
            for i in range(0, len(s)-1):
                if s[i] >= s[i+1]:
                    return False
                else:
                    pass
            return True

    for i in range (0, len(sequence) - 1):
        if sequence[i] >= sequence [i+1]:
            #Either remove the current one or the next one
            s1 = sequence[:i] + sequence[i+1:]
            s2 = sequence[:i+1] + sequence[i+2:]
            if IncreasingSequence(s1) == True:
                return True
            elif IncreasingSequence(s2) == True:
                return True
            else:
                return False
    
    
    """if(len(sequence)<2):
        return(True)
    
    for i in range(0,len(sequence)-1):
        if(sequence[i] < sequence[i+1]):
            a=True
        else:
            del sequence[i+1]
            l=len(sequence)
            f=l-1
            for i in range(0,len(sequence)-1):
                if(sequence[i] < sequence[i+1]):
                    a=True
                else:
                    a=False
                    return(a)
            return(a)
    return(a)"""
