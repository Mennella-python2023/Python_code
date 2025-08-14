
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Crea la figura
fig, ax = plt.subplots(figsize=(8, 6))

# Crea il box per Arduino
arduino_box = patches.Rectangle((0.1, 0.7), 0.8, 0.25, linewidth=1, edgecolor='black', facecolor='lightgray', label="Arduino Uno")
ax.add_patch(arduino_box)

# Etichette per i pin di Arduino
ax.text(0.2, 0.85, "Pin A0", fontsize=12, color="black")
ax.text(0.85, 0.85, "5V", fontsize=12, color="black")
ax.text(0.85, 0.75, "GND", fontsize=12, color="black")

# Crea il box per il potenziometro
potentiometer_box = patches.Rectangle((0.55, 0.45), 0.35, 0.15, linewidth=1, edgecolor='black', facecolor='lightblue', label="Potenziometro")
ax.add_patch(potentiometer_box)

# Etichette per i pin del potenziometro
ax.text(0.7, 0.48, "Pin centrale (A0)", fontsize=10, color="black")
ax.text(0.7, 0.42, "Pin 5V", fontsize=10, color="black")
ax.text(0.7, 0.37, "Pin GND", fontsize=10, color="black")

# Disegna le linee di collegamento
ax.plot([0.5, 0.7], [0.5, 0.5], color="black", lw=2)  # Collegamento Pin A0
ax.plot([0.8, 0.85], [0.5, 0.73], color="black", lw=2)  # Collegamento Pin 5V
ax.plot([0.8, 0.85], [0.5, 0.63], color="black", lw=2)  # Collegamento Pin GND

# Aggiungi dettagli come frecce per migliorare la chiarezza
ax.annotate('', xy=(0.7, 0.5), xytext=(0.5, 0.5), arrowprops=dict(facecolor='black', edgecolor='black', arrowstyle="->", lw=2))  # A0
ax.annotate('', xy=(0.85, 0.73), xytext=(0.8, 0.5), arrowprops=dict(facecolor='black', edgecolor='black', arrowstyle="->", lw=2))  # 5V
ax.annotate('', xy=(0.85, 0.63), xytext=(0.8, 0.5), arrowprops=dict(facecolor='black', edgecolor='black', arrowstyle="->", lw=2))  # GND

# Aggiungi un altro testo per migliorare la chiarezza
ax.text(0.5, 0.55, "Collegamenti", fontsize=12, color="black", ha='center')

# Imposta limiti e proporzioni
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')

# Nascondi gli assi
ax.axis('off')

# Titolo
ax.set_title("Schema dettagliato di collegamento del potenziometro ad Arduino", fontsize=14)

# Mostra il grafico
plt.show()
