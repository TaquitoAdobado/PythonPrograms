''' pygame es un modulo (externo) que sirve para crear juegos en python'''

import pygame
import random
from pygame import mixer    #Para reproducir sonidos
import io

# Inicializar Pygame
pygame.init()

# pygame.time.Clock() nos permite controlar la velocidad de actualización de la pantalla, usado para controlar los FPS
clock = pygame.time.Clock()

# pygame.key.set_repeat() nos permite controlar la velocidad de repetición de las teclas
pygame.key.set_repeat(100,100)

# Crear una pantalla
''' (800, 600) son las dimensiones de la pantalla en pixeles, se escribe dentro de una tupla. '''
screen = pygame.display.set_mode((800, 600))


#Colores:
''' Los colores se identifican por su tupla de 3 enteros (R, G, B) '''
GREEN = (30, 200, 60)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Título de la ventana
pygame.display.set_caption("Zelda Invaders")


# Icono de la ventana
''' trifuerza.png está dentro de la carpeta del juego, es un png de 32x32 pixeles '''
icon = pygame.image.load("trifuerza.png") #Cargamos la imagen
pygame.display.set_icon(icon)


#Fondo del juego
''' fondo.png esta dentro de la carpeta del juego, es un png de 800x600 pixeles '''
background = pygame.image.load("fondo.png")

def background_game():
    ''' Esta funcion coloca la imagen del fondo en la pantalla '''
    screen.blit(background, (0, 0))


# Jugador
''' Ganon.png esta dentro de la carpeta del juego, es un png de 32x32 pixeles.
El calculo para 384 es: 800/2 - 32/2(pantalla/2 - imagen/2) para centrar la imagen en la pantalla en eje X 
Para 568 es: 600-32 (pantalla - imagen) para que la imagen este en la parte inferior de la pantalla'''

player = pygame.image.load("Ganon.png")
player_x = 384
player_y = 568
lifes = 3
life_box_x = 10
life_box_y = 25
walking_sound = mixer.Sound("caminar.mp3")
life_text = "Lifes"

def player_image(x, y):
    ''' Esta funcion coloca la imagen del jugador en la pantalla en la posicion especificada '''
    screen.blit(player, (x, y))


# Fuente

def font_bytes(font):
    ''' Esta funcion convierte la fuente en bytes para poder mostrarla en la pantalla.
     Se usó esta funcion como parte para poder convertir el codigo en un archivo .exe'''
    # Abre el archivo TTF en modo lectura binaria
    with io.open(font,'rb') as f: #rb significa read binary
        # Lee los bytes del archivo y los almacena en una variable
        ttf_bytes = f.read()
    # Crea un objeto BytesIO a partir de los bytes leidos del archivo TTF de la fuente
    return io.BytesIO(ttf_bytes)

font_as_bytes = font_bytes("freesansbold.ttf")
font = pygame.font.Font(font_as_bytes, 16) #Esta es la que usaremos para la caja de puntuacion y lifes.


# Puntuacion
points_box = pygame.image.load("Cajatexto_120x60.png")
points_box_x = 660 #posicion de la caja en x
points_box_y = 25 #posicion de la caja en y
points = 0
points_text = "Points"

def numeric_box(x, y, text, quantity, color):
    ''' Esta funcion coloca la imagen de la caja de puntuaicon en la posicion especificada  y sobre ella
    el texto de la puntuacion '''
    text_box = font.render(f"{text}:", True, color)
    quantity = font.render(f"{quantity}", True, color)
    screen.blit(points_box, (x, y))
    screen.blit(text_box, (x + 10, y + 10))
    screen.blit(quantity, (x + 55, y + 32))


# Musica
counter = 0 #Lo usaremos para acceder a la funcion de game_over_music durante el codigo cuando las vidas sean = 0
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(.5)  # Establecer volumen
pygame.mixer.music.play(-1)  # Reproducir en bucle

def background_music():
    ''' Esta funcion reproduce la musica del juego '''
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.set_volume(.4)  # Establecer volumen
    pygame.mixer.music.play(-1)  # Reproducir en bucle

def game_over_music():
    ''' Esta funcion reproduce la musica del Game Over '''
    pygame.mixer.music.load("game_over.mp3")
    pygame.mixer.music.set_volume(.5)  # Establecer volumen
    pygame.mixer.music.play(-1)  # Reproducir en bucle

# Proyectiles
fire_s = pygame.image.load("fire_S_16x20.png")
fire_s_sound = mixer.Sound("fire_s.mp3")

fire_s_x = player_x
fire_s_y = 568
fire_s_speed = 20 #Velocidad del proyectil en pixeles
shoot = False

def proyectil(proyectil, x, y):
    ''' Esta funcion coloca la imagen del proyectil en la pantalla en la posicion especificada '''
    global shoot
    shoot = True
    screen.blit(proyectil, (x+8, y))

# Enemigos
enemy_img_list = [] #Almacena las imagenes de los enemigos
enemy_x = [] #Almacena la posicion inicial en x de los enemigos
enemy_y = [] #Almacena la posicion inicial en y de los enemigos
enemy_speed_list = [] #Almacena la velocidad de los enemigos
enemy_number = 5

hey_sound = mixer.Sound("hey.mp3")
listen_sound = mixer.Sound("listen.mp3")
hello_sound = mixer.Sound("hello.mp3")
wachout_sound = mixer.Sound("wachout.mp3")
navi_in_sound = mixer.Sound("navi_in.mp3")
navi_sound_list = [hey_sound, listen_sound, hello_sound, wachout_sound, navi_in_sound]

def random_navi_sound():
    sound = random.choice(navi_sound_list)
    sound.set_volume(0.2)
    sound.play()

def create_enemigos():
    for i in range(enemy_number):
        enemy_img_list.append(pygame.image.load("navi.png"))
        enemy_y.append(0)
        enemy_speed_list.append(round(random.uniform(0.5, 1.5),1)) # velocidad de los enemigos
        enemy_x.append(random.randrange(160, 576, 32))  # rango de aparicion de los enemigos

def place_enemy(x, y, ene):
    ''' Esta funcion coloca la imagen del enemigo en la pantalla en la posicion especificada '''
    screen.blit(enemy_img_list[ene], (x, y))

def enemy_respawn(enemy_x, enemy_y, x_ini, x_fin, rango):
    ''' Esta funcion controla la reaparicion de los enemigos '''
    enemy_x = random.randrange(x_ini, x_fin, rango)
    enemy_y = 0
    return enemy_x, enemy_y


# Aumento de dificultad
puntuation_umbral = {
    50: 6,  #Puntuacion: Cantidad de enemigos
    100: 7,
    150: 8,
    200: 9,
    250: 10,
    300: 11,
    350: 12,
    500: 13,
    550: 14,
    600: 15
}

def add_enemy():
    ''' Esta funcion añadirá un enemigo extra cada tantos puntos    '''
    global enemy_number
    if points in puntuation_umbral:
        enemy_number = puntuation_umbral[points]


# Colisiones

def collision_detect(x1, y1, x2, y2):
    ''' Esta funcion comprueba si hay colision entre dos objetos obteniendo la distancia entre ellos '''
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    if distance < 32:
        return True
    else:
        return False

# Game Over
game_over_x = 250
game_over_y = 275
game_over_font = pygame.font.Font(font_as_bytes, 48)
game_over_text = "GAME OVER"


def game_over(x, y, text, color):
    ''' Esta funcion termina el juego cuando se acaban las lifes del jugador '''
    message = game_over_font.render(text, True, color)
    screen.blit(message, (x, y))


#Restart

restart_x = 200
restart_y = 325
restart_font = pygame.font.Font(font_as_bytes, 30)
restart_text = "Press R to restart or Q to quit"

def restart_quit(x, y, text, color):
    ''' Esta funcion coloca el texto de restart o quit en la pantalla '''
    message = restart_font.render(text, True, color)
    screen.blit(message, (x, y))

def restart_game():
    ''' Esta funcion resetea todos los parametros del juego '''
    global player_x, player_y, lifes, points, fire_s_y, shoot, enemy_img_list, enemy_x, enemy_y, enemy_speed_list,\
        counter, enemy_number
    counter = 0
    player_x = 384
    player_y = 568
    lifes = 3
    points = 0
    fire_s_y = 568
    shoot = False
    enemy_img_list.clear()
    enemy_number = 5
    enemy_x.clear()
    enemy_y.clear()
    enemy_speed_list.clear()
    background_music()


background_music() # Cargamos la musica del juego
#---------------------------- Bucle del juego ----------------------------

running = True
while running:

    # Cargamos el background del juego
    background_game()

    # Cargamos la imagen del jugador
    player_image(player_x, player_y)

    #Cargamos la caja de puntuacion
    numeric_box(points_box_x, points_box_y, points_text, points, WHITE)

    #Cargamos la caja de lifes
    numeric_box(life_box_x, life_box_y, life_text, lifes, WHITE)

    #En vez de una imagen podemos usar un color
    #screen.fill(GREEN)

    #Game Over y Restart
    if lifes <= 0:
        ''' Mostramos texto de Game Over '''
        game_over(game_over_x, game_over_y, game_over_text, RED)
        ''' Mostramos texto de Restart o Quit '''
        restart_quit(restart_x, restart_y, restart_text, BLACK)
        if counter < 1:
            pygame.mixer.music.stop()
            game_over_music()
            counter += 1


    #------------ Eventos del juego ------------

    for event in pygame.event.get():
        ''' pygame.event.get() nos permite obtener los eventos que se producen mientras se ejecuta el bucle '''
        if event.type == pygame.QUIT:   #Evento para cerrar la ventana
            running = False #Termina el bucle while

        if event.type == pygame.KEYDOWN: # pygame.KEYDOWN es un evento que se produce cuando se presiona una tecla.
            if event.key == pygame.K_r and lifes <= 0: #Si no hay vidas y se aprieta la tecla R se reinicia el juego
                restart_game()
            if event.key == pygame.K_q and lifes <= 0: #Si no hay vidas y se aprieta la tecla Q se cierra el juego
                running = False

        key = pygame.key.get_pressed() # pygame.key.get_pressed() nos permite obtener el estado de las teclas
        if key[pygame.K_a]:
            walking_sound.set_volume(1)
            walking_sound.play()
            player_x -= 16
        if key[pygame.K_d]:
            walking_sound.set_volume(1)
            walking_sound.play()
            player_x += 16
        #Disparo del jugador
        if key[pygame.K_SPACE]:
                if shoot == False:
                    fire_s_x = player_x
                    proyectil(fire_s, fire_s_x, fire_s_y)
                    fire_s_sound.play()

    # ------------ Limites del jugador ------------
    ''' Se comprueba que la posicion del jugador no sea menor o mayor que el tamaño de la pantalla (menos el tamaño
    de la imagen del jugador), de lo contrario, se queda en la posicion correspondiente. '''

    # Limites del jugador en eje X
    if player_x <= 176: #16 pixels mas que el limite por el despplazamiento de 16px del jugador
        player_x = 160   #Limite izquierdo
    if player_x >= 596: #16 pixels menos que el limite por el despplazamiento de 16px del jugador
        player_x = 612 #Limite derecho

    #---------- Proyectil -----------

    #Movimiento del proyectil
    if shoot == True:
        proyectil(fire_s, fire_s_x, fire_s_y) #Mantenemos la imagen del proyectil en la pantalla
        fire_s_y -= fire_s_speed #Mueve el proyectil hacia arriba

    # Limites del proyectil en eje Y
    if fire_s_y <= 0:
        shoot = False
        fire_s_y = 568

    #----------- enemigos -----------

    add_enemy() #revisa la puntuacion y decide cuantos enemigos hay
    create_enemigos() #Se crean los enemigos
    for e in range(enemy_number):

        # Se colocan los enemigos en la pantalla
        if lifes > 0:
            place_enemy(enemy_x[e], enemy_y[e], e)
        else:
            for ene in range(enemy_number):
                enemy_y[ene] = 700

        # Movimiento de cada enemigo
        enemy_y[e] += enemy_speed_list[e]

        #Colision del proyectil con el enemigo
        collision = collision_detect(fire_s_x, fire_s_y, enemy_x[e], enemy_y[e])
        if collision:
            random_navi_sound()
            shoot = False
            fire_s_y = 568
            points += 1
            enemy_x[e], enemy_y[e] = enemy_respawn(enemy_x[e], enemy_y[e], 160, 612, 32)


        # Limites del enemigo en eje Y
        if 600< enemy_y[e] <650:
            lifes -= 1
            enemy_x[e], enemy_y[e] = enemy_respawn(enemy_x[e], enemy_y[e], 160, 612, 32)

        #Colision del jugador con el enemigo
        collision = collision_detect(player_x, player_y, enemy_x[e], enemy_y[e])
        if collision:
            lifes -= 1
            enemy_x[e], enemy_y[e] = enemy_respawn(enemy_x[e], enemy_y[e], 160, 612, 32)


    # clock.tick() nos permite controlar la velocidad de actualización de la pantalla
    clock.tick(60)

    # Actualizar la pantalla
    pygame.display.flip()
