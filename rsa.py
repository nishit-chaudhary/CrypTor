from Crypto.PublicKey import RSA

key = RSA.generate(2048)
f = open("private.pem", "wb")
f.write(key.export_key("PEM"))
f.close()

pub = key.publickey()
f = open("public.pem", "wb")
f.write(pub.export_key("PEM"))
f.close()