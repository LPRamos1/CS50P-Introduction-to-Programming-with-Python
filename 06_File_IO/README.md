# Module 06: File I/O

This module focuses on persistent data storage and manipulation. The exercises demonstrate how to read from and write to external files, handle CSV data structures, and perform basic image processing using Python.

## 🚀 Key Learning Points
* **File Handling:** Using `open()` with different modes (`r`, `w`) and ensuring proper closure via `with` blocks.
* **CSV Manipulation:** Utilizing the `csv` module to parse, filter, and restructure tabular data.
* **Command-Line Validation:** Ensuring the correct number of arguments and valid file extensions before processing.
* **External Libraries:** Introduction to the `Pillow` (PIL) library for image manipulation and the `tabulate` library for terminal formatting.
* **Error Management:** Handling `FileNotFoundError` to prevent program crashes during I/O operations.

## 📂 Included Programs

### 1. Lines of Code (`lines/lines.py`)
A program that counts the number of "lines of code" in a Python file, excluding comments and blank lines.
* **Technical Focus:** File reading, string stripping, and logic to ignore non-code lines.

### 2. Pizza Py (`pizza/pizza.py`)
A tool that reads a CSV file containing pizza menu data and outputs a formatted table.
* **Technical Focus:** Using the `tabulate` library to transform raw CSV data into a clean, human-readable ASCII table.

### 3. Scourgify (`scourgify/scourgify.py`)
A data cleaning script that reads a CSV file with "Name, House" (where name is "Last, First") and writes a new CSV with "first, last, house".
* **Technical Focus:** Simultaneous reading and writing of CSV files (`csv.DictReader` and `csv.DictWriter`) to restructure data.

### 4. CS50 P-Shirt (`shirt/shirt.py`)
An image processing script that overlays a virtual t-shirt onto a user-provided photo.
* **Technical Focus:** Using the `PIL` (Pillow) library for image resizing, cropping, and pasting (overlaying) with transparency.

---
*Part of my learning journey in Harvard's CS50P.*