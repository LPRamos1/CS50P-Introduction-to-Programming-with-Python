# Module 07: Regular Expressions

This module explores the power of Regular Expressions (Regex) in Python. The exercises focus on using the `re` module to define complex search patterns for validating user input, extracting specific data from strings, and reformatting text efficiently.

## 🚀 Key Learning Points
* **Pattern Matching:** Utilizing symbols like `^`, `$`, `+`, `*`, and `?` to define precise string structures.
* **The `re` Module:** Mastering functions such as `re.search()`, `re.match()`, and `re.sub()`.
* **Grouping & Capturing:** Using parentheses `()` to isolate and extract specific parts of a string (e.g., YouTube IDs or time components).
* **Validation:** Implementing robust checks for IP addresses, email formats, and time strings.
* **Text Extraction:** Parsing HTML and complex strings to retrieve specific substrings using regex groups.

## 📂 Included Programs & Tests

### 1. NUMB3RS
* **Files:** (`numb3rs/numb3rs.py` & `numb3rs/test_numb3rs.py`)
* **Technical Focus:** Validating IPv4 addresses. The regex ensures exactly four numbers separated by dots, with each number ranging from 0 to 255.

### 2. Watch on YouTube (`watch/watch.py`)
* **Technical Focus:** Extracting YouTube video IDs from HTML `<iframe>` tags.
* **Logic:** Uses regex to identify various YouTube URL formats (http, https, www, youtu.be) and converts them into a shortened `youtu.be` link.

### 3. Working 9 to 5
* **Files:** (`working/working.py` & `working/test_working.py`)
* **Technical Focus:** Converting 12-hour time formats (AM/PM) to 24-hour formats. Uses regex groups to capture hours, minutes, and indicators, handling optional minute inputs.

### 4. Regular, um, Expressions
* **Files:** (`um/um.py` & `um/test_um.py`)
* **Technical Focus:** Counting occurrences of "um" as a standalone word using word boundaries (`\b`), ensuring it doesn't match substrings in words like "yummy".

### 5. Response Validation (`response/response.py`)
* **Technical Focus:** Using the `validator-collection` or `validators` library to verify if an input is a syntactically valid email address.

## 🛠️ How to Run Tests
To verify the regex logic:
```bash
pytest .
```