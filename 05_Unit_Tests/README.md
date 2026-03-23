# Module 05: Unit Tests

This module introduces the concept of automated software testing. The focus is on writing independent test functions to verify the correctness of existing code, ensuring that refactoring or adding new features doesn't break current functionality.

## 🚀 Key Learning Points
* **Pytest Framework:** Utilizing `pytest` to run automated test suites.
* **Assertions:** Using `assert` statements to validate expected outputs against actual results.
* **Edge Case Testing:** Identifying and testing boundary conditions (e.g., empty strings, zero values, special characters).
* **Exception Testing:** Verifying that functions correctly raise exceptions like `ValueError` or `ZeroDivisionError` when expected.
* **Modular Code:** Structuring programs to be "testable" by separating input/output from core logic.

## 📂 Included Programs & Tests

### 1. Back to the Bank
* **Files:** `bank.py` / `test_bank.py`
* **Technical Focus:** Testing string matching logic for greetings. Ensures that variations in capitalization and spacing return the correct monetary values ($0, $20, or $100).

### 2. Re-requesting a Feast
* **Files:** `twttr.py` / `test_twttr.py`
* **Technical Focus:** Verifying vowel-removal logic. Tests include strings with all uppercase, all lowercase, numbers, and punctuation to ensure only vowels are stripped.

### 3. Refueling
* **Files:** `fuel.py` / `test_fuel.py`
* **Technical Focus:** Testing numerical conversions and error handling. Uses `pytest.raises` to ensure that non-numeric inputs or zero denominators trigger the appropriate exceptions.

### 4. Re-reading the Vanity Plates
* **Files:** `plates.py` / `test_plates.py`
* **Technical Focus:** Validation of complex business rules. Tests the placement of numbers, minimum/maximum lengths, and prohibited punctuation in license plate strings.

## 🛠️ How to Run Tests
To run all tests in this directory, ensure you have `pytest` installed and execute:
```bash
pytest .

---
