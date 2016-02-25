import re
def validate_hello(greetings):
    thelist = list()
    r = re.compile(r'\bhello\b | \bciao\b | \bsalut\b | \bhallo\b | \bhola\b | \bahoj\b | \bczesc\b', flags=re.I | re.X )
    #r = re.compile('hello | ciao | salut | hallo | hola | ahoj | czesc', flags=re.I | re.X )
    thelist = r.findall(greetings)
    print thelist
    if (len(thelist) == 0):
        return False
    else:
        return True
