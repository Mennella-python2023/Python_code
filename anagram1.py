def Ex1(l1,l2):
    ris = set()
    for s1 in l1:
        for s2 in l2:
            if len(s1) == len(s2):
                anagram = True
                for c in s1:
                    if s1.count(c) != s2.count(c):
                        anagram = False
                        break                       
                if anagram:
                    ris.add(s1)
                    ris.add(s2)
    return ris
