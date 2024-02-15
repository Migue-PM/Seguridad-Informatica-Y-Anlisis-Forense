import Crypto.Util.number
import Crypto.Random
import hashlib

# Número de bits
bits = 1024

# Obtener los primos para Alice y Bob
pA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("Primo de Alice", pA, "\n")

qA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("Primo de Alice", qA, "\n")

pB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("Primo de Bob", pB, "\n")

qB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("Primo de Bob", qB, "\n")

# Obtener la primera parte de la llave pública de Alice y Bob
nA = pA * qA
print("nA: ", nA, "\n")

nB = pB * qB
print("nB: ", nB, "\n")

# Calculamos el Indicador de Euler Phi
phiA = (pA - 1) * (qA - 1)
print("phiA: ", phiA, "\n")

phiB = (pB - 1) * (qB - 1)
print("phiB: ", phiB, "\n")

# Por razones de eficiencia usaremos el número 4 de Fermat: 65537, debido a que es 
# un primo largo y no es potencia de 2, y como forma parte de la clave pública, no es 
# necesario calcularlo
e = 65537

# Calcular la llave privada de Alice y Bob
dA = Crypto.Util.number.inverse(e, phiA)
print("dA: ", dA, "\n")

dB = Crypto.Util.number.inverse(e, phiB)
print("dB: ", dB, "\n")

# Mensaje original
msg = 'Hola mundo'
print("Mensaje original: ", msg, "\n")
print("Longitud del mensaje en bytes: ", len(msg.encode('utf-8')))

# Hash del mensaje original
hash_msg = hashlib.sha256(msg.encode('utf-8')).digest()
print("Firma hasheada del mensaje: ", hash_msg, "\n")

# Convertir el hash a número
m = int.from_bytes(hash_msg, byteorder='big')
print("Firma hasheada convertida en entero: ", m, "\n")

# Ciframos la firma hasheada
c = pow(m, dA, nA)
print("Firma hasheada cifrada: ", c, "\n")

# Desciframos la firma hasheada
des = pow(c, e, nA)
print("Firma hasheada descifrada: ", des, "\n")

if des == m:
    print ("Si es Igual")
