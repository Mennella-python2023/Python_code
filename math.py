import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]  # Reduced to 5 elements to match the length of y
y = [2, 3, 5, 7, 11]

plt.plot(x, y)
print('Created plot')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Sample Line Plot')

plt.grid(True)

plt.show()
print('Hello world')
