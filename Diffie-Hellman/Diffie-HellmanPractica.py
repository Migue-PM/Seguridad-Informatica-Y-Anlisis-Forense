import random
from cryptography.fernet import Fernet

def generar_primo():
    # Este es un número primo seguro para Diffie-Hellman
    return 23

def generar_llave_privada():
    # Genera una llave privada aleatoria de 256 bits
    return random.getrandbits(256)

def generar_llave_publica(g, private_key, p):
    # Calcula la llave pública según A = g^private_key mod p
    return pow(g, private_key, p)

def generar_llave_secreta(public_key, private_key, p):
    # Calcula la llave secreta según s = public_key^private_key mod p
    return pow(public_key, private_key, p)

def main():
    # Paso 1: Definir g y p
    g = 2
    p = generar_primo()

    # Paso 2: Generar llaves privadas aleatorias para Alice y Bob
    private_key_A = generar_llave_privada()
    private_key_B = generar_llave_privada()

    # Paso 3: Simular el intercambio de números entre Alice y Bob
    public_key_A = generar_llave_publica(g, private_key_A, p)
    public_key_B = generar_llave_publica(g, private_key_B, p)

    # Paso 4: Calcular la llave secreta
    secret_key_A = generar_llave_secreta(public_key_B, private_key_A, p)
    secret_key_B = generar_llave_secreta(public_key_A, private_key_B, p)

    print("Secret Key A:", secret_key_A)
    print("Secret Key B:", secret_key_B)

    # Checar si las claves secretas son iguales
    if secret_key_A == secret_key_B:
        print("Las claves secretas son iguales.")
    else:
        print("Las claves secretas NO son iguales.")

    # Clave de Fernet utilizando la clave secreta
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    data = b"Message"
    cipher_text = cipher_suite.encrypt(data)
    plain_text = cipher_suite.decrypt(cipher_text)

    # Checar que el mensaje cifrado y descifrado sea igual al original
    assert plain_text == data

if __name__ == "__main__":
    main()
