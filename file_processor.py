import os

def process_file_and_handle_errors():
    """
    Prompts the user for a filename, reads its content,
    converts the text to uppercase, and writes it to a new file.
    Includes robust error handling for common file-related issues.
    """
    source_filename = input("Enter the name of the file to read: ")
    destination_filename = "output_" + os.path.basename(source_filename)

    try:
        # File Read & Write Challenge
        # Use 'with' statement for automatic file management
        with open(source_filename, 'r') as infile:
            content = infile.read()
            modified_content = content.upper()

        with open(destination_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"\nSuccess! The content of '{source_filename}' has been converted to uppercase and written to '{destination_filename}'.")

    except FileNotFoundError:
        # Handles the case where the user-provided file does not exist
        print(f"\nError: The file '{source_filename}' was not found.")
    except IOError as e:
        # Handles other I/O errors, such as permission issues
        print(f"\nAn I/O error occurred: {e}")
    except Exception as e:
        # A general catch-all for any other unexpected errors
        print(f"\nAn unexpected error occurred: {e}")

# Run the file processing program
if __name__ == "__main__":
    process_file_and_handle_errors()