def minesweeper(matrix):
    print("matrix input =", matrix)
    print("len(matrix) =", len(matrix))
    for i in range(0,len(matrix)):
        print("len(matrix[", i, "]) = ", len(matrix[i]))
        print("matrix",i,matrix[i])
        for j in range(0,len(matrix[i])):
            print(matrix[i][j])


#declarations
m1=[[True,False,False],[False,True,False],[False,False,False]]

#function calls
minesweeper(m1)
