from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes
from base64 import b64decode

enc_key = input("Enter encrypted key: ")

f = open("private.pem", "r")
key = RSA.import_key(f.read())

enc_key = bytes_to_long(b64decode(enc_key.encode()))
# print(enc_key)

dec_key = pow(enc_key, key.d, key.n)
dec_key = long_to_bytes(dec_key).decode()

print("Your decrypted key is:", dec_key)

