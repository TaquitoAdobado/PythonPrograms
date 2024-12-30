import json 
import os   

#Esta funcion guardrá las tareas registradas en un archivo JSON
def Save_Tasks(task_list, filename="TaskMaster List.json"):
    with open(filename, "w") as file:
        json.dump(task_list, file) 

#Esta funcion cargará las tareas desde un archivo JSON
def Load_Tasks(filename="TaskMaster List.json"):
    try:
        with open(filename, 'r') as file: 
            return json.load(file)
    except FileNotFoundError:
        return []
    
#La funcion main_menu crea la interfaz en la que se muestra la bienvenida al programa y un menú con diferentes opciones las cuales serán las de la lista menu_list
def main_menu(menu_list):
    print("+", "----------"*3, "+", sep="")     #+------------------------------+
    print("|    Welcome to TaskMaster     |")   #|    Welcome to TaskMaster     |
    print("+", "----------"*3, "+", sep="")     #+------------------------------+

    for option in menu_list:
        print("|       ", option)               #|    opciones del menu         |
    print("+", "----------"*3, "+", sep="")     #+------------------------------+

#Esta funcion realizará la accion de la opcion 1: View Task
def View_Tasks(task_list):
    os.system("cls" if os.name=="nt" else "clear")  
    if len(task_list)==0:
        print("+", "----------"*3, "+", sep="")        #+------------------------------+
        print("|          Task list:          |")      #|          Task list:          |
        print("+", "----------"*3, "+", sep="")        #+------------------------------+
        print("\n          empty list")                #          empty list
    else:
        print("+", "----------"*3, "+", sep="")
        print("|          Task list:          |")
        print("+", "----------"*3, "+", sep="")
        number_task=1
        for task in task_list:
            print(str(number_task)+":", task)
            number_task+=1

#Esta funcion realizará la accion de la opción 2: Add Task
def Add_Task(task_list):
    View_Tasks(task_list)                                             
    while True:                                                       
        new_task=input("\nInsert new Task or insert '0' to return: ")
        if new_task== "0":
            os.system("cls" if os.name=="nt" else "clear")
            return
        else:
            task_list.append(new_task)
            while True:
                    add_new=input("\nDo you want to add another task? (y/n): ").lower()
                    if add_new=="n":
                        os.system("cls" if os.name=="nt" else "clear")
                        return
                    elif add_new=="y":
                        View_Tasks(task_list)
                        break
                    else:
                        View_Tasks(task_list)
                        print("\nInvalid input, please try again...")

#Esta función realizará la accion de la opción 3: Edit Task
def Edit_Task(task_list):
    View_Tasks(task_list)
    while True:
        try:
            ed_task=int(input("\nWich task do you want to edit? \ninsert number or insert '0' to cancel: "))
            if ed_task == 0:
                os.system("cls" if os.name=="nt" else "clear")
                return
            elif 1<=ed_task<=len(task_list):
                print("\nEditing task","'"+task_list[ed_task -1]+"'", "to: ", end="")
                task_list[ed_task-1]=input("")
                View_Tasks(task_list)
                Save_Tasks(task_list)
                print("\nThe task has been edited successfully")
                while True:
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
            else:
                View_Tasks(task_list)
                print("\nTask", ed_task, "doesn't exist, please try again...")
        except ValueError:
            View_Tasks(task_list)
            print("\nInvalid input, please try again...")

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
                

#La función main() será donde se ejecutará todo el programa.
def main(menu_list, task_list):
    os.system("cls" if os.name=="nt" else "clear")
    while True:
        main_menu(menu_list)
        try:
            user_choice=int(input("\nPlease insert the number option you want: "))
            if 1<=user_choice<=5: #1-5 son las opciones del menú
                option_menu[user_choice](task_list) #Usando la key 1-5 llamamos al value, que será una funcion, escribimos el argumento (task_list) que usara la funcion.
            elif user_choice==6: # La opcion 6 del menu es salir del programa
                Save_Tasks(task_list)
                break
            else:
                print("\nThe option", user_choice, "doesn't exist. Please try again...")
        except ValueError:
            print("\nInvalid answer please try again...")
    print("\nClosing program, until next time :D/")
    return
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Al iniciar el programa se empieza por:
if __name__ == "__main__" :#asegura que el código dentro de este bloque solo se ejecute cuando el archivo se ejecuta directamente.
    
    menu_list = ["1: View Tasks         |", "2: Add Task           |", "3: Edit Task          |", "4: Mark Task          |", "5: Delete Task        |", "6: Close Program      |"]
    
    task_list=Load_Tasks() #Cargamos el archivo JSON con tareas guardadas anteriormente
    if not task_list:
        task_list=[]    

    #Se crea el diccionario con las funciones para el menu
    option_menu = {
        1: View_Tasks,
        2: Add_Task,
        3: Edit_Task,
        4: Mark_Task,
        5: Delete_Task
        }

    Load_Tasks  
    #Se ejecuta la funcion main donde entraremos en bucle hasta que el usuario decida salir del programa.
    main(menu_list, task_list)  #La cual contiene el proceso del programa.