
import numpy as np
from scipy.linalg import null_space

# Definizione matrici |1>, |2>, |3>
m1 = np.array([[0, 1],
               [0, 0]])

m2 = np.array([[1, 1],
               [0, 1]])

m3 = np.array([[-2, -1],
               [0, -2]])

# Flatten matrici in vettori colonna
v1 = m1.flatten()
v2 = m2.flatten()
v3 = m3.flatten()

# Matrice 4x3
M = np.column_stack([v1, v2, v3])

# Calcola il null space (nucleo) di M: soluzioni di Mx=0
ns = null_space(M)

if ns.size == 0:
    print("Non ci sono soluzioni non banali: i vettori sono indipendenti.")
else:
    print("Soluzioni non banali trovate nel null space:")
    # ns è una matrice con vettori base del nucleo (qui di dimensione 1)
    sol = ns[:,0]
    # Normalizziamo per rendere il primo coefficiente pari a 1 (se non zero)
    sol = sol / sol[0]
    a, b, c = sol
    print(f"a = {a:.3f}, b = {b:.3f}, c = {c:.3f}")
    # Verifica combinazione
    comb = a * v1 + b * v2 + c * v3
    print(f"Combinazione lineare = {comb}")
