import os
from os import system
from pathlib import Path

#-----------------------Auxiliar functions-----------------------
def show_menu(menu_list):
    for option in menu_list:
        print(option)

def select_menu_option(menu_list):
    while True:
        try:
            user_menu_choice = int(input("\nChoose the option number: "))
            system("cls" if os.name == "nt" else "clear")
            if 1 <= user_menu_choice <= len(menu_list):
                return user_menu_choice
            else:
                system("cls" if os.name == "nt" else "clear")
                show_menu(menu_list)
                print("\nOption doesn't exist please try again...")
        except ValueError:
            system("cls" if os.name == "nt" else "clear")
            show_menu(menu_list)
            print("\nInvalid answer please try again...")

def show_categories(categories_route):
    categories = []
    number=1    #Indice de cada categoria (será incremental)
    for directory in categories_route.glob('*'):
        if directory.is_dir():
            print(number,":",directory.name)
            categories.append(directory)
            number+=1
    return categories   #Lista de categorias

def select_category(categories):
    while True:
        try:
            user_choice = int(input("\nChoose the category number: "))
            system("cls" if os.name == "nt" else "clear")
            if 1 <= user_choice <= len(categories):
                category_selected= Path(categories_rute, categories[user_choice - 1])
                return category_selected    #Retorna Path a la categoria seleccionada
            else:
                system("cls" if os.name == "nt" else "clear")
                show_categories(categories_rute)
                print("\nOption doesn't exist please try again...")
        except ValueError:
            system("cls" if os.name == "nt" else "clear")
            show_categories(categories_rute)
            print("\nInvalid answer please try again...")

def show_recipes(categories_rute):
    categories = show_categories(categories_rute)   #Lista de categorias
    category_selected = select_category(categories) #Path de la categoria seleccionada
    recipes = []    #Lista de recetas
    number = 1  #Indice de cada receta
    for recipe in category_selected.glob('*.txt'):
        print(number,":",recipe.stem)
        recipes.append(recipe.stem)
        number += 1
    return category_selected, recipes   #Retorna Path a las recetas y lista de recetas

def recipes_list(recipes):
    system("cls" if os.name == "nt" else "clear")
    number = 1  # Indice de cada receta
    for recipe in recipes:
        print(number, ":", recipe)
        number += 1

def goto_menu():
    while True:
        user_ret_button = input("\nPress any button to return to the menu: ").lower()
        system("cls" if os.name == "nt" else "clear")
        if type(user_ret_button) is str:
            return

'''-----------------------------------------------------------'''
#-------------------------Menu functions-------------------------
def read_recipe():
    category_selected, recipes = show_recipes(categories_rute)  #Path a recetas y lista de recetas
    if len(recipes) == 0:
        print("\nThere are no recipes yet, please create some first")
        goto_menu()
    else:
        while True:
            try:
                user_recipe_choice = int(input("\n Which recipe do you want to read?: "))
                system("cls" if os.name == "nt" else "clear")
                if 1 <= user_recipe_choice <= len(recipes):
                    recipe_selected = Path(category_selected, recipes[user_recipe_choice -1] + '.txt')
                    print(recipe_selected.read_text())
                    goto_menu()
                    return
                else:
                    recipes_list(recipes)
                    print("\nOption doesn't exist please try again...")
            except ValueError:
                recipes_list(recipes)
                print("\nInvalid answer please try again...")

def create_recipe():
    category_selected, recipes = show_recipes(categories_rute)  #Path a recetas y lista de recetas
    while True:
        try:
            new_recipe = Path(category_selected, input("\nEnter the new recipe name: ") + '.txt')
            system("cls" if os.name == "nt" else "clear")
            new_recipe.touch(exist_ok=False)    #Si existe: FileExistsError
            recipe_content = ""
            print("\nIngress the recipe or type 'end' to finish:\n")
            while True:
                line = input()
                if line.lower() == "end":
                    break
                else:
                    recipe_content += line + "\n"
            new_recipe.write_text(recipe_content)
            print("\nRecipe created successfully!")
            goto_menu()
            return
        except FileExistsError:
            recipes_list(recipes)
            print("\nRecipe already exists, please try again...")

def create_category():
    show_categories(categories_rute)
    while True:
        try:
            new_category = Path(categories_rute, input("\nEnter the new category name: "))
            system('cls' if os.name == 'nt' else 'clear')
            new_category.mkdir(exist_ok=False)  #Si existe: FileExistsError
            print("\nCategory created successfully!")
            goto_menu()
            return
        except FileExistsError:
            show_categories(categories_rute)
            print("\nCategory already exists, please try again...")

def delete_recipe():
    category_selected, recipes = show_recipes(categories_rute)  # Path a recetas y lista de recetas
    if len(recipes) == 0:
        print("\nThere are no recipes yet, please create some first")
        goto_menu()
    else:
        while True:
            try:
                user_recipe_choice = int(input("\n Which recipe do you want to delete?: "))
                system("cls" if os.name == "nt" else "clear")
                if 1 <= user_recipe_choice <= len(recipes):
                    recipe_selected = Path(category_selected, recipes[user_recipe_choice - 1] + '.txt')
                    recipe_selected.unlink()
                    print("\nRecipe deleted successfully!")
                    goto_menu()
                    return
                else:
                    recipes_list(recipes)
                    print("\nOption doesn't exist please try again...")
            except ValueError:
                recipes_list(recipes)
                print("\nInvalid answer please try again...")

def delete_category():
    categories = show_categories(categories_rute)  # Lista de categorias
    if len(categories) == 0:
        print("\nThere are no categories yet, please create some first")
        goto_menu()
        return
    else:
        print("\nWhich category do you want to delete?")
        category_selected = select_category(categories)  # Path de la categoria seleccionada
        category_selected.rmdir()
        print("\nCategory deleted successfully!")
        goto_menu()
        return
#--------------------------Program code--------------------------
menu_list = [
    "1 : Read recipe",
    "2 : Create recipe",
    "3 : Create category",
    "4 : Delete recipe",
    "5 : Delete category",
    "6 : Close program"
    ]
menu_options = {
    1: read_recipe,
    2: create_recipe,
    3: create_category,
    4: delete_recipe,
    5: delete_category,
}
#Creacion de directorios si no existen
categories_rute = Path(Path.home(),'RecipeMaster', 'Proyecto_Recetario/Recetas')
if not categories_rute.exists():
    categories_rute.mkdir(parents=True)
    default_categories = ['Carnes', 'Ensaladas', 'Pastas', 'Postres']
    for category in default_categories:
        Path(categories_rute, category).mkdir()

#Loop principal del programa
while True:
    print("\nWelcome to RecipeMaster\n")
    show_menu(menu_list)
    user_menu_choice = select_menu_option(menu_list)
    if user_menu_choice == 6:
        break
    else:
        menu_options[user_menu_choice]()
system("cls" if os.name == "nt" else "clear")
print("\nClosing program, until next time :D/")