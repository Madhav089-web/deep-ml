import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    # res=np.linalg.solve(A,b)
   x=np.zeros_like(b,dtype=np.float32)
   d=np.diag(A)
   r=A-np.diagflat(d)
   for _ in range(n):
    x=(b-np.dot(r,x))/d
   return np.round(x,4).tolist()