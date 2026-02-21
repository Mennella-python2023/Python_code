def Ex3(file1,file2):
    menu = {}
    dizionario = {}

    with open(file1, 'r') as f1:
        for line in f1:
            parts = line.strip().split(',')
            piatto = parts[0]
            prezzo = float(parts[1])
            disponibilita = int(parts[2])   # <-- CORRETTO
            menu[piatto] = (prezzo, disponibilita)

    with open(file2, 'r') as f2:
        for line in f2:
            parts = line.strip().split(',')
            cliente = parts[0]
            ordini = parts[1:]
            ok = True
            costo_totale = 0

            for ordine in ordini:
                ordine = ordine.split(':')
                piatto = ordine[0].strip()
                quantita = int(ordine[1])
                if quantita > menu[piatto][1]:
                    ok = False

            if not ok:
                dizionario[cliente] = 'Ordine non disponibile'
            else:
                for ordine in ordini:
                    ordine = ordine.split(':')
                    piatto = ordine[0].strip()
                    quantita = int(ordine[1])
                    prezzo, disp = menu[piatto]
                    costo_totale += prezzo * quantita
                    menu[piatto] = (prezzo, disp - quantita)

                dizionario[cliente] = costo_totale

    return dizionario


if __name__ == "__main__":
    risultato = Ex3("file1.csv", "file2.csv")
    print(risultato)
