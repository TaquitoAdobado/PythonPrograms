import os   #Se importa el OS  para poder limpiar la pantalla. Cuando se llame usa 'cls' si el os.name =="nt" para windows o 'clear' para otro so (Linux/MAC)

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
    View_Tasks(task_list)
    while True:
        try:
            ed_task=int(input("\nWich task do you want to edit? \ninsert number or insert '0' to cancel: "))
            if ed_task == 0:
                os.system("cls" if os.name=="nt" else "clear")
                break
            elif 1<=ed_task<=len(task_list):
                print("\nEditing task","'"+task_list[ed_task -1]+"'", "to: ", end="")
                task_list[ed_task-1]=input("")
                View_Tasks(task_list)
                print("\nThe task has been edited successfully")
                while True:
                    try:
                        edit_more=input("\nDo you want to edit another task? (y/n): ").lower()
                        if edit_more=="n":
                            os.system("cls" if os.name=="nt" else "clear")
                            return
                        elif edit_more=="y":
                            View_Tasks(task_list)
                            break
                        else:
                            View_Tasks(task_list)
                            print("\nInvalid input, please try again...")
                    except ValueError:
                        View_Tasks(task_list)
                        print("\nInvalid input, please try again...")
            else:
                View_Tasks(task_list)
                print("\nTask", ed_task, "doesn't exist, please try again...")
        except ValueError:
            View_Tasks(task_list)
            print("\nInvalid input, please try again...")

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
                                continue
                else:
                    while True:
                            unmark=input("\nTask already marked, do you want to unmark? (y/n): ").lower()
                            if unmark=="y":
                                print(task_list[marked_task-1])
                                task_list[marked_task-1]=task_list[marked_task-1].replace("✔ ","")
                                print(task_list[marked_task-1])
                                View_Tasks(task_list)
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

#La función main será donde se ejecutará todo el programa
def main(menu_list, task_list):
    os.system("cls" if os.name=="nt" else "clear")
    while True:
        main_menu(menu_list)
        try:
            user_choice=int(input("\nPlease insert the number option you want or insert 0 to see menu again or: "))
            if 0<=user_choice<=5:
                mapping_menu[user_choice](task_list)
            elif user_choice==6:
                break
            else:
                print("\nThe option", user_choice, "doesn't exist. Please try again...")
        except ValueError:
            print("\nInvalid answer please try again...")
    print("\nClosing program, until next time :D/")
    return
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Se crea la lista menu_list, al final de cada opcion tiene los espacios necesarios con su "|" para cuadrar con la interfaz.
menu_list = ["1: View Tasks         |", "2: Add Task           |", "3: Edit Task          |", "4: Mark Task          |", "5: Delete Task        |", "6: Close Program      |"]

task_list=[]    #Se crea la lista task_list. En esta lista se almacenarán todas las tareas registradas por el usuario.

mapping_menu = {    #mapeo entre las opciones de la lista 'menu_list' y las funciones de cada opción seleccionada
    1: View_Tasks,
    2: Add_Task,
    3: Edit_Task,
    4: Mark_Task,
    5: Delete_Task
    }

main(menu_list, task_list)  #Llamamos a la funcion main, la cual contiene el proceso del programa.

