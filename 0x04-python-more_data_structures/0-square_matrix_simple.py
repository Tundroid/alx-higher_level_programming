def square_matrix_simple(matrix=[]):
    #return [[elem**2 for elem in row] for row in matrix]
    new_matrix = []
    for row in matrix:
        result = list(map(lambda x: x**2, row))
        new_matrix.append(result)
    return new_matrix
