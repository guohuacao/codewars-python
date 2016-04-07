"""notes from Idomatic video in Feb, 2016"""

for i in [ 0, 1, 2, 3, 4, 5]:
    print i **2

for i in range(6):  ##good
    print i **2

for i in xrange(6):
    print i **2

for i in range(len(colors)):
    print color[i]

colors = ['red', 'green', 'red', 'blue']
for color in colors:    #good
    print color

for color in reversed(colors):
    print color

for i, color in enumerate(colors): # list indexes
    print i, '--->', colors[i]

names = ['ray', 'grace']

for color, name in zip(colors, names): #third list of tuple, memory not scale
    print color, '--->', name

for color, name in izip(colors, names): #?
    print color, '--->', name

for color in sorted(colors):
    print color
for color in sorted(colors, reverse=True):
    print color

def compare_length(c1, c2)
print sorted(colors, cmp=compare_length) #bad

print sorted(colors, key=len)

#iter, partial

block = []
while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)

for block in iter(partial(f.read, 32), ''):
    blocks.append(block)

#connect together, .join, not connect together +

def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
        else:
            return -1
        return i

d = { 'matthew': 'blue', 'rachel':' green', 'raymond':' red'}
for k in d:
    print k  #keys

for k in d.keys(): # d.keys() is copy, so free to mutate the dictionary
    if k.startwith('r'):
        del d[k]

for k, v in d.items():
    print k, '--->', v

for k, v in d.iteritems():
    print k, '--->', v

d = dict(izip(names, colors))
d = dict(enumerate(names))
{'0', 'raymond', '2': 'rachel'}

#counting using a dictionary
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
    {'red': 2 , 'green': 1, 'blue': 1}

for color in colors:
    d[color] = d.get(color, 0) + 1

d = defaultdict(int)
for color in colors:
    d[color] += 1

#Grouping with dictionary
d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)

d={}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)

d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)

# is a dictionary popitem atomic? yes
while d:
    key, value = d.popitem()
    print key, '--->', value

#linking dictornaries
defaults = { 'color': 'red', 'user': 'guest'}
parser = argparser.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args([])
command_line_args = { k:v for k, v in vars(namespace).items() if v}

# the following code copys like crazy
d = defaults.copy()
d.update(os.version)
d.update(command_line_args)

# do like this
d = ChainMap(command_line_args, os.version, defaults)

#clarify function calls with keyword Arguments
twitter_search('@obama', False, 20, True)
twitter_search('@obama', retweets=False, numtweets=20, popular=True) #do this

#Clarify multiple return values with names tuples
doctest.testmod()
(0,4)

#now it returns
doctest.testmod()
TestResults(failed=0, attempted=4)
TestResults = namedtuple('TestResults', ['failed','attempted'])

#Unpacking sequences
p = 'ray', 'hettinger', 0x30, 'python@example.com'
fname, lname, age, email = p

#Update multiple state variables
def fibonacci(n):
    x, y = 0,1
    for i in range(n):
        x, y = y, x+y

x, y, dx, dxy = ( x + dx*t,
                    y + dy * t
                    influece(....),
                    influnce(....))

#Concatenating strings
s = name[0]
for name in names[1:]:
    s == ','  + name
print s

#should do this instead
prinnt ', '.join(names)

#Updating sequences
del name[0]
names.pop(0)
names.insert(0, 'mark')

#instead
names = deque([names])
del name[0]
names.popleft()
names.insertleft('mark')

# Decorators and context managers
# using decorators to factor-out administrative logic
def web_loopup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url), read()
    saved[url] = page
    return page

#peer function - everytime return the same item
@cache
def web_loopup(url):
    return urllib.urlopen(url).read()

#Caching decorators
def cache(func):
    saved = {}
    @wrapps(func)
    def newfunc(*args):
        if args in saved:
                return newfunc(*args)
        result = func(*args)
        saved[args] = result
        return result
    return newfunc

#facotr-out temporary contexts
old_context = getcontext.copy()
getcontext().prec = 50
print Decimal(355) / Decimal(133)
setcontext(old_context)

with localcontext(Context(prec=50)):
    print Decimal(355) / Decimal(133)

#how to open and close failed
f = open('data.txt')
try:
    data = f.read()
finally:
    f.close()

#new way
with open('data.txt') as f:
    data = f.read()

#how ot use locks
lock = threading.Lock()
#oldway
lock.acquire()
try:
    print ('cristical section 1')
    print ('critical section 2')
finally:
    lock.release()

    #new way
    with lock:
        print ('cristical section 1')
        print ('critical section 2')

try:
    os.remove('somefile')
except OSError:
    pass

with ignored(OSError):
    os.remove('somefile')

sum(i**2 for i in range(10))
