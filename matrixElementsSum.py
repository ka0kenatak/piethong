def matrixElementsSum(matrix):
    sumOfElements = 0
    #creates indicator array of 1s equal to len(matrix[0])
    previousZeroDetected = [1]*len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            #this line remembers if previous row had a 0
            sumOfElements += previousZeroDetected[j]*matrix[i][j]
            print("sumOfElements in for loop is",sumOfElements)
            if matrix[i][j] == 0:
                #updates indicator arrays to 0 where 0 was found 
                previousZeroDetected[j] = 0
    return sumOfElements
