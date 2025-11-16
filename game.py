import curses
import random
from data import temas
from utils import validar_entero_menu
import time


RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"


def seleccionar_tema():
    menu = ("\n---Seleccione un tema para comenzar a jugar---\n"
            "1. Cultura\n2. Ingles\n")
    opcion = validar_entero_menu(menu, "Elija una opcion de juego (1-2):", 1,2)
    
    match opcion:
        case 1:
            return "Cultura"
        case 2: 
            return "Ingles"
    

def inicializar_colores():
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(4, curses.COLOR_CYAN, -1)
    
    
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

def mostrar_feedback(stdscr, texto, opciones, seleccion, indice_correcto):
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

    
    stdscr.addstr(len(opciones) + 4, 0, "Presione cualquier tecla para continuar", curses.color_pair(4))
    stdscr.refresh()

    stdscr.getch()
    
    
import time  # asegúrate de tener este import arriba del archivo UNA sola vez

import time
import sys

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

        time.sleep(sleep)
        sleep += sleep_increment  

    print(f"\n{GREEN}Pregunta seleccionada{RESET}\n")
    time.sleep(0.4)


def juego_curses(stdscr, niveles):
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
            seleccion = seleccionar_opcion(stdscr, texto, opciones_mezcladas)
            if seleccion == indice_correcta:
                puntuacion += 1
            mostrar_feedback(stdscr, texto, opciones_mezcladas, seleccion, indice_correcta)

    return {"puntuacion": puntuacion}

def jugar():
    tema= seleccionar_tema()
    niveles = temas[tema]
    curses.wrapper(juego_curses,niveles)
    