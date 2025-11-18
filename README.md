# ¿Que tanto sabes? Game

CRUDAZSO Games is a command-line mini‑platform that manages users,
authentication, and a trivia-style game.\
The project is structured in modular Python files, making it easy to
extend, maintain, and scale.

## 🚀 Features

-   **User Registration & Login** (with JSON persistence)
-   **Admin CRUD** for managing users
-   **Trivia Game Engine**
-   **Utility Helpers** for input validation and formatting
-   **Clean Modular Architecture**

## 📁 Project Structure

    crudzaso_games/
    │── administrador_crud.py   # Admin CRUD operations for users
    │── auth.py                 # Authentication logic (login/register)
    │── data.py                 # JSON data handlers
    │── game.py                 # Game logic
    │── main.py                 # Entry point of the app
    │── preguntas.json          # Trivia questions
    │── usuarios.json           # Stored user accounts
    │── utils.py                # Utilities and helpers

## 🧠 How It Works

### 1. **Authentication Layer (`auth.py`)**

Handles: - Creating users - Logging in - Validating credentials -
Checking roles (user/admin)

### 2. **Data Management (`data.py`)**

Manages read/write operations to: - `usuarios.json` - `preguntas.json`

Ensures persistent storage without databases.

### 3. **CRUD Admin Module (`administrador_crud.py`)**

Admins can: - List users - Edit users - Delete users - View user stats

### 4. **Game Engine (`game.py`)**

Manages: - Random question selection - Score tracking - Game flow

### 5. **Main Controller (`main.py`)**

Acts as the app's router: - Loads menu - Calls authentication - Opens
game - Opens admin panel based on user role

## 📦 Requirements

-   Python 3.9+
-   No external packages required (pure Python)

## ▶️ Run the App

``` bash
python main.py
```

The main menu will guide you through login, registration, and gameplay.

## 🛠️ Extending the Project

-   Add more game categories\
-   Implement difficulty levels\
-   Add more CRUD fields\
-   Migrate JSON storage to SQLite or PostgreSQL\
-   Build a GUI or web version

## ❤️ About This Project

A lightweight modular trivia platform designed for learning, practicing
Python, and experimenting with CRUD + game dynamics.

------------------------------------------------------------------------

```mermaid
flowchart TD

    A[Inicio del Programa] --> B[Menú Principal]

    B --> C[Iniciar sesión]
    B --> D[Registrar Usuario]
    D --> E[Validar Registro]
    E --> B

    C --> F{¿Usuario es Admin?}

    F -->|SI| G[Menú Administrador]
    F -->|NO| H[Menú Jugador]

    %% ADMIN
    G --> I[Administrar preguntas]
    I --> J[CRUD Preguntas<br/>(Crear, Listar, Actualizar, Eliminar)]
    G --> S[Salir]

    %% JUGADOR
    H --> K[Seleccionar Tema]
    K --> L[Seleccionar Modo]
    L --> M[Seleccionar Dificultad]
    M --> N[Configurar Puntos]
    N --> O[Jugar Preguntas]
    O --> P[Mostrar Resultados]

    P --> Q{¿Desea volver a jugar?}
    Q -->|SI| K
    Q -->|NO| R[Fin del Programa]

    %% Cambio usuario
    H --> T{¿Desea continuar con el mismo usuario?}
    T -->|SI| H
    T -->|NO| B

    %% Flujo de jugar directo desde admin
    G --> U[Jugar]
    U --> H
´´´
