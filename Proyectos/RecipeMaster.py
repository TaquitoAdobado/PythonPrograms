import os
from os import system
from pathlib import Path


def limpiar_pantalla():
    system("cls" if os.name == "nt" else "clear")

def creacion_carpetas_default():
    categories_rute = Path(Path.home(), 'RecipeMaster', 'Recetas')
    if not categories_rute.exists():
        categories_rute.mkdir(parents=True)
        default_categories = ['Carnes', 'Ensaladas', 'Pastas', 'Postres']
        for category in default_categories:
            Path(categories_rute, category).mkdir()

    return categories_rute

def bienvenida():
    print('\n' + '*' * 27)
    print("* Welcome to RecipeMaster *")
    print('*' * 27)

def contador_recetas(ruta_proyecto):
    recetas = list(ruta_proyecto.glob('**/*.txt'))
    print(f"\nRecetas existentes: {len(recetas)}")

def mostrar_menu():
    print("\n1 : Leer Receta\n2 : Crear Receta\n3 : Crear Categoria\n"
          "4 : Borrar Receta\n5 : Borrar Categoria\n6 : Cerrar Programa ")

def seleccion_menu():
    menu = {
        1: leer_receta,
        2: crear_receta,
        3: crear_categoria,
        4: borrar_receta,
        5: borrar_categoria
    }
    while True:
        try:
            seleccion_usuario = int(input("\nSeleccione una opción del menú: "))
            if seleccion_usuario not in range(1, 7):
                print("\nEsa opción no existe, intenta nuevamente")
            elif seleccion_usuario == 6:
                return False
            else:
                menu[seleccion_usuario]()
                regresar()
                return True
        except ValueError:
            print("\nEntrada invalida, intenta de nuevo")

def regresar():
    while True:
        clave = input("\nIngrese 'q' para regresar al menu: ").lower()
        if not clave == 'q':
            limpiar_pantalla()
            print("\nEntrada invalida")
        else:
            return

def mostrar_categorias(ruta_categorias):
    if len(list(ruta_categorias.glob('*'))) == 0:
        print("\nNo hay categorias, crea una primero")
        return None
    print("\nCategorias:\n")
    numero_opcion = 1
    for categoria in ruta_categorias.glob('**/*'):
        if categoria.is_dir():
            print(numero_opcion,':',categoria.name)
            numero_opcion += 1

def seleccion_usuario(ruta, metodo, nombre='categoria', tipo='directorios'):
    tipo = []
    for elemento in ruta.iterdir():
        if metodo(elemento):
            tipo.append(elemento.name)

    while True:
        try:
            seleccion_objeto = int(input(f"\nSeleccione una {nombre}: "))
            if not seleccion_objeto in range(1, len(tipo) + 1):
                print(f"\nEsa opcion no existe, intenta nuevamente")
            else:
                return Path(ruta, tipo[seleccion_objeto - 1])
        except ValueError:
            print(f"\nEntrada invalida, intenta nuevamente")

def mostrar_recetas(ruta_recetas):
    if len(list(ruta_recetas.glob('*.txt'))) == 0:
        print("\nNo hay recetas en esta categoria")
        return None
    print("\nRecetas:\n")
    numero = 1
    for receta in ruta_recetas.glob('*.txt'):
        print(numero, ':', receta.name)
        numero += 1

def contenido_receta(receta):
    print("\nIngrese el contenido de la receta (escribe 'end' para terminar):\n")
    contenido_receta = ""
    while True:
        renglon = input("")
        if renglon.lower() == 'end':
            break
        contenido_receta += renglon + '\n'
    receta.write_text(contenido_receta)
    print("\nReceta creada con exito")

#----------- Funciones principales -----------
def leer_receta():
    limpiar_pantalla()
    if mostrar_categorias(ruta_categorias) == None:
        return
    else:
        ruta_recetas = seleccion_usuario(ruta_categorias, Path.is_dir)
        limpiar_pantalla()
        if mostrar_recetas(ruta_recetas) == None:
            return
        else:
            receta_seleccionada = seleccion_usuario(ruta_recetas, Path.is_file, 'receta', 'archivos')
            limpiar_pantalla()
            print(f"\n{receta_seleccionada.stem}:\n")
            print(receta_seleccionada.read_text())
            return

def crear_receta():
    limpiar_pantalla()
    if mostrar_categorias(ruta_categorias) == None:
        return
    else:
        ruta_recetas = seleccion_usuario(ruta_categorias, Path.is_dir)
        limpiar_pantalla()
        mostrar_recetas(ruta_recetas)
        receta_nombre = input("\nIngrese el nombre de la receta nueva: ")
        receta = Path(ruta_recetas, receta_nombre + '.txt')
        receta.touch()
        contenido_receta(receta)
        return

def crear_categoria():
    limpiar_pantalla()
    mostrar_categorias(ruta_categorias)
    nombre_categoria = input("\nIngrese el nombre de la categoria nueva: ")
    Path(ruta_categorias, nombre_categoria).mkdir()
    return
def borrar_receta():
    limpiar_pantalla()
    if mostrar_categorias(ruta_categorias) == None:
        return
    else:
        ruta_recetas = seleccion_usuario(ruta_categorias, Path.is_dir)
        if mostrar_recetas(ruta_recetas) == None:
            return
        else:
            receta = seleccion_usuario(ruta_recetas, Path.is_file, 'receta', 'archivos')
            receta.unlink()
            limpiar_pantalla()
            print("\nReceta borrada con exito")
            return


def borrar_categoria():
    limpiar_pantalla()
    if mostrar_categorias(ruta_categorias) == None:
        return
    else:
        ruta_recetas = seleccion_usuario(ruta_categorias, Path.is_dir)
        for file in ruta_recetas.glob('**/*'):
            if file.is_file():
                file.unlink()
        ruta_recetas.rmdir()
        print("\nCategoria borrada con exito")
        limpiar_pantalla()
        # Regresar al menu

def cerrar_programa():
    return False

#----------- Programa Main -----------

programa_continua = True
ruta_categorias = creacion_carpetas_default()
while programa_continua == True:
    limpiar_pantalla()
    print(ruta_categorias)
    bienvenida()
    contador_recetas(ruta_categorias)
    mostrar_menu()
    programa_continua = seleccion_menu()
    limpiar_pantalla()
    print("*" * 33)
    print("* Gracias por usar RecipeMaster *")
    print("*" * 33)