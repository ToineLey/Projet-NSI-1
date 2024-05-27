import time
secret = b'\x0e6/+y;.< x-(7,,\x9b\xf0z48z:646<z*\x9a\xf3(64+<{'

ch='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def chiffre_xor(msg,cle):
    ch=[]
    for i in range(len(msg)):
        ch.append(msg[i]^cle[i%len(cle)])
    return

def force():
    for elem1 in ch:
        for elem2 in ch:
            for elem3 in ch:
                a=chiffre_xor(secret,bytes(elem1+elem2+elem3))
                if a[-4:].decode()=="nse!":
                    return elem1+elem2+elem3
                
print(force())