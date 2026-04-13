# 🐍 CS50P: Introduction to Programming with Python (Harvard University)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![CS50P](https://img.shields.io/badge/CS50P-Harvard-white?style=for-the-badge&logo=harvard&logoColor=red)
![Testing](https://img.shields.io/badge/Tested%20with-Pytest-0A9EDC?style=for-the-badge&logo=pytest)

Welcome to my portfolio for **CS50P**, Harvard University's introduction to Python programming. This repository presents a beginner-to-intermediate progression with tested projects—documenting my journey from learning core syntax to tackling practical programming tasks, building tested scripts, and working with APIs.

---

## 📂 Repository Structure

The curriculum is organized into modules, each focusing on a core computer science concept applied through Python:

| Module | Core Topics | Key Learning |
| :--- | :--- | :--- |
| [**00 - Functions & Variables**](./00_Functions_Variables) | Arguments, return values, and primitive types. | Code modularization. |
| [**01 - Conditionals**](./01_Conditionals) | Logic gates, if/else statements, control flow. | Decision-making logic. |
| [**02 - Loops**](./02_Loops) | Iteration, lists, and dictionary manipulation. | Efficient data traversal. |
| [**03 - Exceptions**](./03_Exceptions) | Try/Except blocks, input validation. | Defensive programming. |
| [**04 - Libraries**](./04_Libraries) | Third-party APIs and built-in modules. | Extending functionality. |
| [**05 - Unit Tests**](./05_Unit_Tests) | Writing robust tests with **Pytest**. | Test-Driven Development (TDD). |
| [**06 - File IO**](./06_File_IO) | Persistence: CSV and file manipulation. | Data management. |
| [**07 - Regular Expressions**](./07_Regular_Expressions) | Advanced pattern matching (Regex). | String data extraction. |
| [**08 - OOP**](./08_Object_Oriented_Programming) | Classes, Encapsulation, and Properties. | System design fundamentals. |
| [**09 - Final Project**](./09_Project) | **Capstone:** End-to-end project synthesis. | Putting all skills together. |

---

## 🏆 Featured Project: IP Analyzer (Capstone)

### [Explore the Project Here](./09_Project)

A command-line capstone project that extracts, validates, and geolocates IPv4 addresses from `.json`, `.csv`, `.log`, and `.txt` files.

### Overview
The project is designed as an end-to-end CLI workflow: input validation, IP extraction, API integration, and terminal reporting.

### Key Features
* **Hybrid extraction pipeline:** Regex finds potential IPv4s, then Python logic validates octets (`0-255`).
* **JSON-safe approach:** Nested JSON data is flattened to text before extraction.
* **Batch API requests:** Up to 50 IPs per request using `requests`, with delay control between batches.
* **Readable output:** Results are displayed in a formatted table using `tabulate`.


## 🛠️ Setup, Run, and Tests

### 1. Setup
```bash
git clone https://github.com/LPRamos1/CS50P-Introduction-to-Programming-with-Python.git
cd CS50P-Introduction-to-Programming-with-Python
python -m venv venv
```

Activate the virtual environment:
```bash
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

Install dependencies:
```bash
pip install -r 09_Project/requirements.txt
```

### 2. Run
```bash
python 09_Project/project.py 09_Project/logs/acess.log
```

### 3. Tests
```bash
pytest 09_Project/
```

### Design Decisions
* Keep extraction logic modular (`ip_info`, `_extract_from_regex`, `_extract_from_json`) for readability and easier testing.
* Use `pytest` with monkeypatching and mocking to isolate filesystem and API behavior.
* Favor clarity and reliability over unnecessary complexity, consistent with a CS50P-level capstone.


## 🛠️ Tech Stack & Skills

* **Language:** Python 3.12+
* **Testing:** Pytest (Unit testing, Mocking, Test Coverage)
* **Architecture:** Object-Oriented Programming (OOP), Functional Programming
* **Dev Tools:** Git/GitHub, Visual Studio Code
* **Core Libraries:** `requests` (API), `pathlib` (File System), `re` (Regex), `json`, `tabulate`.

---

## 📜 Academic Integrity & License

> [!IMPORTANT]
> **Academic Honesty:** This repository is intended for portfolio demonstration and educational documentation only. In accordance with Harvard University's CS50 Academic Honesty policy, these solutions should **not** be used to complete assignments. 
> 
> All problem set specifications and base codes are property of Harvard University's CS50P course.

---

## 🎓 About the Certification

**CS50P** goes beyond syntax, emphasizing how to read documentation, debug, and adopt Pythonic best practices (PEP 8). This repository demonstrates my ability to write clean, maintainable, and documented code as part of a structured, beginner-to-intermediate curriculum.

---


## 📬 Contact Me

- 📫 **Email:** [lucaspaolo.dev@gmail.com](mailto:lucaspaolo.dev@gmail.com)
- 🔗 **LinkedIn:** [lucas-paolo-ramos](https://www.linkedin.com/in/lucas-paolo-ramos-16a693402/en)
