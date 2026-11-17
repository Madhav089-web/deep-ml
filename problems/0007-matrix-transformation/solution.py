import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    Tdet = np.linalg.det(T)
    Sdet = np.linalg.det(S)
    if (np.isclose(Tdet, 0)) or (np.isclose(Sdet,0)):
        return -1
    x=np.linalg.inv(np.array(T))
    transformed_matrix=np.matmul(np.matmul(x,np.array(A)),np.array(S))
    return transformed_matrix