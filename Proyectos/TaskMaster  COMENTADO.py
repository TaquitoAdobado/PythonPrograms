import json #Importamos el modulo json para poder hacer una copia de seguridad en un archivo de texto tipo json
import os   #Importamos modulo os para poder limpiar la pantalla. Cuando se llame usa 'cls' si el os.name =="nt" para windows o 'clear' para otro so (Linux/MAC)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Esta funcion guardrá las tareas registradas en un archivo JSON
def Save_Tasks(task_list, filename="TaskMaster List.json"):  #Se define la funcion con sus argumentos, file name contiene el nombre default del archivo json que se creará
    with open(filename, "w") as file:#Se abre el archivo filename en modo escritura (w), with asegura que el archivo se cierre despues de usarse, file es una referencia al archivo abierto.
        json.dump(task_list, file) #Esta linea convierte la task_list en formato json y la escribe en el archivo file referenciado en la linea anterior.

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Esta funcion cargará las tareas desde un archivo JSON
def Load_Tasks(filename="TaskMaster List.json"):#Se define la funcion y se usa de argumento el filename con el nombre del archivo que cargaremos.
    try:       #Ejecutamos un try, mientras no haya un error en su bloque, no pasaremos al except.
        with open(filename, 'r') as file:   #abrimos el archivo filename name en modo lectura (r), with asegura que el archivo se cierre despues de usarse, file es una referencia al archivo abierto. 
            return json.load(file)  #En esta linea se lee el contenido de file y lo convierte de JSON a una lista de Python usando json.load.
                                    #Si el archivo se lee correctamente, finaliza la función.
    except FileNotFoundError:   #FileNotFoundError ocurre si el archivo filename no existe.
        return []   #Si filename no existe, la funcion devuelve una lista vacia '[]', de tal forma que el programa funcione sin interrumpirse.

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#La funcion main_menu crea la interfaz en la que se muestra la bienvenida al programa y un menú con diferentes opciones las cuales serán las de la lista menu_list
# 1: View Tasks 
# 2: Add Task 
# 3: Edit Task 
# 4: Mark Task 
# 5: Delete Task
def main_menu(menu_list):
    print("+", "----------"*3, "+", sep="")     #+------------------------------+
    print("|    Welcome to TaskMaster     |")   #|    Welcome to TaskMaster     |
    print("+", "----------"*3, "+", sep="")     #+------------------------------+

    for option in menu_list:
        print("|       ", option)               #|    opciones del menu         |
    print("+", "----------"*3, "+", sep="")     #+------------------------------+

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Esta funcion realizará la accion de la opcion 1: View Task
def View_Tasks(task_list):
    os.system("cls" if os.name=="nt" else "clear")  #Limpiamos pantalla. (Esto pasará cada que llamemos a esta funcion)
    if len(task_list)==0:
        print("+", "----------"*3, "+", sep="")        #+------------------------------+
        print("|          Task list:          |")      #|          Task list:          |
        print("+", "----------"*3, "+", sep="")        #+------------------------------+
        print("\n          empty list")                #          empty list
    else:
        print("+", "----------"*3, "+", sep="")
        print("|          Task list:          |")      #Se muesta la misma interfaz de task list
        print("+", "----------"*3, "+", sep="")
        number_task=1                                  #asignamos una variable el valor 1 (el numero será el numero de tarea para cada task)
        for task in task_list:                         #Para cada valor en la task list
            print(str(number_task)+":", task)          #se imprime el numero (empezando por 1) + la tarea en la lista, asi con cada iteracion
            number_task+=1                             #Le sumamos 1 la variable par que con cada iteracion el numero sea uno consecutivo

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Esta funcion realizará la accion de la opción 2: Add Task
def Add_Task(task_list):
    View_Tasks(task_list)                                             #Limpiamos la pantalla y mostramos las tareas actuales
    while True:                                                       #iniciamos un bucle
        new_task=input("\nInsert new Task or insert '0' to return: ") #Solicitamos al usuario ingresar una nueva task o insertar 0 para regresar al menu inicial
        if new_task== "0":                                            #Si el usuario ingresó 0:
            os.system("cls" if os.name=="nt" else "clear")            #Limpiamos pantalla
            return                                                    #Salimos de la funcion hacia el menu principal
        else:                                                         #Si el usuario no insertó '0', insertó una nueva tarea
            task_list.append(new_task)                                #Se agrega la nueva tarea al final de la lista
            View_Tasks(task_list)                                     #Se limpia pantalla y mostramos las tareas actuales
            print("\nThe task:", new_task + "\nhas been added")       #Mostramos mensaje de que la tarea se ha añadido
            Save_Tasks(task_list)                                     #Guardamos la tasklist en un archivo json
            while True:                                               #Si el usuario añadió una tarea nueva, iniciamos un bucle nuevo:
                    add_new=input("\nDo you want to add another task? (y/n): ").lower() #Se le pregunta al usuario si quiere agregar algo mas (se guarda la respuesta en minuscula)
                    if add_new=="n":                                    #Si la respuesta es 'n'
                        os.system("cls" if os.name=="nt" else "clear")  #Limpiamos la pantalla
                        return                                          #Regresamos al menu de inicio
                    elif add_new=="y":                                  #Si la respuesta es 'y':
                        View_Tasks(task_list)                           #Limpiamos pantalla, mostramos la task list actual
                        break                                           #Salimos de este bucle y regresamos al bucle de insertar nueva tarea
                    else:                                               #Si se ingresó algo diferente a 'y' o 'n':
                        View_Tasks(task_list)                           #Limpiamos pantalla, mostramos task list actual
                        print("\nInvalid input, please try again...")   #Advertimos que se ingresó una entrada invalida que lo intente de nuevo y se repite este bucle

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Esta función realizará la accion de la opción 3: Edit Task
def Edit_Task(task_list):
    View_Tasks(task_list)           #Cuando llamamos a la funcion editar, limpiamos la pantalla y mostramos la task list actual
    while True:                     #Iniciamos un bucle
        try:
            ed_task=int(input("\nWich task do you want to edit? \ninsert number or insert '0' to cancel: "))    #Se pregunta que tarea se quiere editar y se almacena valor en una variable
            if ed_task == 0:                                        #Si el valor ingresado es 0:
                os.system("cls" if os.name=="nt" else "clear")      #Limpiamos pantalla
                return                                              #Regresamos al menu inicial
            elif 1<=ed_task<=len(task_list):                               #Si se ingresa un numero tarea dentro del rango de tareas que existe:
                print("\nEditing task","'"+task_list[ed_task -1]+"'", "to: ", end="")   #Mostramos un mensaje de que editaremos una trea, usamos ed_task -1 ya que hacemos alucion a la posicion en la lista
                task_list[ed_task-1]=input("")                                          #Se sobreescribirá la tarea elegida por lo que ingrese el usuario
                View_Tasks(task_list)                                                   #Limpiamos pantalla y mostramos lista de tareas actuales
                Save_Tasks(task_list)                                                   #Guardamos la tasklist en un archivo json
                print("\nThe task has been edited successfully")                        #Mostramos mensaje de tarea editada exitosamente (mero adorno)
                while True:                                                             #Iniciamos nuevo bucle:
                        edit_more=input("\nDo you want to edit another task? (y/n): ").lower()  #Se pregunta si quiere editar otra tarea
                        if edit_more=="n":                                                      #Si se ingresa 'n'
                            os.system("cls" if os.name=="nt" else "clear")                      #Limpiamos pantalla
                            return                                                              #Regresamos al menu inicial
                        elif edit_more=="y":                                                #Si se ingresa 'y':
                            View_Tasks(task_list)                                           #Limpiamos pantalla, mostramos lista de tareas actuales
                            break                                                           #Salimos de este bucle y regresamos al bucle anterior
                        else:                                                           #Si se ingresa algo diferente a 'n' o 'y':
                            View_Tasks(task_list)                                       #Limpuamos pantalla, mostramos lista de tareas actuales
                            print("\nInvalid input, please try again...")               #Se muestra mensaje de entrada invalida y se repite el bucle
            else:                                                           #Si se ingresa un numero de tarea fuera del rango de tareas que existe:
                View_Tasks(task_list)                                       #Se limpia pantalla y muestran tareas actuales
                print("\nTask", ed_task, "doesn't exist, please try again...")#Se muestra mensaje avisando que la tarea no existe y se repite el bucle
        except ValueError:                                                   #Si se ingresa una entrada de otro tipo (como str)
            View_Tasks(task_list)                                            #Se limpia pantalla y muestran tareas actuales
            print("\nInvalid input, please try again...")                    #Se muestra mensaje de entrada invalida y se repite el bucle

#--------------------------------------------------------------------------------------------------------------------------------------------------------
def Mark_Task(task_list):
    if len(task_list)==0:
        View_Tasks(task_list)
        return
    else:
        View_Tasks(task_list)
    while True:
        try:
            print("\nWich task do you want to mark?. \nIf you select a task marked, you can unmark it.")
            marked_task=int(input("\ninsert number or insert '0' to cancel: "))
            if marked_task==0:
                os.system("cls" if os.name=="nt" else "clear")
                return
            elif 1<=marked_task<=len(task_list):
                if "✔" not in task_list[marked_task-1]:
                    task=task_list[marked_task-1]
                    task_list[marked_task-1]= "✔ "+ task
                    View_Tasks(task_list)
                    Save_Tasks(task_list)
                    print("\nThe task has been marked")
                    while True:
                            mark_again=input("\nDo you want to mark another task? (y/n): ").lower()
                            if mark_again=="n":
                                os.system("cls" if os.name=="nt" else "clear")
                                return
                            elif mark_again=="y":
                                View_Tasks(task_list)
                                break
                            else:
                                View_Tasks(task_list)
                                print("\nInvalid input please try again...")
                else:
                    while True:
                            unmark=input("\nTask already marked, do you want to unmark? (y/n): ").lower()
                            if unmark=="y":
                                print(task_list[marked_task-1])
                                task_list[marked_task-1]=task_list[marked_task-1].replace("✔ ","")
                                View_Tasks(task_list)
                                Save_Tasks(task_list)
                                print("\nThe task has been unmarked successfully")
                                break
                            elif unmark=="n":
                                os.system("cls" if os.name=="nt" else "clear")
                                return
                            else:
                                View_Tasks(task_list) 
                                print("\nInvalid input please try again...")
            else:
                View_Tasks(task_list)
                print("\nTask doesn't exist, please try again...")
        except ValueError:
            View_Tasks(task_list)
            print("\nInvalid input please try again...")
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Esta funcion realizará la accion de la opción 5: Delete Task
def Delete_Task(task_list):
    if len(task_list)==0:
        View_Tasks(task_list)
        return
    else:
        View_Tasks(task_list)
        while True:
            try:
                del_task=int(input("\nWich task do you want to delete? \ninsert number or insert '0' to cancel: "))
                if del_task==0:
                    os.system("cls" if os.name=="nt" else "clear")
                    return
                elif 1<=del_task<=len(task_list):
                    del task_list[del_task-1]
                    View_Tasks(task_list)
                    Save_Tasks(task_list)
                    print("\nThe task been deleted successfully") 
                    while True:
                        del_more=input("\nDo you want to delete another task? (y/n): ").lower()
                        if del_more=="n":
                            os.system("cls" if os.name=="nt" else "clear")
                            return
                        elif del_more=="y":
                            if len(task_list)==0:
                                View_Tasks(task_list)
                                return
                            else:
                                View_Tasks(task_list)
                                break
                        else:
                            View_Tasks(task_list)
                            print("\nInvalid input, please try again...")
                else:
                    View_Tasks(task_list)
                    print("\nTask", del_task, "doesn't exist, please try again...")
            except ValueError:
                View_Tasks(task_list)
                print("\nInvalid input, please try again...")
                
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#La función main() será donde se ejecutará todo el programa.
def main(menu_list, task_list):
    os.system("cls" if os.name=="nt" else "clear")      #Al iniciar el programa limpiamos patalla
    while True:                                         #Iniciamos un bucle
        main_menu(menu_list)                            #Mostramos el menu de inicio
        try:
            user_choice=int(input("\nPlease insert the number option you want: ")) #Se pide al usuario ingresar una opcion del menu
            if 1<=user_choice<=5:                   #El menu tiene 5 opciones, si se elige una entre 1-5:
                option_menu[user_choice](task_list) #Usando la key 1-5 llamamos al value, que será una funcion, escribimos el argumento (task_list) que usara la funcion.
            elif user_choice==6:                         #Si el usuario ingresa 6:
                Save_Tasks(task_list)
                break                                    #Salimos del bucle por lo que salimos del programa y se imprime mensaje de despedida
            else:                                                                      #Si se escribe un numero fuera del rango 1-5:
                print("\nThe option", user_choice, "doesn't exist. Please try again...")#Avisamos que esa opcion no existe
        except ValueError:                                          #Si se ingresa una entrada con tipo diferente (como str)
            print("\nInvalid answer please try again...")           #Avisamos de entrada invalida y repetimos el bucle
    print("\nClosing program, until next time :D/")     #Mensaje de despedida
    return                                              #Salimos del programa
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Al iniciar el programa se empieza por:
if __name__ == "__main__" :#asegura que el código dentro de este bloque solo se ejecute cuando el archivo se ejecuta directamente.
    #Se crea la lista menu_list, al final de cada opcion tiene los espacios necesarios con su "|" para cuadrar con la interfaz.
    menu_list = ["1: View Tasks         |", "2: Add Task           |", "3: Edit Task          |", "4: Mark Task          |", "5: Delete Task        |", "6: Close Program      |"]
    #Se crea la lista task_list. En esta lista se almacenarán todas las tareas registradas por el usuario.
    task_list=Load_Tasks() #Cargamos el archivo JSON con tareas guardadas anteriormente
    if not task_list:
        task_list=[]    

    #Se crea el diccionario con las funciones para el menu
    option_menu = {     #El diccionario contendra las funciones del programa que se llamaran a eleccion del usuario
        1: View_Tasks,  # Se escriben las funciones sin () ni parametros, ya que esos se programan al llamarse en el codigo
        2: Add_Task,
        3: Edit_Task,
        4: Mark_Task,
        5: Delete_Task
        }

    #Se ejecuta la funcion main donde entraremos en bucle hasta que el usuario decida salir del programa.
    main(menu_list, task_list)  #La cual contiene el proceso del programa.