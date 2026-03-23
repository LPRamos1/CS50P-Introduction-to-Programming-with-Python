# Module 04: Libraries

This module focuses on extending Python's capabilities by using built-in modules and third-party libraries. The exercises cover command-line arguments, API interactions, and external package management.

## 🚀 Key Learning Points
* **External Modules:** Importing and using libraries like `requests`, `pyfiglet`, and `emoji`.
* **Command-Line Arguments:** Handling user input via `sys.argv` for more dynamic scripts.
* **API Integration:** Fetching real-time data from external services (JSON parsing).
* **Randomization & Math:** Using the `random` module to create interactive logic and games.
* **Input Validation:** Ensuring program stability when dealing with unpredictable user inputs or network responses.

## 📂 Included Programs

### 1. Adieu, Adieu (`adieu/adieu.py`)
A program that takes a list of names and formats them into a "Farewell" string according to English grammar rules (using commas and "and").
* **Technical Focus:** Using the `inflect` library to handle pluralization and list formatting.

### 2. Bitcoin Price Index (`bitcoin/bitcoin.py`)
A real-time price tracker that converts a specific amount of Bitcoin into USD.
* **Technical Focus:** Utilizing the `requests` library to query the CoinDesk API and handling JSON data structures.

### 3. Emojize (`emojize/emojize.py`)
A simple script that converts emoji aliases (like `:thumbs_up:`) into actual Unicode emojis.
* **Technical Focus:** Working with the `emoji` library to enhance text output.

### 4. Frank, Ian and Glen’s Letters (`figlet/figlet.py`)
A tool that transforms plain text into large, stylized ASCII art banners.
* **Technical Focus:** Using `pyfiglet` and managing command-line arguments to select specific fonts.

### 5. Guessing Game (`game/game.py`)
An interactive game where the user tries to guess a randomly generated number within a specified range.
* **Technical Focus:** Implementing the `random` module and robust `while` loops for input validation.

### 6. Little Professor (`professor/professor.py`)
A mathematical educational tool that generates addition problems based on chosen difficulty levels.
* **Technical Focus:** Logic structuring, random number generation within specific digit constraints, and score tracking.

---
*Part of my learning journey in Harvard's CS50P.*