def minesweeper(matrix):

    r=[]

    print("matrix input =", matrix)
    print("len(matrix) =", len(matrix))
    for i in range(len(matrix)):
        print("len(matrix[", i, "]) = ", len(matrix[i]))
        print("matrix",i,matrix[i])
        for j in range(len(matrix[i])):
            print(matrix[i][j])

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for x in range(-1,0,1):
                for y in range(-1,0,1):

#declarations
m1=[[True,False,False],[False,True,False],[False,False,False]]

#function calls
minesweeper(m1)
