from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii
import base64


f = open('private_key.pem', 'r')
keyPair = RSA.import_key(f.read())

# Sign the message using the PKCS#1 v1.5 signature scheme (RSASP1)
archivo = open('documento_prueba.txt', 'rb').read()
hash = SHA256.new(archivo)
signer = PKCS115_SigScheme(keyPair)
signature = signer.sign(hash)

#signature = base64.b64encode(signature)
print(base64.b64encode(signature))

f = open('signature.bin', 'wb')
f.write(signature)
f.close()













