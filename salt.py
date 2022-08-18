import hashlib
import binascii

#Salting: This is a method used for masking a password with random characters

print("SALTING \n")

hash = hashlib.pbkdf2_hmac("sha256", b"yahoo4messenger", b"saltthepassword", 10000)
binas = binascii.hexlify(hash)
print(f"Hash function: {hash}")
print(f"Hexlify function: {binas}")