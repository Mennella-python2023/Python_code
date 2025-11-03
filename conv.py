import numpy as np
import matplotlib.pyplot as plt

# Define rectangular function
def rect(n):
    return np.where(np.abs(n) <= 0.5, 1, 0)

# Define triangular function
def tri(n):
    return np.where(np.abs(n) <= 1, 1 - np.abs(n), 0)

# Generate input array
n = np.linspace(-5, 5, 1000)

# Evaluate functions on n
x_n = rect(n)
y_n = tri(n)

# Perform convolutions with mode 'same' to keep length consistent
convxy = np.convolve(x_n, y_n, mode="same")
convxx = np.convolve(x_n, x_n, mode="same")

# Plot everything
plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.plot(n, x_n, color="b")
plt.title("rect(n)")

plt.subplot(4, 1, 2)
plt.plot(n, y_n, color="g")
plt.title("tri(n)")

plt.subplot(4, 1, 3)
plt.plot(n, convxy, color="r")
plt.title("Convolution of rect(n) and tri(n)")

plt.subplot(4, 1, 4)
plt.plot(n, convxx, color="m")
plt.title("Convolution of rect(n) with itself")

plt.tight_layout()
plt.show()
