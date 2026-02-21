def Ex3(file):

    diz = {}          # Dizionario risultato finale: valuta → mese del massimo rincaro
    prezzo = {}       # Ultimo prezzo visto per ogni valuta
    maxrincaro = {}   # Valore del massimo rincaro per ogni valuta

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:

            dati = line.strip().split(',')

            mese = int(dati[0])  

            valute = dati[1::2]    
            cambi = dati[2::2]     

            for i in range(len(valute)):

                if valute[i] not in diz:
                    diz[valute[i]] = "nessun rincaro"
                    maxrincaro[valute[i]] = 0

                elif float(cambi[i]) - prezzo[valute[i]] > maxrincaro[valute[i]]:
                    maxrincaro[valute[i]] = float(cambi[i]) - prezzo[valute[i]]
                    diz[valute[i]] = mese

                prezzo[valute[i]] = float(cambi[i])

    return diz   # ← ORA È FUORI DAL CICLO
