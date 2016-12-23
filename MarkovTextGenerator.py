import random
def split(filename):
    f= open(filename)
    text=f.read()
    f.close()
    return text.split()
def cD(filename):
    f = open(filename)
    text = f.read()
    f.close()
    punc = ['.','!','?']
    LoW = text.split()
    d={}
    NLoW = []
    for w in LoW:
        # Makes a list with elements with a punctuation mark
        if w[-1] in punc:
            NLoW = NLoW + [w]
    d['$'] = [LoW[0]]
    for w in range(len(LoW)):
        # $ is a list of starting words
 
        if '.' in LoW[w] or '!' in LoW[w] or '?' in LoW[w]:
            if w<(len(LoW)-1):
                d['$'] += [LoW[w+1]]
    for w in range(len(LoW)):
        #dictionary d now contains all elements from LoW as key.
            d[LoW[w]] =[]
    for w in range(len(LoW)):
        # d now contains all elements from LoW as keys and set the
        # proceeding words as its values
    
        if w<(len(LoW)-1):
            d[LoW[w]] += [LoW[w+1]]
    k = list(set(NLoW))
    for i in range(len(k)):
        #dictionary d now removes all keys with a puncutation mark
        del d[k[i]]
    
    return d

def gT(n=0):
    # the function returns a string of 'n' words.
    punc = ['.','!','?']
    d= input("filename : ") # takes a filename from user
    f = cD(d) #cD(user's input) and assign it to f
    g = f.get('$') # list of first words
    fw = random.choice(g) # first word in string
    sen = [fw]
    for i in range(n-1):
        p = f.get(sen[-1])
        if p == None:
            p = g
        nw = random.choice(p)
        sen += [nw]
    blank = ''
    for numb in range(len(sen)):
       blank = blank + str(sen[numb]) + ' '
    print blank
        
        
        
        
    

    
    
