def Ex2(i, file):
    import re
    dizionario = {elemento: 0 for elemento in i}

    with open(file, 'r', encoding='utf-8') as f:
        testo = f.read()

    pattern = r'(00|\+)(\d\d?)-?\d\d\d-?\d\d\d\d\d\b'

    for match in re.finditer(pattern, testo):
        prefisso = match.group(2)
        if prefisso in dizionario:
            dizionario[prefisso] += 1

    return dizionario


# --- TEST ---
ris = Ex2(["39", "1", "44"], "numeri.txt")
print(ris)
