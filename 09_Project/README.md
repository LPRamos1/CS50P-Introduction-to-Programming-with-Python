# IP Analyzer
#### Video Demo: <Link>
#### Description:

## 📌 Description
The **IP Analyzer** is a command-line tool designed to simplify the process of extracting, validating, and geolocating IPv4 addresses from various file formats. Developed as a final project for Harvard's CS50P, this tool bridges the gap between raw log data and actionable geographical insights.

## 🚀 Key Features
- **Multi-format Support:** Seamlessly processes `.txt`, `.log`, `.csv`, and `.json` files.
- **Hybrid Extraction:** Combines Regular Expressions (Regex) with mathematical validation to ensure every extracted IP is a valid IPv4 address (0-255 range).
- **Batch Processing:** Implements Batch Requests to the IP-API service, allowing the analysis of up to 50 IPs per request.
- **Terminal Visualization:** Generates clean, professional reports using the `tabulate` library with automatic text wrapping for long organization names.

## 📂 File Structure
- **project.py:** The main engine. It contains the orchestrator function (`ip_info`), the extraction logic, and the API communication layer.
- **test_project.py:** A comprehensive test suite utilizing `pytest`. It uses testing techniques like **monkeypatching** and **mocking** to simulate file systems and API responses without relying on an internet connection.
- **requirements.txt:** Lists the external dependencies (`requests`, `tabulate`) necessary for the project.

## 🛠️ Design Choices
One of the most challenging parts of this project was handling JSON files. Initially, I debated whether to map specific keys in the JSON structure. However, I realized that log files often have unpredictable structures. To solve this, I implemented a "Flatten and Extract" strategy: the tool parses the JSON, dumps it back into a string, and applies the validated Regex. This ensures that no matter where an IP is hidden in a JSON, it will be found.

Another critical decision was the implementation of **Rate Limiting**. To respect the IP-API's free tier limits (45 requests per minute), I built a batching system with a mandatory `time.sleep` pause between chunks of 50 IPs. This makes the tool robust and "polite" to the server, preventing IP bans during large-scale analysis.

### Why this project?
As an Electronic Engineering student moving towards AI and Data Science, I wanted to build something that reflects real-world data processing challenges. This project allowed me to practice software architecture, API integration, and unit testing—skills that are essential for any modern developer.