def arrayChange(inputArray):
    x, array = inputArray, 0
    for i in range(len(x)-1):
        a,b = x[i], x[i+1]
        if a >= b:
            array += a + 1 - b
            x[i+1] = a + 1
    return array
