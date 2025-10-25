import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 1, 400)
y = x**2 + 2*x
y = x**2 - 2*x

plt.fill_between(x, y1, y2, where=(x <= 0), color='lightblue', alpha=0.6, label='Dominio')

plt.plot(x, y1, 'r', label='y = x^2 + 2x')
plt.plot(x, y2, 'g', label='y = x^2 - 2x')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.xlim(-4, 1)
plt.ylim(-6, 3)
plt.legend()
plt.title("Área entre las parábolas x^2 + 2x <= y <= x^2 - 2x para x ≤ 0")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()