#En esta funcion dibujamos la cuadricula 3x3 que se usará como tablero de juego
def display_board(board):
    for row in range(len(board)):
        print("+-------" * 3+"+")
        print("|"+"       |" *3, end="\n|")
        for column in range(len(board)):
            print("  ",str(board[row][column]),"  |",end="")
        print("\n|"+"       |"*3)
    print("+-------" * 3+"+")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Esta funcion se usará para registrar el username de los 2 jugadores. No se puede tener 2 nombres iguales
def username_selection():
    player_1=input("Insert Player 1 username: ") #Se le pide al jugador 1 ingresar su username
    player_1_lower=player_1.lower()   #Convertimos a minuscula el nombre ingresado para fines de comparacion futura
    while True:
        player_2=input("Insert Player 2 username: ") #Se le pide al jugador 2 ingresar su username
        player_2_lower=player_2.lower()   #Convertimos a minuscula para fines de comparacion
        if player_2_lower==player_1_lower:  #Si los nombres de usuario en minuscula son iguales
            print("The username must be different from Player 1. Please try again.")  #Avisamos el nombre ingresado ya está ocupado, que ingrese uno diferente.
        else: break # Si los nombres no son iguales, continuamos explicando el juego
    print(player_1, "will mark the squares with an 'X'","and", player_2, "with an 'O'.")
    print("The first player to get three in a row wins.")
    print("if all 9 squares are filled and no players has three in a row, the game ends in a draw.")
    print("\n LETS START!!! \n")
    return player_1, player_2   #Retornamos los nombres de usuarios
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Mapeo de casillas a indices, cada numero del 1 al 9 representa a una casilla, el primer numero es la fila y el segundo la columna
cell_mapping = {
    1: (0,0), 2: (0,1), 3: (0,2),
    4: (1,0), 5: (1,1), 6: (1,2),
    7: (2,0), 8: (2,1), 9: (2,2)
}
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Esta función determinará si el juego es un empate
def draw(board):
    board=str(board)
    count=0       #Definimos una variable con valor 0
    for n in range(1,10):   # para n del 1 al 9
        if str(n) not in board:      # Si n no está en la lista de la cuadricula
            count+=1  # La variable count = count +1   
    if count==9:        # Cuando count=9 significa que en la lista del tablero ya no hay posiciones libres
        return True     # Regresamos un True de que ya no hay casillas disponibles
    else:               # Si es diferente a 9, significa que aun pueden elegir una casilla el jugador.
        return False    # Regresamos un False de que todavia hay casillas disponibles
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Esta funcion verificará las condiciones para ganar. mark será la marca de cada jugador (X ó O). Se llamará  a la funcion despues del turno de cada jugador.
def verify_victory(board, mark):
    if (board[0][0]==board[0][1]==board[0][2] == mark or    #horizontales: casilla 1, 2, 3   
    board[1][0]==board[1][1]==board[1][2] == mark or        #              casilla 4, 5, 6
    board[2][0]==board[2][1]==board[2][2] == mark or        #              casilla 7, 8, 9
    board[0][0]==board[1][0]==board[2][0] == mark or        #verticales:                   casilla 1, 4, 7
    board[0][1]==board[1][1]==board[2][1] == mark or        #                              casilla 2, 5, 8
    board[0][2]==board[1][2]==board[2][2] == mark or        #                              casilla 3, 6, 9
    board[0][0]==board[1][1]==board[2][2] == mark or        #diagonales:    casilla 1, 5, 9
    board[0][2]==board[1][1]==board[2][0] == mark):         #               casilla 3, 5, 7
        return True
    else:
        return False
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    #En esta funcion se programará el turno de un jugador con parametro player. Al tener ese parametro funcionará para los 2 jugadores
    #usamos tambien el parametro board ya que se ocupa la lista board y el parametro mark que será la X ó O que usará el jugador
def player_turn (board, player, mark):
    display_board(board)   #Mostramos el tablero actualizado llamando a su funcion   
    if draw(board) ==False: #Llamando a la funcion draw, Si aun hay casillas libres (no es empate) 
        print("Its your turn", player)  #Empezamos el turno del jugador definido al llamar a la funcion player_turn 
        while True: #Empezamos un bucle que contendrá el turno
            print(player,"", end="")
            try:    #Hacemos uso del try ya que pediremos que se ingrese un numero entero, en caso de ingresar otra cosa, se ejecutará el except
                casilla = int(input("Which square do you want to mark? (1-9): "))
                if 1<=casilla<=9:   #Si el numero ingresado esta dentro del rango permitido, se continua
                    row, column = cell_mapping[casilla]   #El numero ingresado corresponderá a una key del diccionario cell_mapping
                                                            #Por lo que su clave se asignará a los parametros fila y columna los cuales se interpretarán mas adelante
                                                            #como la posición dentro de la lista board. board[fila][columna]
                    if board[row][column] not in ["X", "O"]: #Se revisa que la posición en board[fila][columna], no sea X ó O, si no es, continua
                        board[row][column]= mark    #Se sustituye el valor de la posicion de board[fila][columna] por la marca (X ó O) definida al llamar a la funcion.
                        break   #Salimos del bucle while True, por lo que termina el turno del jugador actual
                    else: #Si la posicón en board[fila][columna] si es X ó O, se le avisa al jugador que ya está ocupada esa posición
                        print("That square is already marked, please choose another one.")    #Mensaje de aviso, casilla ocupada.
                else:   #Si el numero ingresado no está dentro del rango permitido de casillas, avisamos al jugador
                    print("That square does not exist.") #Mensaje para cuando el jugador ingresa un numero fuera de rango del 1 al 9
            except ValueError:  #Except de ValueError para cuando no se ingrese un numero entero en el try
                print("Please use a valid number.")   #Mensaje de error
        return True #Retornamos un True cuando se ejecuta el turno de un jugador    
    else:
        return False    #Retornamos un False cuando NO se ejecutó el turno del jugador
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
def game(player_1, player_2):
    game_in_progress=True
    while game_in_progress==True:   #Mientras juego_en_curso=True el juego continua
        if player_turn(board,player_1, "X")==False:    #Si el turno del jugador NO se ejecutó, es porque es un empate.
            print("Its a DRAW!, Friendship won!!!")
            game_in_progress = False  #Variable que indica que el juego terminó
            break   #Salimos del ciclo y termina el juego
        #Si el turno del jugador Si se ejecutó continuamos a la siguiente linea.
        elif verify_victory(board, "X"):  #Si el jugador con el simbolo X cumple una condicion de victoria de la funcion verify_victory:
            print("\n And the winer is...", player_1, "!!!")  #Se imprime mensaje anunciando al ganador
            game_in_progress=False    #Variable que indica que el juego terminó
            break   #Salimos del bucle y termina el juego
        #Si el jugador anterior no ganó:
        elif player_turn(board, player_2, "O")==False: #Si el turno del jugador NO se ejecutó, es porque es un empate.
            print("Its a DRAW!, Friendship won!!!!!!")
            game_in_progress = False  #Variable que indica que el juego terminó
            break   #Salimos del bucle y termina el juego
        #Si el turno del jugador Si se ejecutó continuamos a la siguiente linea.
        elif verify_victory(board, "O"):  #Si el jugador con el simbolo O cumple una condicion de victoria de la funcion verify_victory:
            print("\n And the winer is...", player_2, "!!!")  #Se imprime mensaje anunciando al ganador
            game_in_progress=False   #Variable que indica que el juego terminó
            break   #Salimos del bucle y termina el juego
    return game_in_progress
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Iniciamos el juego con un titulo:
print("-----------------------------------------")
print("Lets play Tic-Tac-Toe, whats your username?")
print("-----------------------------------------")

game_in_progress=True   #Declaramos la varibale game_in_progress como True
while game_in_progress==True:   #Mientras game_in_progress sea True, el juego se ejecutará
    player_1, player_2 = username_selection()   #Se ejecuta funcion para elegir usename
    board=[[c+f*3 for c in range(1,4)] for f in range(3)]   #Se numeran casillas del tablero 3x3 del 1 al 9
    game_in_progress=game(player_1, player_2) #Se llama a la funcion game(), el juego iniciará. Cuando termine, game_in_pogress = False
    display_board(board)    #El juego terminó y se muestra el tablero con el resultado final
    while game_in_progress==False:  #Al estar terminado el juego, se entra en este bucle
        rematch=input("\nDo you want to play again? (y/n): ").lower()  #Se pregunta al usuario si quiere jugar nuevamente (su respuesta se guarda en minuscula)
        if rematch not in ["y","n"]:    #Si el usuario ingresa algo diferente a "y" o "n"
            print("Invalid response, please try again...")  #Se le avisa que ingreso una respuesta invalida, que intente de nuevo
        elif rematch == "y":    #Si el usuario escribe y
            game_in_progress = True #Declaramos game_in_progress como True
            break   #Salimos del bucle (y/n) con game_in_progress= True, por lo que el bucle del juego se ejecutará nuevamente desde la solicitud de usenames
        elif rematch == "n":    #Si el usuario escribe "n"
            break   #Salimos del bucle (y/n) con game_in_progress=False, por lo que tambien se sale del bucle que ejecuta el juego y se imprime la siguiente linea
print("GAME OVER!!!")   #GAME OVER!!! , finaliza el programa.



