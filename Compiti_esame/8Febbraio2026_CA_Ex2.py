def Ex2(file):
    import re
    conta = 0
    f=open(file,'r',encoding='utf-8')
    pattern = r'\b\w*(\w)\b\W+\b\1\w*(\w)\b\W+\b\2\w*\b'
    for line in f:
        if re.search(pattern, line):
            conta += 1
    f.close()
    return conta