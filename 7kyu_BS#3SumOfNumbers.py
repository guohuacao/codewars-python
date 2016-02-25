def sum(small, big):
    i = big - small
    if(i%2 == 0):
        j= i/2
        return j*(big+small) + (big+small)/2
    else:
        j=i/2 +1
        return j*(big+small)

def get_sum(a,b):
    if (a == b):
        return a
    elif( a > b):
        return sum(b, a)
    else:
        return sum(a, b)
