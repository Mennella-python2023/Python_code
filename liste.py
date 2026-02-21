def ex1(l, n):
    """
    Restituisce l'insieme delle stringhe s1 in l tali che
    esiste almeno una stringa s2 (diversa da s1) con almeno
    n caratteri diversi in comune.
    """
    ris = set()
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            comuni = set(l[i]) & set(l[j])
            if len(comuni) >= n:
                ris.add(l[i])
                ris.add(l[j])
    return ris


# -----------------------
# TEST
# -----------------------

def test_ex1():
    l = ['arciere', 'pippo', 'accordare']
    n = 2
    risultato_atteso = {'arciere', 'accordare'}
    
    risultato = ex1(l, n)
    
    print("Risultato ottenuto:", risultato)
    print("Risultato atteso:  ", risultato_atteso)
    
    if risultato == risultato_atteso:
        print("✔ Test superato")
    else:
        print("✘ Test fallito")


# Esegui il test
test_ex1()
