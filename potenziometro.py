
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create the plot
fig, ax = plt.subplots()

# Create a simple schematic for the potentiometer connection to Arduino
# Define the Arduino box
arduino_box = patches.Rectangle((0.1, 0.6), 0.8, 0.3, linewidth=1, edgecolor='black', facecolor='lightgray', label="Arduino")
ax.add_patch(arduino_box)

# Labels for Arduino pins
ax.text(0.2, 0.83, "A0", fontsize=10, color="black")
ax.text(0.85, 0.83, "5V", fontsize=10, color="black")
ax.text(0.85, 0.73, "GND", fontsize=10, color="black")

# Draw the potentiometer
potentiometer_box = patches.Rectangle((0.5, 0.4), 0.3, 0.15, linewidth=1, edgecolor='black', facecolor='lightblue', label="Potenziometro")
ax.add_patch(potentiometer_box)

# Labels for potentiometer pins
ax.text(0.7, 0.43, "Pin centrale", fontsize=8, color="black")
ax.text(0.7, 0.37, "Pin 5V", fontsize=8, color="black")
ax.text(0.7, 0.32, "Pin GND", fontsize=8, color="black")

# Draw lines connecting the components
ax.plot([0.5, 0.7], [0.5, 0.5], color="black")  # Pin centrale (A0)
ax.plot([0.8, 0.85], [0.5, 0.73], color="black")  # Pin 5V
ax.plot([0.8, 0.85], [0.5, 0.63], color="black")  # Pin GND

# Set the limits and aspect
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')

# Hide axes for better visibility
ax.axis('off')

# Title
ax.set_title("Schema di collegamento del potenziometro ad Arduino")

# Show the plot
plt.show()
