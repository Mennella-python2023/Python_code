def Ex1(s, c1, c2):
    maxlen = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            parte = s[i:j + 1]
            if j+1-i > maxlen and parte.count(c1) == parte.count(c2) and parte.count(c1) > 0:
                maxlen = maxlen = j + 1 - i
    return maxlen