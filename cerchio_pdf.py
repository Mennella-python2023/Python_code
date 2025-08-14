
import math
from reportlab.pdfgen import canvas

def disegna_cerchio_pdf(R, nome_file="cerchio.pdf"):
    fattore_y = 0.5
    scala = 10  # dimensione dei caratteri (più grande = più leggibile)

    # Crea un canvas PDF
    c = canvas.Canvas(nome_file)

    # Font e dimensioni
    c.setFont("Courier", scala)

    # Coordinate iniziali (offset per lasciare margini)
    offset_x = 50
    offset_y = 800  # partiamo dall'alto

    for y in range(-R, R+1):
        riga = ""
        for x in range(-R, R+1):
            distanza = math.sqrt(x**2 + (y / fattore_y)**2)
            if abs(distanza - R) < 0.5:
                riga += "*"
            else:
                riga += " "
        # Scrive la riga nel PDF, spostando verso il basso ad ogni riga
        c.drawString(offset_x, offset_y - scala * (y + R), riga)

    c.save()
    print(f"Cerchio di raggio {R} salvato in '{nome_file}'.")

# Esempio di utilizzo
R = int(input("Inserisci il raggio R (numero intero positivo): "))
disegna_cerchio_pdf(R)
