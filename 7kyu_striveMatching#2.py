"""
candidates = [{
  'desires_equity': True,
  'current_location': 'New York',
  'desired_locations': ['San Francisco', 'Los Angeles']
}, ...]

job = {
  'equity_max': 1.2,
  'locations': ['New York', 'Kentucky']
}
"""

def match(j, c):
    #match equity, and match locations
    newCandidates = []
    for can in c:
        if not (can['desires_equity'] and (j['equity_max'] == 0) ):
                combineLoc = [can['current_location']] + can['desired_locations']
                if (any((loc in j['locations']) for loc  in combineLoc)):
                    newCandidates.append(can)
    return newCandidates


candidates = [{
  'desires_equity': True,
  'current_location': 'New York',
  'desired_locations': ['San Francisco', 'Los Angeles']
}, {
  'desires_equity': False,
  'current_location': 'San Francisco',
  'desired_locations': ['Kentucky', 'New Mexico']
}]
job1 = { 'equity_max': 0, 'locations': ['Los Angeles', 'New York'] }
job2 = { 'equity_max': 1.2, 'locations': ['New York', 'Kentucky'] }

new = match(job1, candidates)
print (new)
#new1 = match(job2, candidates)
#print (new1)
#print len(match(job2, candidates))
#Test.assert_equals(len(match(job1, candidates)), 0)
#Test.assert_equals(len(match(job2, candidates)), 2)
