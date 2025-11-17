from data import temas

RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"


def crud_preguntas():
    crud_activo = True
    while crud_activo:
        print("\n" + "="*40)
        print("        ADMIN - CRUD PREGUNTAS")
        print("="*40)
        print("1. Listar preguntas")
        print("2. Crear pregunta")
        print("3. Editar pregunta")
        print("4. Eliminar pregunta")
        print("0. Volver")
        opcion = input(f"\n{GREEN}Elige una opción: {RESET}").strip()

        if opcion == "1":
            listar_preguntas()
        elif opcion == "2":
            crear_pregunta()
        elif opcion == "3":
            editar_pregunta()
        elif opcion == "4":
            eliminar_pregunta()
        elif opcion == "0":
            crud_activo = False
        else:
            print(f"{RED}Opción inválida.{RESET}")

def seleccionar_tema():
    print(f"\n{YELLOW}--- Seleccionar tema ---{RESET}")
    nombres_temas = list(temas.keys())
    for i, nombre in enumerate(nombres_temas, start=1):
        print(f"{i}. {nombre}")
    opcion = input("Tema: ").strip()

    if not opcion.isdigit():
        print(f"{RED}Entrada inválida.{RESET}")
        return None, None, None

    idx = int(opcion) - 1
    if idx < 0 or idx >= len(nombres_temas):
        print(f"{RED}Opción fuera de rango.{RESET}")
        return None, None, None

    tema_seleccionado = nombres_temas[idx]
    return tema_seleccionado, temas[tema_seleccionado], idx

def seleccionar_lista_preguntas():
    tema_nombre, niveles_tema, _ = seleccionar_tema()
    if not tema_nombre:
        return None, None, None

    print(f"\n{YELLOW}--- Elegir dificultad ---{RESET}")
    for i, (nombre_nivel, _) in enumerate(niveles_tema, start=1):
        print(f"{i}. {nombre_nivel}")

    opcion = input("Dificultad: ").strip()
    if not opcion.isdigit():
        print(f"{RED}Entrada inválida.{RESET}")
        return None, None, None

    idx = int(opcion) - 1
    if idx < 0 or idx >= len(niveles_tema):
        print(f"{RED}Opción fuera de rango.{RESET}")
        return None, None, None

    nombre_nivel, lista_preguntas = niveles_tema[idx]
    return tema_nombre, nombre_nivel, lista_preguntas

def listar_preguntas():
    tema, nivel, lista = seleccionar_lista_preguntas()
    if not lista:
        return

    print(f"\n{YELLOW}Preguntas de {tema} - {nivel}{RESET}")
    if len(lista) == 0:
        print("No hay preguntas.")
        return

    for idx, pregunta in enumerate(lista):
        correcta = pregunta["correcta"]
        print(f"{idx}) {pregunta['texto']} "
              f"(Correcta: {pregunta['opciones'][correcta]})")

def crear_pregunta():
    tema, nivel, lista = seleccionar_lista_preguntas()
    if not lista:
        return

    print(f"\nCreando pregunta en {tema} - {nivel}")
    texto = input(f"{YELLOW}Texto de la pregunta: {RESET}").strip()
    if not texto:
        print("La pregunta no puede estar vacía.")
        return

    opciones = []
    for i in range(4):
        op = input(f"Opción {i+1}: ").strip()
        if not op:
            print("La opción no puede estar vacía.")
            return
        opciones.append(op)

    correcta_str = input("Índice de la correcta (1-4): ").strip()
    if not correcta_str.isdigit():
        print("Índice inválido.")
        return
    correcta = int(correcta_str) - 1
    if correcta not in [0, 1, 2, 3]:
        print("Índice fuera de rango.")
        return

    lista.append({"texto": texto, "opciones": opciones, "correcta": correcta})
    print(f"{GREEN}Pregunta creada en {tema} - {nivel}.{RESET}")


def editar_pregunta():
    tema, nivel, lista = seleccionar_lista_preguntas()
    if not lista or len(lista) == 0:
        print("No hay preguntas para editar.")
        return

    listar_preguntas()
    idx_str = input("Índice de la pregunta a editar: ").strip()
    if not idx_str.isdigit():
        print("Índice inválido.")
        return
    idx = int(idx_str)
    if idx < 0 or idx >= len(lista):
        print("Índice fuera de rango.")
        return

    pregunta = lista[idx]
    print(f"\nEditando pregunta {idx} de {tema} - {nivel}")

    nuevo_texto = input(
        f"Nuevo texto (Enter para mantener '{pregunta['texto']}'): "
    ).strip()
    if nuevo_texto:
        pregunta["texto"] = nuevo_texto

    for i, op in enumerate(pregunta["opciones"]):
        nueva_op = input(
            f"Nueva opción {i+1} (Enter para mantener '{op}'): "
        ).strip()
        if nueva_op:
            pregunta["opciones"][i] = nueva_op

    nueva_correcta = input(
        f"Nuevo índice correcta (1-4, Enter para mantener {pregunta['correcta']+1}): "
    ).strip()
    if nueva_correcta:
        if nueva_correcta.isdigit():
            ind = int(nueva_correcta) - 1
            if ind in [0, 1, 2, 3]:
                pregunta["correcta"] = ind
            else:
                print("Índice fuera de rango, se mantiene anterior.")
        else:
            print("Entrada inválida, se mantiene anterior.")

    print(f"{GREEN}Pregunta editada.{RESET}")

def eliminar_pregunta():
    tema, nivel, lista = seleccionar_lista_preguntas()
    if not lista or len(lista) == 0:
        print("No hay preguntas para eliminar.")
        return

    listar_preguntas()
    idx_str = input("Índice de la pregunta a eliminar: ").strip()
    if not idx_str.isdigit():
        print("Índice inválido.")
        return
    idx = int(idx_str)
    if idx < 0 or idx >= len(lista):
        print("Índice fuera de rango.")
        return

    confirm = input("¿Seguro que quieres eliminar? (s/n): ").strip().lower()
    if confirm == "s":
        lista.pop(idx)
        print(f"{GREEN}Pregunta eliminada de {tema} - {nivel}.{RESET}")
    else:
        print("Operación cancelada.")
