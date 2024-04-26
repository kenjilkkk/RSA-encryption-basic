import itertools
import random

word = input('Escreva a mensagem a ser codificada(RSA): ')
d = []
cod = []
dec = []

for z  in word:
    d.append(z)
 
def prime():
    counter = 0
    a = list(range(1,1000))
    while True:
        ch = random.choice(a)
        if ch == 1:
            return(ch)

        else: 
            for num in range(2,ch-1):
                if ch % num == 0:
                    counter = 1
                else:
                    continue
            if counter == 0:
                return(ch)
            else:
                continue

def repetidor():
    nb = prime()
    while nb == 1:
        nb = prime()

    return(nb)


def encrypt(p,q):
    global n
    global z
    global e
    #p = 17 #numero primo 1
    #q = 11 #numero primo 2
    z = (p-1)*(q-1) #chave públlica
    n = p*q #chave públlica
    i = 0
    global cod
    for x in range(1, z-1):
        if z%x != 0:
            e = x #chave públlica
            break
    
    while i <= len(d) - 1:
        
        for o in d[i]:
            cod.append((ord(o)**e)%n)
            
            #print(ord(o))
            i+=1

def decrypt():
    global key
    for d in itertools.count(start=1,step=1):
        if d*e % z == 1:
            key = d
            break
    s = 0
    while s <= len(cod) - 1:
        for l in cod:
            dec.append(chr((l**key)%n))
            
            s += 1
    
    palavra_decodificada = ''.join(dec)
    return(palavra_decodificada.encode('utf-8').decode('utf-8'))

#encrypt(prime(),prime())
encrypt(repetidor(),repetidor())
print(cod)
print(decrypt())

