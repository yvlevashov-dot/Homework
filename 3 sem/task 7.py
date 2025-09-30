import numpy as np
def lin_eq(N,M):
    mat = np.zeros((N, M))
    for i in range(N):
        mat[i,0:M]=input().split()
    coef = mat[0:N,0:M-1]
    end = mat[0:N,M-1:M]

    print(np.linalg.solve(coef,end))
N,M=map(int,input().split())
lin_eq(N,M)