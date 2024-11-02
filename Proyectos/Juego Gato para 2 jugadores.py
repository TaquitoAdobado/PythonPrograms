#En esta funcion dibujamos la cuadricula 3x3 que se usará como tablero de juego
def display_board(board):
    for fila in range(len(board)):
        print("+-------" * 3+"+")
        print("|"+"       |" *3, end="\n|")
        for columna in range(len(board)):
            print("  ",str(board[fila][columna]),"  |",end="")
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
            print("Nombre de usuario ocupado, ingrese uno diferente")  #Avisamos el nombre ingresado ya está ocupado, que ingrese uno diferente.
        else: break # Si los nombres no son iguales, continuamos explicando el juego
    print(player_1, "marcará las casillas con una 'X'", "y", player_2, "las marcará con una 'O'")
    print("Ganará el primero en conseguir una linea de 3")
    print("\n EMPECEMOS!!! \n")
    return player_1, player_2
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Mapeo de casillas a indices, cada numero del 1 al 9 representa a una casilla
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
    if draw(board) ==False: #Si aun hay casillas libres (no es empate)
        print("Es tu turno", player)  #Empezamos el turno del jugador definido al llamar a la funcion player_turn 
        while True: #Empezamos un bucle que contendrá el turno
            print(player, end="")
            try:    #Hacemos uso del try ya que pediremos que se ingrese un numero entero, en caso de ingresar otra cosa, se ejecutará el except
                casilla = int(input(" ¿Que numero de casilla quieres marcar? (1-9): "))
                if 1<=casilla<=9:   #Si el numero ingresado esta dentro del rango permitido, se continua
                    fila, columna = cell_mapping[casilla]   #El numero ingresado corresponderá a una key del diccionario cell_mapping
                                                            #Por lo que su clave se asignará a los parametros fila y columna los cuales se interpretarán mas adelante
                                                            #como la posición dentro de la lista board. board[fila][columna]
                    if board[fila][columna] not in ["X", "O"]: #Se revisa que la posición en board[fila][columna], no sea X ó O, si no es, continua
                        board[fila][columna]= mark    #Se sustituye el valor de la posicion de board[fila][columna] por la marca (X ó O) definida al llamar a la funcion.
                        break   #Salimos del bucle while True, por lo que termina el turno del jugador actual
                    else: #Si la posicón en board[fila][columna] si es X ó O, se le avisa al jugador que ya está ocupada esa posición
                        print("Esa casilla ya se encuentra ocupada")    #Mensaje de aviso, casilla ocupada.
                else:   #Si el numero ingresado no está dentro del rango permitido de casillas, avisamos al jugador
                    print("Ese numero de casilla no existe") #Mensaje para cuando el jugador ingresa un numero fuera de rango del 1 al 9
            except ValueError:  #Except de ValueError para cuando no se ingrese un numero entero en el try
                print("Ingresa un numero valido")   #Mensaje de error
        return True #Retornamos un True cuando se ejecuta el turno de un jugador    
    else:
        return False    #Retornamos un False cuando NO se ejecutó el turno del jugador
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
def game(player_1, player_2):
    juego_en_curso=True
    while juego_en_curso:   #Mientras juego_en_curso=True el juego continua
        if player_turn(board,player_1, "X")==False:    #Si el turno del jugador NO se ejecutó, es porque es un empate.
            print("Es un empate, ganó la amistad!!!")
            juego_en_curso = False
            break   #Salimos del ciclo y termina el juego
        #Si el turno del jugador Si se ejecutó continuamos a la siguiente linea.
        elif verify_victory(board, "X"):  #Si el jugador con el simbolo X cumple una condicion de victoria de la funcion verify_victory:
            print("\n El ganador es...", player_1, "!!!")  #Se imprime mensaje anunciando al ganador
            juego_en_curso=False    
            break   #Salimos del bucle y termina el juego
        #Si el jugador anterior no ganó:
        elif player_turn(board, player_2, "O")==False: #Si el turno del jugador NO se ejecutó, es porque es un empate.
            print("Es un empate, ganó la amistad!!!")
            juego_en_curso = False
            break   #Salimos del bucle y termina el juego
        #Si el turno del jugador Si se ejecutó continuamos a la siguiente linea.
        elif verify_victory(board, "O"):  #Si el jugador con el simbolo O cumple una condicion de victoria de la funcion verify_victory:
            print("\n El ganador es...", player_2, "!!!")  #Se imprime mensaje anunciando al ganador
            juego_en_curso=False   
            break   #Salimos del bucle y termina el juego
    return juego_en_curso
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
board=[[c+f*3 for c in range(1,4)] for f in range(3)]   #Se numeran casillas del tablero 3x3 del 1 al 9
# Iniciamos el juego con un titulo:
print("-----------------------------------------")
print("Lets play TicTacToe, whats your username?")
print("-----------------------------------------")

player_1, player_2 = username_selection()
game(player_1, player_2) #Se llama a la funcion game(), el juego iniciará y se le pedirá al jugador elegir una casilla para marcarla.
       
display_board(board)    #Se muestra el tablero con el resultado final
print("JUEGO TERMINADO!")