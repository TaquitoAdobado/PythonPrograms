import os

# ----------------Definicion de clases-----------------

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return (f'Nombre: {self.nombre}'
                f'\nApellido: {self.apellido}'
                f'\nNumero de cuenta: {self.numero_cuenta}'
                f'\nSaldo: ${self.balance}')

    def ingresar_dinero(self, cantidad):
        self.balance += cantidad
        print(f"Dinero ingresado con exito, su saldo actual es: ${self.balance}")

    def retirar_dinero(self, cantidad):
            self.balance -= cantidad
            print(f"Dinero retirado con exito, su saldo actual es: ${self.balance}")
# ----------------Funciones auxiliares------------------

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu():
    print("\n" + "*-"*15 + "*")
    print("Seleccione una opcion del menu:")
    print("*-"*15 + "*")
    print("1. Agregar cliente"
          "\n2. Buscar cliente"
          "\n3. Ingresar dinero"
          "\n4. Retirar dinero"
          "\n5. Salir")
    print("*-"*15 + "*")

def validacion_cuenta_nueva(numero_cuenta): # Valida que el numero de cuenta sea unico
    while numero_cuenta in cuentas_ocupadas:
        numero_cuenta += 1
    return numero_cuenta

def ingresar_numero():  # Usaremos para validar el ingreso de numeros de cuenta o montos de dinero
    try:
        ingreso =  int(input())
        limpiar_pantalla()
        return ingreso
    except ValueError:
        limpiar_pantalla()
        print("Opcion invalida, intenta de nuevo :)")
        return

def validacion_cuenta_existente(numero_cuenta): # Valida que el numero de cuenta exista
    if numero_cuenta not in cuentas_ocupadas:
        return "Rechazado"
    else:
        return "Validado"

def validacion_opcion_menu(opcion_usuario, numero_cuenta=1111):
    try:
        if opcion_usuario == 1: # Ejecutamos la opcion de agregar cliente
            numero_cuenta = validacion_cuenta_nueva(numero_cuenta)
            menu_principal[opcion_usuario](numero_cuenta)
            return
        else:
            salir_programa = menu_principal[opcion_usuario]()   # Ejecutamos la opcion elegida
            return salir_programa
    except KeyError:    # Mensaje de error si opcion no existe
        os.system("cls" if os.name == "nt" else "clear")
        print("Opcion no existente, intenta de nuevo :)")
        return

# ----------------Funciones del menu------------------

def agregar_cliente(numero_cuenta, balance = 0):
    nombre = input("Ingrese nombre del cliente: ")
    apellido = input("Ingrese apellido del cliente: ")
    nuevo_cliente = Cliente(nombre, apellido, numero_cuenta, balance)   # Se crea la instancia de Cliente
    lista_clientes.update({nuevo_cliente.numero_cuenta: nuevo_cliente}) # Agregamos la instancia a la lista
    cuentas_ocupadas.append(numero_cuenta)  # Agregamos el numero de cuenta a la lista para validar que no se repita
    limpiar_pantalla()
    print(f"Cliente registrado con exito. Su numero de cuenta es: {nuevo_cliente.numero_cuenta}")
    return nuevo_cliente

def buscar_cliente():
    print("¿Cual es el numero de cuenta del cliente que desea buscar?")
    numero_cuenta = ingresar_numero()
    if numero_cuenta is None:
        return
    if validacion_cuenta_existente(numero_cuenta) == "Rechazado":
        print("Numero de cuenta inexistente")
        return
    else:
        print(lista_clientes[numero_cuenta])    # Imprimimos la instancia del cliente elegido


def ingresar_dinero():
    print("Ingrese el numero de cuenta a ingresar dinero")
    numero_cuenta = ingresar_numero()
    while numero_cuenta is not None:
        if validacion_cuenta_existente(numero_cuenta) == "Rechazado":
            print("Numero de cuenta inexistente")
            break
        else:
            print(f"\nSaldo actual: ${lista_clientes[numero_cuenta].balance}")
            print("Ingrese la cantidad de dinero a ingresar: $", end="")
            monto = ingresar_numero()
            if monto is None:
                continue
            elif monto<0:
                print("Cantidad invalida")
                continue
            else:
                lista_clientes[numero_cuenta].ingresar_dinero(monto)
                break
    return

def retirar_dinero():
    print("Ingrese el numero de cuenta a retirar dinero")
    numero_cuenta = ingresar_numero()
    while numero_cuenta is not None:
        if validacion_cuenta_existente(numero_cuenta) == "Rechazado":
            print("Numero de cuenta inexistente")
            break
        else:
            print(f"\nSaldo actual: ${lista_clientes[numero_cuenta].balance}")
            print("Ingrese la cantidad de dinero a retirar: $", end = "")
            monto = ingresar_numero()
            if monto is None:
                continue
            elif monto<0:
                print("Cantidad invalida")
            elif monto>lista_clientes[numero_cuenta].balance:
                print("Saldo insuficiente")
                continue
            else:
                lista_clientes[numero_cuenta].retirar_dinero(monto)
                break
    return

def salir():
    limpiar_pantalla()
    return True


# ----------------Variables globales------------------
cuentas_ocupadas = []
lista_clientes={}
menu_principal = {
    1: agregar_cliente,
    2: buscar_cliente,
    3: ingresar_dinero,
    4: retirar_dinero,
    5: salir
}

# ----------------Ejecucion del programa----------------
salir = None
while salir is None:    # Bucle hasta que se ejecute la opcion 5 del menu: salir
    mostrar_menu()
    ingreso_usuario = ingresar_numero() # Se solicita al usuario el ingreso de una opcion
    if ingreso_usuario is None: # Si el ingreso es invalido, se repite el bucle
        continue
    else:
        salir = validacion_opcion_menu(ingreso_usuario) # Si el ingreso es valido, se ejecuta la opcion elegida

# ----------------Fin del programa----------------
print("\nGracias por usar el programa")