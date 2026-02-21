def Ex1(l1, l2):
    """
    Restituisce l'insieme di tutte le parole che hanno almeno
    un anagramma nell'altra lista.
    """
    ris = set()
    for i in l1:
        for j in l2:
            if sorted(i) == sorted(j):
                ris.add(i)
                ris.add(j)
    return ris


# -------------------------
# TEST DI PROVA
# -------------------------

if __name__ == "__main__":
    l1 = ['arco', 'pluto', 'corda']
    l2 = ['palla', 'darco', 'ocra']

    risultato = Ex1(l1, l2)
    print("Risultato:", risultato)

    # Controllo atteso
    atteso = {'arco', 'ocra', 'darco', 'corda'}

    print("Test superato:", risultato == atteso)

