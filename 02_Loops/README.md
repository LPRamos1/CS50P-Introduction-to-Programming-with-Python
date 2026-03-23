# Module 02: Loops

This module explores the implementation of iterative logic in Python using `for` and `while` loops. The exercises focus on string transformations, complex validation rules, and efficient data retrieval through collections.

## 🚀 Key Learning Points
* **Iterative Logic:** Using loops to process data character-by-character or through collections.
* **String Transformation:** Implementing algorithms to convert naming conventions (e.g., camelCase to snake_case).
* **Data Mapping:** Utilizing Python Dictionaries (`dict`) for fast, key-based data lookup.
* **Complex Validation:** Applying multiple logical constraints within a loop to validate user input.

## 📂 Included Programs

### 1. camelCase (`camel/camel.py`)
A program that converts variables from `camelCase` to `snake_case`.
* **Logic:** Iterates through each character to identify uppercase letters and appends an underscore before converting them to lowercase.
* **Technical Focus:** Character-by-character string iteration and case detection logic.

### 2. Vanity Plates (`plates/plates.py`)
A validation tool that checks if a requested license plate meets specific legal requirements (length, numeric placement, and character types).
* **Logic:** Implements a series of conditional checks to ensure the plate starts with letters and handles numbers correctly.
* **Technical Focus:** String slicing, membership testing, and boolean logic within validation functions.

### 3. Nutrition Facts (`nutrition/nutrition.py`)
A script that outputs the calorie count for various fruits based on an official FDA chart.
* **Logic:** Maps fruit names to their respective calorie values using a dictionary.
* **Technical Focus:** Dictionary lookup and case-insensitive key handling.

---
*Part of my learning journey in Harvard's CS50P.*