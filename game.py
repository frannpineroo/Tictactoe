from random import randrange

def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    print("*-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3, sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|", sep="")
    print("*-------" * 3, sep="")

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    ok = False # suposicion falsa, la utilizamos para entrar al bucle
    while not ok:
        move = input("Ingresa tu movimiento (1-9): ")
        ok = len(move) == 1 and move >= '1' and move <= '9' #verifica que el movimiento sea un numero del 1 al 9
        if not ok:
            print("Movimiento no valido. Intenta de nuevo.")
            continue
        move = int(move) - 1 # convertimos el movimiento a un numero del 0 al 8
        row = move // 3 # obtenemos la fila del movimiento
        col = move % 3 # obtenemos la columna del movimiento
        sign = board[row][col] # obtenemos el valor del cuadro donde se quiere hacer el movimiento
        ok = sign not in ['O', 'X']
        if not ok:
            print("Cuadro ocupado. Intenta de nuevo.")
            continue
    board[row][col] = 'O'  # actualizamos el tablero con el movimiento del usuario

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    free = []  # lista de cuadros libres
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:  # si el cuadro no esta ocupado
                free.append((row, col))  # agregamos el cuadro a la lista de cuadros libres
    return free  # devolvemos la lista de cuadros libres

def victory_for(board, sgn):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    if sgn == 'X':
        who = 'Máquina'
    elif sgn == 'O':
        who = 'Jugador'
    else:
        who = None
    cross1 = cross2 = True #para la diagonal
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn: 
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board[rc][rc] != sgn:
            cross1 = False
        if board[2 - rc][rc] != sgn:
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    free = make_list_of_free_fields(board)  # obtenemos la lista de cuadros libres
    cnt = len(free)  # contamos los cuadros libres
    if cnt > 0:
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'

board = [ [ 3 * j + i + 1 for i in range(3)] for j in range(3)]  # inicializamos el tablero
board[1][1] = 'X'  # la máquina comienza en el centro
free = make_list_of_free_fields(board)  # obtenemos la lista de cuadros libres
human_turn = True  # el jugador comienza
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)  # el jugador ingresa su movimiento
        victory = victory_for(board, 'O')  # verificamos si el jugador ha ganado
    else:
        draw_move(board)  # la máquina dibuja su movimiento
        victory = victory_for(board, 'X')
    if victory != None:  # si hay un ganador
        break
    human_turn = not human_turn  # cambiamos el turno
    free = make_list_of_free_fields(board)  # actualizamos la lista de cuadros libres

display_board(board)  # mostramos el tablero final
if victory == 'Máquina':
    print("¡La máquina ha ganado!")
elif victory == 'Jugador':
    print("¡Felicitaciones! has ganado el juego.")
else:
    print("¡El juego ha terminado en empate!")