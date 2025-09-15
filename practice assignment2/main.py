"""
File I/O Program
Author: Lihua LU

Main module for user interaction with file operations.
Reference: 
Python Software Foundation. (2023). Reading and Writing Files.
Available: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
[Accessed: Sep 12, 2025].
"""

import file_operations


def display_menu():
    """Displays the program menu with author name"""
    print("\n" + "="*50)
    print("FILE I/O PROGRAM")
    print("Author: Lihua LU")
    print("="*50)
    print("1. Read from a file")
    print("2. Write to a new file")
    print("3. Overwrite an existing file")
    print("4. Exit")
    print("="*50)


def main():
    """Main function to run the program"""
    while True:
        display_menu()
        choice = input("Please enter your choice (1-4): ")

        if choice == '1':
            # Read file option
            filename = input(
                "Enter the filename to read (with .txt extension): ")
            result = file_operations.read_file(filename)
            print(f"\nFile content:\n{result}")

        elif choice == '2':
            # Write to new file option
            content = input("Enter the content to write: ")
            filename = input(
                "Enter the filename to write to (with .txt extension): ")
            result = file_operations.write_file(filename, content)
            print(f"\n{result}")

        elif choice == '3':
            # Overwrite file option
            content = input("Enter the content to write: ")
            filename = input(
                "Enter the filename to overwrite (with .txt extension): ")
            confirm = input(
                f"Are you sure you want to overwrite '{filename}'? (y/n): ")
            if confirm.lower() == 'y':
                result = file_operations.overwrite_file(filename, content)
                print(f"\n{result}")
            else:
                print("Operation cancelled.")

        elif choice == '4':
            # Exit program
            print("Thank you for using the File I/O Program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
