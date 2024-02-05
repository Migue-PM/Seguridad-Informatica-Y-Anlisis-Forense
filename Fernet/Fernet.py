#cifrado fernet

from cryptography.fernet import Fernet


clave = Fernet.generate_key()

f = Fernet(clave)

token = f.encrypt(b'   Banate')

print(token)
print (clave)


#Descifrar
des= f.decrypt(token)

print(des)