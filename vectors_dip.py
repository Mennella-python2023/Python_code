
import matplotlib.pyplot as plt

import numpy as np
import matplotlib
import matplotlib
matplotlib.use('TkAgg')  # forza una finestra grafica


# (Opzionale) Forza una backend grafica se plt.show() non funziona
# matplotlib.use('TkAgg')

# Definizione dei vettori
v1 = np.array([1, 0])   # |1⟩
v2 = np.array([0, 1])   # |2⟩
v3 = 2 * v1 + 3 * v2    # |3⟩ = 2|1⟩ + 3|2⟩

origin = np.array([0, 0])

# Punto P: 2 * |1⟩
P = 2 * v1

# Setup grafico
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.grid(True)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)

# Disegna i vettori
def draw_vector(start, vec, color, label):
    ax.quiver(*start, *vec, angles='xy', scale_units='xy', scale=1, color=color, label=label)

draw_vector(origin, v1, 'blue', '|1⟩')
draw_vector(origin, v2, 'green', '|2⟩')
draw_vector(origin, v3, 'red', '|3⟩ = 2|1⟩ + 3|2⟩')

# Linea antiparallela a |2⟩ dalla punta di |3⟩
end_antiparallel = v3 - 4 * v2
ax.plot([v3[0], end_antiparallel[0]], [v3[1], end_antiparallel[1]], 'r--', label='Antiparallela a |2⟩ da |3⟩')

# Linea da origine a |1⟩ (rappresenta asse |1⟩)
ax.plot([origin[0], v1[0]*3], [origin[1], v1[1]*3], 'b--', label='Direzione |1⟩')

# Punto P
ax.plot(P[0], P[1], 'ko', label='P (2 × |1⟩)')
ax.text(P[0] + 0.1, P[1] + 0.1, 'P', fontsize=12)

# Impostazioni assi
ax.set_xlim(-1, 4)
ax.set_ylim(-1, 5)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Visualizzazione di |3⟩ come combinazione di |1⟩ e |2⟩")
plt.legend()
plt.tight_layout()
plt.show()
