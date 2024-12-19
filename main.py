import random

# Variable con los caracteres que pueden componer la contraseña
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Solicitar al usuario la longitud de la contraseña
password_length = int(input("Introduce la longitud de la contraseña: "))

# Variable para almacenar la contraseña generada
generated_password = ""

# Generar la contraseña usando un bucle
for _ in range(password_length):
    generated_password += random.choice(characters)

# Imprimir la contraseña resultante
print("Tu contraseña generada es:", generated_password)
