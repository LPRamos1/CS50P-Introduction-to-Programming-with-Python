# Module 03: Exceptions

This module focuses on writing robust Python code by handling runtime errors and unexpected user input. These exercises demonstrate the use of `try`, `except`, `else`, and `pass` blocks to create resilient applications.

## 🚀 Key Learning Points
* **Error Handling:** Implementing `try`/`except` blocks to catch specific errors like `ValueError`, `ZeroDivisionError`, and `KeyError`.
* **Input Validation:** Creating loops that persist until the user provides valid, parseable data.
* **Data Parsing & Formatting:** Handling various input formats (dates, fractions) and converting them into standardized outputs.
* **Program Termination:** Gracefully handling `EOFError` (Ctrl-D) to end user input sessions.

## 📂 Included Programs

### 1. Fuel Gauge (`fuel/fuel.py`)
A program that calculates fuel percentage from a fraction (X/Y).
* **Technical Focus:** Catching `ValueError` and `ZeroDivisionError` to ensure the denominator is valid and the input is numeric.

### 2. Felipe’s Taqueria (`taqueria/taqueria.py`)
A point-of-sale system that enables users to place orders from a menu.
* **Technical Focus:** Handling `KeyError` when an item isn't on the menu and using `EOFError` to finish the order.

### 3. Grocery List (`grocery/grocery.py`)
A tool that organizes a grocery list alphabetically and counts item frequency.
* **Technical Focus:** Using dictionaries to store counts and handling input termination via `EOFError`.

### 4. Outdated (`outdated/outdated.py`)
A script that converts middle-endian dates (e.g., September 8, 1636) to ISO 8601 format (YYYY-MM-DD).
* **Technical Focus:** Advanced exception handling during string parsing to manage multiple date formats.

---
*Part of my learning journey in Harvard's CS50P.*
