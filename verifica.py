from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii
import base64

# Generate 1024-bit RSA key pair (private + public key)
#keyPair = RSA.generate(bits=1024)
#pubKey = keyPair.publickey()

f = open('public_key.pem', 'r')
pubKey = RSA.import_key(f.read())
f.close()

f = open('signature.bin', 'rb')
signature = f.read()
f.close()

archivo = open('documento_prueba.txt', 'rb').read()
hash = SHA256.new(archivo)
verifier = PKCS115_SigScheme(pubKey)

try:
    verifier.verify(hash, signature)
    print('la firma es valida')
except:
    print('la firma no es valida')

"""
arrbytes 
byte = f.read(1)
while(byte):
    print(byte)
    byte = f.read(1)
f.close()
"""





"""
print("Signature:", base64.b64encode(signature))


# Verify valid PKCS#1 v1.5 signature (RSAVP1)
msg = b'Message for RSA signing'
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pubKey)


try:
    verifier.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")

# Verify invalid PKCS#1 v1.5 signature (RSAVP1)
msg = b'A tampered message'
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pubKey)
try:
    verifier.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")
"""







