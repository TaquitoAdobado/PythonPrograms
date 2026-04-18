'''
Fundamento de seguridad para todo sistema de autenticacion:
    
    NUNCA se debe guardar contraseñas en texto plano.

Conceptos claves:

    * Hashing: Transformar una contraseña en una cadena irreconocible (cifrada) usando un algoritmo seguro (de hashing)

    * Salting: Añadir un valor aleatorio para que 2 contraseñas iguales no generen el mismo hash.

Flask cuenta con una libreria para el hashing de contraseñas llamada werkzeug.security
werzeug al hacer el hashing incluye el salting automaticamente.
'''

#Para usar werkzeug.security debemos importarlo de la siguiente manera:

from werkzeug.security import generate_password_hash, check_password_hash


# Ejemplo de creacion de un hash:

password = "MiContrasena12345" # Recordemos nunca guardar contraseñas en texto plano como en este ejemplo.
hashed_password = generate_password_hash(password)

password_2 = "MiContrasena12345"
hashed_password_2 = generate_password_hash(password_2)

print(f"Contraseña original: \n {password}")
print(f"Hash de la contraseña:\n {hashed_password}")


#Ejemplo de verificacion
print(f"Contraseña coincide con '{password}'?: \n {check_password_hash(hashed_password, password)}")
print(f"Contraseña coincide con 'OtraContrasena123'?: \n {check_password_hash(hashed_password, 'OtraContrasena123')}")

print(f"Si 2 contraseñas son iguales, sus hash son iguales tambien?: \n {hashed_password == hashed_password_2}")