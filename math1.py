import matplotlib.pyplot as plt

# Dati di esempio
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]
z = [1, 4, 8, 4, 2]

# Crea la figura e l'asse 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Grafico 3D
ax.plot(x, y, z, marker='o', linestyle='-', color='b', label='3D Line Graph')

# Etichette e titolo
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Graph Example')
ax.legend()

# Mostra il grafico
plt.show()
