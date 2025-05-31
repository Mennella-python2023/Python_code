import numpy as np
from numpy.linalg import matrix_rank 
from scipy.linalg import eigvals

def jordan_block_counts_numpy(A):
    A = np.array(A, dtype=float)
    n = A.shape[0]

    eigenvalues = eigvals(A)

    eigenvalues = np.round(eigenvalues, decimals=10)

    unique, counts = np.unique(eigenvalues, return_counts=True)
    eigenvalue_info = dict(zip(unique, counts))

    print("Autovalori (lambda):")
    for val in eigenvalue_info:
        ma = eigenvalue_info[val]
        M = A - val * np.eye(n)
        mg = n - matrix_rank(M)
        print(f"lambda = {val:.4f} -> m. a. = {ma}, m. g. = {mg} -> blocchi di Jordan")

if __name__=="__main__":
    A = [[5, 4, 2],
         [0, 5, 1],
         [0, 0, 5]]

    jordan_block_counts_numpy(A)