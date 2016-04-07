def match(candidate, job):
    return candidate['min_salary'] * 0.9 <= job['max_salary']

"""
def match(candidate, job):
    try:
        cmin = candidate['min_salary']
        jmax = job["max_salary"]
        print (cmin)
        if (cmin*0.9 <= jmax):
            return True
        else:
            return False
    except:
            print ("Should throw error")
            return True
"""
