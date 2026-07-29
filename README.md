# Python File & Exception Handling

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

**Overview**
This repository features a comprehensive Python script demonstrating core competencies in **File Input/Output (I/O) Operations** and **Advanced Exception Handling**. It serves as a practical implementation of backend data persistence and robust error mitigation strategies.

**Features**
* **Robust File I/O:** Programmatic creation, reading, and appending of text files (`student.txt`) utilizing context managers (`with` statements) for optimal resource management.
* **Multi-method Data Extraction:** Implementation of `.read()`, `.readline()`, and `.readlines()` to parse data structures.
* **Comprehensive Error Catching:** Implementation of `try-except-else-finally` blocks to ensure application stability.
* **Active Input Validation:** Graceful handling of `ZeroDivisionError` and `ValueError` to prevent runtime crashes during user interaction.
* **Mini-Project Implementation:** A Student Result Processing application that evaluates numerical grades, enforces boundary constraints (0-100), and outputs formatted letter grades seamlessly.

## 📋 Prerequisites
To run this project, you will need:
* **Python 3.x** installed on your system.

****How to Run****
1. **Clone the repository:**
   ```bash
   git clone https://github.com/maryam-hamid-sa/Python-File-Handling-Exception-Handling.git
   ```
2. **Navigate to the directory:**
   ```bash
   cd Python-File-Handling-Exception-Handling
   ```
3. **Execute the script:**
   ```bash
   python assignment.py
   ```
   *Note: Upon execution, the script will interactively prompt for inputs and automatically generate/update the `student.txt` file in the same directory.*

**Code Structure**
* `assignment.py` - The main executable script containing all modular implementations for file operations and error handling.
* `student.txt` - Dynamically generated text file validating the I/O write and append operations.

**Key Learnings**
This project highlights clean coding practices, emphasizing the importance of anticipating user input errors and managing external resources (files) securely without memory leaks.
