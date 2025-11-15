# crudzaso_games
Bienvenid@ a PinguiMundo, un trivia game hecho en Python que se juega directo en la terminal. Todo con interfaz interactiva usando curses, mezcla de preguntas aleatorias y varios niveles de dificultad
# ¿Qué es PinguiMundo?
Un juego de preguntas con selección interactiva, colores, feedback visual y diferentes niveles.
Además, ya incluye un sistema de usuarios para registrarse, iniciar sesión y trackear quién juega.
# Categorías de preguntas
- Inglés
- Python
- Cultura e historia
- Música y arte
El objetivo del equipo es que PinguiMundo se convierta en un banco de preguntas completo, fácil de extender y divertido de jugar
# Estructura del proyecto
```bash
crudzaso_games/
│
├── auth.py            # Registro e inicio de sesión
├── game.py            # Lógica del juego y UI con curses
├── utils.py           # Validaciones 
├── data.py            # Categorías y preguntas
├── main.py            # Punto de entrada al programa
└── README.md          # Este archivo
```
# Cómo jugar
Ejecuta el juego: python main.py

En el menú inicial: Regístrate o inicia sesión.

Elige una categoría (cuando todas estén implementadas).

Muévete con las flechas ↑ ↓

Selecciona con Enter

Obtén feedback visual inmediato (correcto/incorrecto).
