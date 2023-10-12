def search_replace(my_list, search, replace):
    new_matrix = []
    for row in matrix:
        result = list(map(lambda x: x**2, row))
        new_matrix.append(result)
    return new_matrix
