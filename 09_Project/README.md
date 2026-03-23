# IP Analyzer
#### Video Demo: <[Link](https://www.youtube.com/watch?v=MsgaPhHCTs4)>

## 📌 Overview
The **IP Analyzer** is a command-line capstone project for CS50P. It extracts, validates, and geolocates IPv4 addresses from multiple file formats, turning raw logs into readable technical reports.

## 🛠️ Core Functions
- `validate_input()`: Ensures the CLI arguments are correct and the file format is supported.
- `_extract_from_regex()`: The heavy-lifter that finds IPs and validates octets (0-255).
- `get_ip_details()`: Manages the Batch API POST requests and rate-limiting pauses.
- `report()`: Transforms the API dictionary into a clean, tabulated terminal grid.

## 🚀 Key Features
- **Multi-format Support:** Seamlessly processes `.txt`, `.log`, `.csv`, and `.json` files.
- **Hybrid Validation:** Leverages both Regular Expressions (Regex) for initial pattern matching and custom Python logic to guarantee every octet is within the valid 0-255 range—ensuring only real IPv4 addresses are reported.
- **Type Hinting:** Employs Python’s native type hints, improving code maintainability, clarity, and modern development practices.
- **Batch Processing:** Efficiently performs IP geolocation via batch requests to the IP-API service, analyzing up to 50 IPs per request for optimal performance and compliance with API policies.
- **Terminal Visualization:** Creates clean, professional-grade terminal reports using the `tabulate` library, with automatic text wrapping to maintain readability even for long organization names.

## ⚡ Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/LPRamos1/CS50P-Introduction-to-Programming-with-Python.git
cd CS50P-Introduction-to-Programming-with-Python/09_Project
pip install -r requirements.txt
```

## ▶️ Run

```bash
python project.py logs/acess.log
```

## ✅ Tests

```bash
pytest .
```

## 📂 File Structure
- **project.py:** The main engine. Contains the orchestrator function (`ip_info`), extraction logic, and API communication layer.
- **test_project.py:** A comprehensive test suite utilizing `pytest`, with advanced techniques like **monkeypatching** and **mocking** to simulate file systems and API responses.
- **requirements.txt:** Lists the external dependencies (`requests`, `tabulate`) necessary for the project.

## 🛠️ Design Decisions
Handling JSON files was one of the main challenges. Given the unpredictability of log data structures, a "Flatten and Extract" strategy is used: JSON content is parsed, serialized back to a string, and the validated Regex is applied, ensuring any embedded IP address—regardless of its nesting—can be found.

A critical design decision was the use of **Rate Limiting** to stay within the IP-API’s free tier of 45 requests per minute. The analyzer organizes requests into batches of up to 50 IPs and introduces a mandatory `time.sleep` pause between requests. This prevents overloading the API and possible temporary IP bans during large-scale processing.

The choice of libraries was intentional: `requests` delivers robust error handling for all API operations, and `tabulate` presents results in a readable Fancy Grid format, ensuring professionalism and clarity in all types of technical reports.

### Why this project?
As an Electronic Engineering student transitioning to AI and Data Science, I wanted to tackle a practical data processing problem. This project has enabled deeper learning in software architecture, API integration, and unit testing—skills vital for any modern developer.
