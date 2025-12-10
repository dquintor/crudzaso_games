# WHAT DO YOU KNOW SO MUCH?

What do you know so much?, is a command-line mini‑platform that manages users,
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

## 6. Libraries used
- pwinput

## 7. Test Scenarios

1. Login with user already in database (JSON file), the data is entered and as a result there is a successful login.
2. User registration in database (JSON file), and login with that same user and as a result login.
3. Entry as administrator with correct data stored, result is enabled in admin menu (CRUD)

------------------------------------------------------------------------

Enjoy hacking on **WHAT DO KNOW SO MUCH? Games**! 🎮🔥
