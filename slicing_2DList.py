ROW = 4
COL = 4

#set size of matrix

def slicing_2DList(matrix):
    row = len(matrix)
    col = len(matrix[0])
    
    
    for i in range(row - ROW + 1):
        for j in range(col - COL + 1):
            matrix_tmp = matrix[i:i+ROW]

            matrix_sliced = list()
            for l in range(len(matrix_tmp)):
                matrix_sliced.append((matrix_tmp[l])[j:j+COL])
    
    return matrix_sliced
    
