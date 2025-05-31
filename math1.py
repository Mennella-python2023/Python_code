
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]
z = [1, 4, 8, 4, 2]

# Create a figure and a 3D axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the data
ax.plot(x, y, z, marker='o', linestyle='-', color='b', label='3D Line Graph')

# Adding labels and title
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Graph Example')
ax.legend()

# Display the graph
import matplotlib
matplotlib.use('TkAgg')  # Prova anche 'Qt5Agg' se necessario

plt.show()
