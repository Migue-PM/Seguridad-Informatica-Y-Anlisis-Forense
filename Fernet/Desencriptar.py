#cifrado fernet

from cryptography.fernet import Fernet

clave = "vDp1tWGJVPY4959E4oTQkCHlcXemGCPaU9lkzU3p2IE="
f = Fernet(clave)
token = "gAAAAABluwihxlabpYgTWc9E1YSbeGvKkjm2XXGANhdEpC310jOMHu5Vqzl6r0OV8t7iT0Ny9xet81EBNceXh3cvWpJr0Sb-wA=="

#Descifrar
des= f.decrypt(token)

print(des)