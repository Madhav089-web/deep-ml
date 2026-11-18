def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # Your code here
    result=[]
    counter=0
    for i in matrix:
        result.append([])
        for j in i:
            result[counter].append(j*scalar)
        counter+=1
    return result
    # pass