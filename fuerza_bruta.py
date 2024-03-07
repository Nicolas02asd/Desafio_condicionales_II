
from string import ascii_lowercase
from getpass import getpass

contraseña = getpass("Ingrese la contraseña: ")
intentos = 0

for letra in contraseña:
    for letra_alfabeto in ascii_lowercase:
        intentos += 1
        if letra_alfabeto == letra:
            break

print(f"La contraseña fue forzada en {intentos} intentos.")



