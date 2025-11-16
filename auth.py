from utils import leer_contraseña_ocultandola

usuarios = {}

def registro_usuario():
    nombre = input("Ingrese su nombre de usuario: ").strip()
    if not nombre:
        print("El usuario no puede estar vacío. Ingrese un nombre de usuario. \n")
        return
    if not all(c.isalpha() or c.isdigit() or c.isspace() for c in nombre):
        print("El nombre solo puede contener letras, números y espacios.\n")
        return
    if nombre in usuarios:
        print("Nombre de usuario ya existe. Elija otro nombre de usuario o Inicie sesion.\n")
        return

    contraseña = leer_contraseña_ocultandola("Ingrese una contraseña: ").strip()
    if not contraseña:
        print("La contraseña no puede estar vacía.\n")
        return

    usuarios[nombre] = contraseña
    print("Usuario registrado con éxito.\n")


def inicio_sesion():
    nombre = input("Ingrese su nombre de usuario: ").strip()
    if not nombre:
        print("El usuario no puede estar vacío. Ingrese un nombre de usuario. \n")
        return False
    if nombre not in usuarios:
        print("Usuario no encontrado.\n")
        return False

    contraseña = leer_contraseña_ocultandola("Ingrese su contraseña: ").strip()
    if usuarios[nombre] == contraseña:
        print("Inicio de sesión exitoso.\n")
        return True

    print("Contraseña incorrecta. Vuelva a intentarlo.\n")
    return False

