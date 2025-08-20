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
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    ```
    *(Replace `your-username` and `your-repo-name` with your actual GitHub username and repository name.)*

2.  **Create a Sample File**:
    Before running the program, create a simple text file (e.g., `sample.txt`) in the same directory as `file_processor.py`. Add some text to it.

    **Example `sample.txt` content:**
    ```
    Hello, this is a test file.
    Python is great!
    ```

3.  **Run the Script**:
    ```bash
    python file_processor.py
    ```

4.  **Enter the File Name**:
    When prompted, enter the name of your sample file (e.g., `sample.txt`). The program will then create a new file named `output_sample.txt` with the content in uppercase.
