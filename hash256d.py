from hashlib import sha256
import sys

print(f'usage: python {sys.argv[0]} password 414')

w = bytes(sys.argv[1], 'utf-8')
#w = b'Password'

rom = int(sys.argv[2])


#def dgs(sat):
    #return sha256(sat).digest()

# h1 = dgs(w)

def hmany(dgst, dk=2):
    ndg = dgst
    for i in range(dk):
        ndg = sha256(ndg).digest()
    return ndg.hex()



nh = hmany(w,rom)

print(nh)








