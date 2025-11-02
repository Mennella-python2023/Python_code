# Funzione per calcolare la somma dei numeri
def somma_lista(lista):
    somma = 0
    for numero in lista:
        somma += numero
    return somma

# Lista di esempio
numeri = [10, 20, 30, 40, 50]

# Calcolare la somma
risultato = somma_lista(numeri)

# Visualizzare il risultato
print(f"La somma dei numeri nella lista è: {risultato}")
