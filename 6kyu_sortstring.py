

"""
sort words based on the digit(number) in each word
"""
"""
#Solution 1
def order(sentence):
    if not sentence:
        return ''
    new_sentence = sentence.split()
    #print (new_sentence)
    word_order_org =[]
    for x in new_sentence:
        word_order_org += list(int(i) for i in x if (i.isdigit()))
    mydict = dict(zip(word_order_org,new_sentence))
    result=''
    for key in mydict.keys():
        if (key != 1):
            result += ' '
        result += (mydict[key])
    print ('result is: {} '.format(result))
    return result

"""
"""
#solution 2
def order(sentence):
    return " ".join(sorted(sentence.split(),key=lambda x: int(i) for i in x if (i.isdigit())))
                    #key=lambda x: int(filter(str.isdigit, x))))
"""



"""
#solution 3
def order(words):
    print (' '.join(sorted(words.split(), key=lambda w:sorted(w))))
    return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
"""
#solution 4
def order(sentence):
  import re
  def find_num(str):
    print ("".join(re.findall("\d*", str)))
    return int("".join(re.findall("\d*", str)))
  return " ".join(sorted(sentence.split(), key = find_num))

"""
def order(sentence):
    if not sentence:
        return ''
    new_sentence = sentence.split()
    #print (new_sentence)
    #print (sorted(list(word for word in new_sentence)))
    for word in new_sentence:
        print (sorted(word))
"""
order("is2 Thi1s T4est 3a")
