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
        print("|       ", option)               #|      opcion del menu         |
    print("+", "----------"*3, "+", sep="")     #+------------------------------+

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Esta funcion realizará la accion de la opcion 1: View Task
def View_Tasks(task_list):
    number_task=1
    if len(task_list)==0:
        print("\nempty list")
    else:
        for task in task_list:
            print(str(number_task)+":", task)
            number_task+=1

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Esta funcion realizará la accion de la opción 2: Add Task
def Add_Task(task_list):
    while True:
        new_task=input("\nInsert new Task or insert 'R' to return: ")
        new_task_lower=new_task.lower()
        if new_task_lower== "r":
            break
        else:
            task_list.append(new_task)
            print("\nThe task:", new_task + "\nhas been added")

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Esta funcion realizará la accion de la opción 5: Delete Task
def Delete_Task(task_list):
    while True:
            print("+", "----------"*3, "+", sep="")
            print("|Task list:                    |")
            print("+", "----------"*3, "+", sep="")
            View_Tasks(task_list)
            try:
                del_task=int(input("\nWich task do you want to delete? \ninsert number or '0' to cancel: "))
                if del_task==0:
                    break
                elif 1<=del_task<=len(task_list):
                    print("\nTask:", task_list[del_task-1] + "\nhas been deleted \n")
                    del task_list[del_task-1]
                    stop_del=input("Do you want to delete another task? (Y/N): ")
                    stop_del_low=stop_del.lower()
                    if stop_del_low=="n":
                        break
                    elif stop_del_low=="y":
                        continue
                    elif len(task_list)==0:
                        print("The task list is already empty, returning to main menu...")
                        break
                else:
                    print("\nTask", del_task, "doesn't exist, please try again...")
            except ValueError:
                print("\nInvalid input, please try again...")
                
#--------------------------------------------------------------------------------------------------------------------------------------------------------

#La función main será donde se ejecutará todo el programa
def main(menu_list, task_list):
    main_menu(menu_list)
    while True:
        try:
            user_choice=int(input("\nPlease insert the number option you want or insert 0 to see menu again: "))
            if 0<=user_choice<=5:
                if user_choice==0:
                    main_menu(menu_list)
                elif user_choice==1 or 2 or 5:
                    mapping_menu[user_choice](task_list)
            else:
                print("The option", user_choice, "doesn't exist. Please try again...")
        except ValueError:
            print("Invalid answer please try again...")

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Se crea la lista menu_list, al final de cada opcion tiene los espacios necesarios con su "|" para cuadrar con la interfaz.
menu_list = ["1: View Tasks         |", "2: Add Task           |", "3: Edit Task          |", "4: Mark Task          |", "5: Delete Task        |"]

task_list=[]    #Se crea la lista task_list. En esta lista se almacenarán todas las tareas registradas por el usuario.

mapping_menu = {    #mapeo entre las opciones de la lista 'menu_list' y las funciones de cada opción seleccionada
    1: View_Tasks,
    2: Add_Task,
    5: Delete_Task

    }

main(menu_list, task_list)  #Llamamos a la funcion main, la cual contiene el proceso del programa.

