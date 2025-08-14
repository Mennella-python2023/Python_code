
import numpy as np

# Definizione matrici |1>, |2>, |3>
m1 = np.array([[0, 1],
               [0, 0]])

m2 = np.array([[1, 1],
               [0, 1]])

m3 = np.array([[-2, -1],
               [0, -2]])

# Convertiamo ogni matrice in vettore colonna (flatten) per lavorare in R^4
v1 = m1.flatten()
v2 = m2.flatten()
v3 = m3.flatten()

# Mettiamo i vettori come colonne in una matrice 4x3
M = np.column_stack([v1, v2, v3])

# Calcoliamo il rango della matrice M
rank = np.linalg.matrix_rank(M)

print(f"Rango della matrice formata dai vettori: {rank}")

# Se rango = numero di vettori (3), sono indipendenti
if rank == M.shape[1]:
    print("Le matrici sono linearmente indipendenti.")
else:
    print("Le matrici sono linearmente dipendenti.")
