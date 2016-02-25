def summation(x):
    if isinstance(x, int):
        return sum(xrange(1,x+1))
    else:
        return "Error 404"
