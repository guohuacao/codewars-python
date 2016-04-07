spoken    = lambda greeting: greeting+'.'  #'Hello.'
shouted   = lambda greeting: greeting.upper()+'!' #'HELLO!'
whispered = lambda greeting: greeting.lower()+'.' # "hello."

D = {'spoken': spoken, 'shouted':shouted, 'whispered':whispered}
#greet = lambda style, msg: style(msg)

#greet = lambda style, msg: spoken(msg) if (style == spoken) else shouted(msg) if (style == shouted) else whispered(msg)  #?

greet = lambda style, msg: map(style, [msg])[0]

greet(spoken, "Hello")
