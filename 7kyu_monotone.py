""" solution 1, bad implementation, try to compare item in list with all subsequent item"""
"""
global result_true
result_ture = True
def monotone(item, alist, positon):
    global result_true
    for id in range(positon, len(alist)):
        if alist[id] < item:
            return False
    return True

def is_monotone(heights):
    global result_true
    if not heights:
        return True
    #return monotone(x,heights, idex) for x in heights for idex in range(len(heights))
    idex = 0
    for x in heights:
        idex += 1
        result_true = monotone(x, heights, idex)
        if not result_true:
            return result_true
    else:
        return result_true

print (is_monotone([5,5,5,5,5,5,5]))
"""

def is_monotone(heights):
    for i, item in enumerate(heights):
        if i>0 and heights[i-1] > item: return False
    return True
