import random
import hashlib

# Paso 1: Definir los parámetros
print("Paso 1: Definir los parámetros")
g = 2  # generador
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A63A3620FFFFFFFFFFFFFFFF  # un primo grande en hexadecimal
print("g:", g)
print("p:", p)

# Paso 2: Generar las llaves privadas de Alice y Bob
print("\nPaso 2: Generar las llaves privadas de Alice y Bob")
a = random.getrandbits(256)  # clave privada de Alice
b = random.getrandbits(256)  # clave privada de Bob
e = random.getrandbits(256)  # clave privada de Eve
print("Clave privada de Alice:", a)
print("Clave privada de Bob:", b)
print("Clave privada de Eve:", e)

# Paso 3: Simular el intercambio de números entre Alice y Bob
print("\nPaso 3: Simular el intercambio de números entre Alice y Bob")
A = pow(g, a, p)  # Alice calcula A
E = pow(g, e, p)  # Eve calcula C
B = pow(g, b, p)  # Bob calcula B
print("Valor calculado por Alice (A):", A)
print("Valor calculado por Eve (E):", E)
print("Valor calculado por Bob (B):", B)

# Paso 4: Calcular las claves secretas
print("\nPaso 4: Calcular las claves secretas")
s_alice_eve = pow(E, a, p)  # Alice calcula la clave secreta
s_eve_alice = pow(A, e, p)  # Eve calcula la clave secreta
s_bob_eve = pow(E, b, p)  # Bob calcula la clave secreta
s_eve_bob = pow(B, e, p)  # Eve calcula la clave secreta
print("Clave secreta entre Alice y Eve:", s_alice_eve)
print("Clave secreta entre Eve y Alice:", s_eve_alice)
print("Clave secreta entre Bob y Eve:", s_bob_eve)
print("Clave secreta entre Eve y Bob:", s_eve_bob)

# Paso 5: Verificar que las claves secretas sean iguales
print("\nPaso 5: Verificar que las claves secretas sean iguales")
hash_s_alice_eve = hashlib.sha256(str(s_alice_eve).encode()).hexdigest()
hash_s_eve_alice = hashlib.sha256(str(s_eve_alice).encode()).hexdigest()
hash_s_bob_eve = hashlib.sha256(str(s_bob_eve).encode()).hexdigest()
hash_s_eve_bob = hashlib.sha256(str(s_eve_bob).encode()).hexdigest()

if hash_s_alice_eve == hash_s_eve_alice:
    print("Las claves secretas entre Eve y Alice son iguales y válidas.")
    print("Clave secreta generada:", hash_s_alice_eve)
else:
    print("Las claves secretas no coinciden entre Eve y Alice.")

if hash_s_bob_eve == hash_s_eve_bob:
    print("Las claves secretas entre Eve y Bob son iguales y válidas.")
    print("Clave secreta generada:", hash_s_bob_eve)
else:
    print("Las claves secretas no coinciden entre Eve y Bob.")
