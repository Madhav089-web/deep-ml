import math
def determinant(matrix:list[list[float|int]]):
    ...
    return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
def trace(matrix:list[list[float|int]]):
    ...
    return matrix[0][0]+matrix[1][1]
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    Trace=trace(matrix)
    dete=determinant(matrix)
    lambda1,lambda2=(Trace+((math.sqrt((Trace**2)-4*1*dete))))/(2*1),(Trace-((math.sqrt((Trace**2)-4*1*dete))))/(2*1)
    eigenvalues=[lambda1,lambda2]

    return eigenvalues