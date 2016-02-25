def sum_consecutives(s):
    dl = list()
    for i in (xrange(len(s)-1)):
        print i
        if (s[i] != s[i+1]):
            continue
        else:
            dl.append(i)
    #print dl
    for j in reversed(dl):
            s[j+1] += s[j]
            #print s[j]
            s.pop(j)
    return s 
