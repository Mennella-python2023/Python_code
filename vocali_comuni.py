def ex2(l, n):
    """
    Restituisce l'insieme delle stringhe s1 in l tali che
    esiste almeno una stringa s2 (diversa da s1) con almeno
    n vocali diverse in comune.
    """
    vocali = {'a', 'e', 'i', 'o', 'u'}
    ris = set()

    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            v1 = set(l[i]) & vocali
            v2 = set(l[j]) & vocali
            comuni = v1 & v2

            if len(comuni) >= n:
                ris.add(l[i])
                ris.add(l[j])

    return ris


# -----------------------
# TEST
# -----------------------

def test_ex2():
    l = ["cane", "cena", "gatto", "piuma"]
    n = 2
    risultato_atteso = {"cane", "cena"}

    risultato = ex2(l, n)

    print("Risultato ottenuto:", risultato)
    print("Risultato atteso:  ", risultato_atteso)

    if risultato == risultato_atteso:
        print("✔ Test superato")
    else:
        print("✘ Test fallito")


# Esegui il test
test_ex2()
