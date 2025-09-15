"""
File Operations Module
Author: Lihua LU

This module handles file reading and writing operations.
Reference: 
Python Software Foundation. (2023). Reading and Writing Files.
Available: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
[Accessed: Sep 12, 2025].
"""

import os


def read_file(filename):
    """
    Reads content from a text file

    Args:
        filename (str): Name of the file to read

    Returns:
        str: Content of the file or error message
    """
    try:
        # Ensure filename ends with .txt
        if not filename.endswith('.txt'):
            filename += '.txt'

        # Check if file exists
        if not os.path.exists(filename):
            return f"Error: File '{filename}' does not exist."

        # Read file content
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading file: {str(e)}"


def write_file(filename, content):
    """
    Writes content to a text file

    Args:
        filename (str): Name of the file to write to
        content (str): Content to write to the file

    Returns:
        str: Success or error message
    """
    try:
        # Ensure filename ends with .txt
        if not filename.endswith('.txt'):
            filename += '.txt'

        # Check if file already exists
        if os.path.exists(filename):
            return f"Warning: File '{filename}' already exists. Please choose a different name or use 'overwrite' option."

        # Write content to file
        with open(filename, 'w') as file:
            file.write(content)
        return f"Successfully wrote to '{filename}'."
    except Exception as e:
        return f"Error writing file: {str(e)}"


def overwrite_file(filename, content):
    """
    Overwrites content to a text file (existing or new)

    Args:
        filename (str): Name of the file to write to
        content (str): Content to write to the file

    Returns:
        str: Success or error message
    """
    try:
        # Ensure filename ends with .txt
        if not filename.endswith('.txt'):
            filename += '.txt'

        # Write content to file (overwrite if exists)
        with open(filename, 'w') as file:
            file.write(content)
        return f"Successfully wrote to '{filename}'."
    except Exception as e:
        return f"Error writing file: {str(e)}"
