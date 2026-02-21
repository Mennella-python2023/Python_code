import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione
def f(x):
    return np.abs(x**2 - 4*x + 3) + np.sqrt(np.abs(x - 1))

# Definiamo un dominio
x = np.linspace(-3, 5, 400)

# Evitiamo valori negativi per la radice quadrata (dove il dominio non è valido)
x = x[x >= 1]

# Calcoliamo i valori della funzione
y = f(x)

# Grafico della funzione
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$f(x) = |x^2 - 4x + 3| + \sqrt{|x - 1|}$', color='b')
plt.title('Grafico della funzione f(x) = |x^2 - 4x + 3| + √|x - 1|')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()
