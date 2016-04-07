"""
Some numbers have funny properties. For example:

    89 --> 8¹ + 9² = 89 * 1

    695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

    46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

    Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.
"""

def dig_pow(n, p):
    s = 0
    for i,c in enumerate(str(n)):
        s += pow(int(c),p+i)
    return s/n if s%n==0 else -1

    """
    for ch in str(num):
        sum += pow(int(ch), factor)
        factor +=1

    if not (sum % num):
        return int(sum / num)
    else:
        return -1
    """

print (dig_pow(89, 1))
print (dig_pow(92, 1))
print (dig_pow(46288, 3))
