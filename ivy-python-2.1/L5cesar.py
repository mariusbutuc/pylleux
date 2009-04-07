def no_space(texte):
    return texte.replace(' ', '')

def upper(texte):
    return texte.upper()

"""
def my_ord(char):
    return ord(char) - 64

def my_chr(char):
    return chr(char + 64)

def cesar_code(texte, cle):
    # A=65 -> Z=90
    texte2 = ""
    cle_a = my_ord(cle)
    for let in texte:
        let_a = my_chr((my_ord(let) + cle_a - 1)%26)
        texte2 += let_a
    return texte2
"""

T = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def code(texte, cle):
    texte = upper(texte)
    cle = upper(cle)
    T2 = T[T.index(cle):] + T[:T.index(cle)] # dictionarul tradus
    return "".join([T2[T.index(x)] for x in texte])
    
def decode(texte, cle):
    texte = upper(texte)
    cle = upper(cle)
    T2 = T[T.index(cle):] + T[:T.index(cle)]
    return "".join([T[T2.index(x)] for x in texte])

def freq(texte):
    length = len(no_space(texte))
    # http://blogamundo.net/py4lx/counting.html
    letters = list(upper(texte))    # 1. list of letters
    occurences = {}                 # 2. dict 2 hold the counts
    freqs = {}
    for letter in T:
        occurences[letter] = letters.count(letter)
    for letter in occurences:
        freqs[letter] = occurences[letter] * 100 / length
    return freqs
        
def find_e(texte):
    freqs = freq(texte)
    return max(freqs, key = lambda x: freqs[x])
    # sortez cu items, iau tuplele, multe, multe, le sortez, gasesc maximele
    
    
def info(fmt, *arg):
    print fmt % arg
    
if __name__ == '__main__':
    while 1:
        try:
            msg = raw_input('')
        except (EOFError, KeyboardInterrupt):
            msg = '.q'
        
        if msg == '.h':
            info("You really think you need help?")
            
        elif msg[0] == 'c':
            cle = msg[1]
            texte = msg[2:]
            if not texte:
                print 'Error: missing text for coding'
            print 'cesar : ' + code(texte, cle)
            
        elif msg[0] == 'd':
            cle = msg[1]
            texte = msg[2:]
            if not texte:
                print 'Error: missing text for decoding'
            print 'cesar : ' + decode(texte, cle)
        
        elif msg == '.q':
            break
        
        else:
            info('Default text')