def arrayChange(inputArray):
    #compare x[i] to x[i+1].
    #If x[i] < x[i+1], pass.
    #Else, ???? the difference x[i]+?-x[i+1].  Add ????
    #difference to total and ???? set x[i+1] ?? x[i]+1
    x, var = inputArray, 0
    for i in range(len(x)-1):
        a,b = x[i], x[i+1]
        if a >= b:
            var += a + 1 - b
            x[i+1] = a + 1
    return var
