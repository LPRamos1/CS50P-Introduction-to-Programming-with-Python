# Module 08: Object-Oriented Programming (OOP)

This module introduces the principles of Object-Oriented Programming in Python. The exercises focus on defining classes, managing internal states through properties, and implementing special "dunder" methods to create custom behaviors for objects.

## 🚀 Key Learning Points
* **Classes & Objects:** Creating blueprints for data and behavior.
* **Encapsulation:** Using getters and setters (@property) to protect and validate internal data.
* **Dunder Methods:** Implementing special methods like `__init__`, `__str__`, and `__add__` to customize object functionality.
* **Error Handling in OOP:** Raising `ValueError` within methods to prevent invalid object states.
* **Operator Overloading:** Defining how objects interact with standard Python operators.
* **PDF Generation:** Utilizing external libraries (fpdf2) to generate visual documents from code.

## 📂 Included Programs & Tests

### 1. Seasons of Love
* **Files:** `seasons.py` / `test_seasons.py`
* **Technical Focus:** Working with the `datetime` module to calculate the difference between dates.
* **Logic:** Converts a lifespan into minutes and outputs the result in words using the `inflect` library.

### 2. Cookie Jar
* **Files:** `jar.py` / `test_jar.py`
* **Technical Focus:** Building a class from scratch with capacity constraints.
* **Logic:** Implements methods to `deposit` and `withdraw` cookies, while using `@property` to manage the jar's current size and maximum capacity.

### 3. CS50 Shirtificate
* **Files:** `shirtificate.py`
* **Technical Focus:** Programmatic PDF creation using the `fpdf2` library.
* **Logic:** Generates a custom PDF certificate with a centered image and personalized text overlay.

## 🛠️ How to Run Tests
To verify the class logic and date calculations:
```bash
pytest .