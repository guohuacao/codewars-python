""""
#solution 1
def openOrSenior(data):
    rlist = []
    for item in data:
        if (item[0] >= 55 and item[1] > 7):
            rlist.append('Senior')
        else:
            rlist.append('Open')
    print (rlist)
    return rlist
"""
def openOrSenior(data):
    return ['Senior' if (item[0] >= 55 and item[1] > 7) else 'Open' for item in data]

print (openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]])) #,['Open', 'Senior', 'Open', 'Senior'])
