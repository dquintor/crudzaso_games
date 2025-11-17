import curses
import random
from data import temas
from utils import validar_entero_menu
import time
import winsound
import sys


RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"


def seleccionar_tema():
    menu = ("\n---Seleccione un tema para comenzar a jugar---\n"
            "1. Cultura\n2. Ingles\n3. Historia\n4. Python\n5. Musica y Arte\n")
    opcion = validar_entero_menu(menu, "Elija una opcion de juego (1-5):", 1,5)
    
    match opcion:
        case 1:
            return "Cultura"
        case 2: 
            return "Ingles"
        case 3:
            return "Historia"
        case 4:
            return "Python"
        case 5: 
            return "Musica"
        
def seleccionar_modo():
    menu = ("\n---Selecciona modo de juego---\n"
            "1. Normal (Sin limite de tiempo)\n2. Modo contrareloj(10 segundos por pregunta)\n")
    opcion = validar_entero_menu(menu, "Elija un modo de juego(1-2:)",1,2)
    match opcion:
        case 1:
            return False, 0
        case 2:
            return True, 10

def inicializar_colores():
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(4, curses.COLOR_CYAN, -1)
    curses.init_pair(5, curses.COLOR_MAGENTA, -1)
    curses.init_pair(6, curses.COLOR_YELLOW, -1)
    curses.init_pair(7, curses.COLOR_GREEN, -1)
    curses.init_pair(8, curses.COLOR_RED, -1)
    curses.init_pair(7, curses.COLOR_GREEN, curses.COLOR_BLACK)  
    curses.init_pair(8, curses.COLOR_YELLOW, curses.COLOR_BLACK)  
    curses.init_pair(9, curses.COLOR_RED, curses.COLOR_BLACK) 
    
def obtener_limite_por_nivel(nombre_nivel):
    nombre = nombre_nivel.lower()

    if "fácil" in nombre or "facil" in nombre:
        return 10   
    elif "intermedio" in nombre or "medio" in nombre:
        return 20
    elif "difícil" in nombre or "dificil" in nombre:
        return 30
    else:
        return 15
    
    
def seleccionar_pregunta(pregunta):
    texto = pregunta["texto"]
    opciones = pregunta["opciones"].copy()
    correcta = opciones[pregunta["correcta"]]
    random.shuffle(opciones)
    indice_correcta = opciones.index(correcta)
    return texto, opciones, indice_correcta


def seleccionar_opcion(stdscr, texto, opciones):
    curses.curs_set(0)
    posicion_seleccion= 0
    
    continuar = True

    while continuar:
        stdscr.clear()
        stdscr.addstr(0, 0, texto, curses.color_pair(4))

        for i, opcion in enumerate(opciones):
            if i == posicion_seleccion:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(i + 2, 0, f"> {opcion}")
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(i + 2, 0, f"  {opcion}")

        tecla_presionada = stdscr.getch()

        if tecla_presionada== curses.KEY_UP and posicion_seleccion> 0:
           posicion_seleccion-= 1
           
        elif tecla_presionada == curses.KEY_DOWN and posicion_seleccion< len(opciones) - 1:
            posicion_seleccion += 1
            
        elif tecla_presionada == curses.KEY_ENTER or tecla_presionada in [10, 13]:
            continuar = False
            
    return posicion_seleccion

def seleccion_opcion_temporizado(stdscr,texto, opciones, limite_segundos):
    curses.curs_set(0)
    stdscr.nodelay(True)
    
    posicion_seleccion = 0 
    continuar = True 
    seleccion = None 
    tiempo_agotado = False
    stdscr.clear()
    stdscr.addstr(0,0, texto, curses.color_pair(4))
        
    
    inicio = time.time()
    
    while continuar: 
        transcurrido = time.time() - inicio 
        restante = int(limite_segundos - transcurrido)
        if restante < 0:
            restante = 0 
            
        if transcurrido >= limite_segundos:
            tiempo_agotado = True
            continuar = False
            
        for i, opcion in enumerate(opciones):
            
            if i == posicion_seleccion:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(i + 2, 0, f"> {opcion}")
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(i + 2, 0, f"  {opcion}")
                
        timer = len(opciones) + 4 
        ancho_timer = 20
        
        if limite_segundos > 0:
            fraccion = restante / limite_segundos
        else:
            fraccion = 0

        if fraccion < 0:
            fraccion = 0
        if fraccion > 1:
            fraccion = 1

        rellenos = int(ancho_timer* fraccion)
        vacios = ancho_timer  - rellenos

        barra = "▉" * rellenos + "-" * vacios 

        if fraccion > 0.66:
            color_barra = curses.color_pair(7)  
        elif fraccion > 0.33:
            color_barra = curses.color_pair(8)  
        else:
            color_barra = curses.color_pair(9)  

        stdscr.attron(color_barra)
        stdscr.addstr(timer, 0, barra)
        stdscr.attroff(color_barra)

        stdscr.addstr(timer + 1, 0, f"Tiempo restante: {int(restante)} s", curses.color_pair(4))

        stdscr.refresh()
        
        if not tiempo_agotado:
            tecla_presionada = stdscr.getch()

            if tecla_presionada == curses.KEY_UP and posicion_seleccion > 0:
                posicion_seleccion -= 1

            elif tecla_presionada == curses.KEY_DOWN and posicion_seleccion < len(opciones) - 1:
                posicion_seleccion += 1

            elif tecla_presionada == curses.KEY_ENTER or tecla_presionada in [10, 13]:
                seleccion = posicion_seleccion
                continuar = False
                
        time.sleep(0.1)
    stdscr.nodelay(False)
    
    return seleccion, tiempo_agotado


def mostrar_feedback(stdscr, texto, opciones, seleccion, indice_correcto,
                     tiempo_agotado=False, limite_segundos=0):
    stdscr.clear()
    stdscr.addstr(0, 0, texto, curses.color_pair(4))

    for i, op in enumerate(opciones):

        if i == indice_correcto:  
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(i + 2, 0, f"  {op}")
            stdscr.attroff(curses.color_pair(2))

        elif i == seleccion:  
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(i + 2, 0, f"  {op}")
            stdscr.attroff(curses.color_pair(3))

        else:  
            stdscr.addstr(i + 2, 0, f"  {op}")

    linea_mensaje = len(opciones) + 4

    if tiempo_agotado:
        mensaje = f"Respuesta no registrada. ¡Se agotó el tiempo!"
    else:
        mensaje = "Presione cualquier tecla para continuar"

    stdscr.addstr(linea_mensaje, 0, mensaje, curses.color_pair(4))
    stdscr.refresh()
    stdscr.getch()

    


def animacion_ruleta():
    elementos = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪"]
    print(f"\n{CYAN}Escogiendo pregunta al azar...{RESET}\n")
    print( " " * 30 )
    pasos_totales = 40
    sleep = 0.02
    sleep_increment = 0.004
    def reescribir_linea(contenido):
        sys.stdout.write("\x1b[1F")  
        sys.stdout.write("\r\x1b[2K" + contenido + "\n")
        sys.stdout.flush()
    for i in range(pasos_totales):
        elementos = elementos[1:] + elementos[:1]   
        tira = " ".join(elementos)

        reescribir_linea(f" {tira} ")
        winsound.Beep(300, 30)

        time.sleep(sleep)
        sleep += sleep_increment  
    winsound.Beep(600, 250)



    print(f"\n{GREEN}Pregunta seleccionada{RESET}\n")
    time.sleep(0.4)


def juego_curses(stdscr, niveles, contrareloj , limite_segundos):
    inicializar_colores()
    curses.curs_set(0)
    puntuacion = 0
    
    for nombre_nivel, lista in niveles:
        lista = lista.copy()
        random.shuffle(lista)
        
        for indice, preg in enumerate(lista):
            curses.endwin()
            animacion_ruleta()
            stdscr = curses.initscr()
            inicializar_colores()
            curses.curs_set(0)

            texto, opciones_mezcladas, indice_correcta = seleccionar_pregunta(preg)
            stdscr.clear()
            stdscr.addstr(0, 0, f"{nombre_nivel} - Pregunta {indice+1}", curses.color_pair(4))
            stdscr.refresh()

            if contrareloj:
                seleccion, tiempo_agotado = seleccion_opcion_temporizado(
                    stdscr,
                    texto,
                    opciones_mezcladas,
                    limite_segundos
                )
            else:
                seleccion = seleccionar_opcion(stdscr, texto, opciones_mezcladas)
                tiempo_agotado = False

            
            if (not tiempo_agotado) and (seleccion == indice_correcta):
                puntuacion += 1

            mostrar_feedback(
                stdscr,
                texto,
                opciones_mezcladas,
                seleccion,
                indice_correcta,
                tiempo_agotado,
                limite_segundos
            )

    return {"puntuacion": puntuacion}


def jugar():
    tema= seleccionar_tema()
    niveles = temas[tema]
    contra_reloj, limite_segundos = seleccionar_modo()
    
    curses.wrapper(juego_curses,niveles, contra_reloj, limite_segundos)
    