import curses
import random
import data 

RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"


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


def juego_curses(stdscr):
    inicializar_colores()
    curses.curs_set(0)
    niveles = [
        ("Easy", data.preguntas_faciles_ingles.copy()),
        ("Intermediate", data.preguntas_intermedias_ingles.copy()),
        ("Hard", data.preguntas_dificiles_ingles.copy())
    ]
    puntuacion = 0
    for nombre_nivel, lista in niveles:
        random.shuffle(lista)
        for indice, preg in enumerate(lista):
            texto, opciones_mezcladas, indice_correcta = seleccionar_pregunta(preg)
            stdscr.clear()
            stdscr.addstr(0, 0, f"{nombre_nivel} - Question {indice+1}", curses.color_pair(4))
            stdscr.refresh()
            seleccion = seleccionar_opcion(stdscr, texto, opciones_mezcladas)
            if seleccion == indice_correcta:
                puntuacion += 1
            mostrar_feedback(stdscr, texto, opciones_mezcladas, seleccion, indice_correcta)

    return {"puntuacion": puntuacion}

def jugar():
    curses.wrapper(juego_curses)