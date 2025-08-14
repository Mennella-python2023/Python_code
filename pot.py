
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Crea la figura
fig, ax = plt.subplots(figsize=(10, 6))

# Crea il box per Arduino
arduino_box = patches.Rectangle((0.05, 0.55), 0.3, 0.3, linewidth=1, edgecolor='black', facecolor='lightgray', label="Arduino Uno")
ax.add_patch(arduino_box)

# Etichette per i pin di Arduino
ax.text(0.17, 0.88, "A0", fontsize=12, color="black", ha="center")
ax.text(0.27, 0.68, "5V", fontsize=12, color="black", ha="center")
ax.text(0.27, 0.58, "GND", fontsize=12, color="black", ha="center")

# Crea il box per il potenziometro
potentiometer_box = patches.Rectangle((0.6, 0.45), 0.3, 0.15, linewidth=1, edgecolor='black', facecolor='lightblue', label="Potenziometro")
ax.add_patch(potentiometer_box)

# Etichette per i pin del potenziometro
ax.text(0.75, 0.51, "Pin centrale", fontsize=10, color="black", ha="center")
ax.text(0.75, 0.44, "Pin 5V", fontsize=10, color="black", ha="center")
ax.text(0.75, 0.38, "Pin GND", fontsize=10, color="black", ha="center")

# Disegna le linee di collegamento con frecce
ax.annotate('', xy=(0.17, 0.88), xytext=(0.75, 0.51), arrowprops=dict(facecolor='black', edgecolor='black', arrowstyle="->", lw=2))  # A0 -> Pin centrale
ax.annotate('', xy=(0.27, 0.68), xytext=(0.75, 0.44), arrowprops=dict(facecolor='black', edgecolor='black', arrowstyle="->", lw=2))  # 5V -> Pin 5V
ax.annotate('', xy=(0.27, 0.58), xytext=(0.75, 0.38), arrowprops=dict(facecolor='black', edgecolor='black', arrowstyle="->", lw=2))  # GND -> Pin GND

# Etichetta per la spiegazione
ax.text(0.5, 0.55, "Collegamento del potenziometro ad Arduino", fontsize=14, color="black", ha="center")

# Imposta limiti e proporzioni
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')

# Nascondi gli assi
ax.axis('off')

# Titolo
ax.set_title("Schema di collegamento preciso tra Arduino e potenziometro", fontsize=14)

# Mostra il grafico
plt.show()
