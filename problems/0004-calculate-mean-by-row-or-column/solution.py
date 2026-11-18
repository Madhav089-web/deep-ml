def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode=="column":
        ...
        r=len(matrix)
        c=len(matrix[0])
        means=[]
        for i in range(c):
            sum=0
            for j in range(r):
                sum+=matrix[j][i]
            means.append(sum/r)
    if mode=="row":
        ...
        r=len(matrix)
        c=len(matrix[0])
        means=[]
        for i in range(r):
            sum=0
            for j in range(c):
                sum+=matrix[i][j]
            means.append(sum/c)

    return means