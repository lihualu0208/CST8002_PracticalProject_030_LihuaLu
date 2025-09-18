# main.py
"""
CST8002 - Practical Project Part 02
Professor: Stanley Pieda
Due Date: 2025-10-19
Author: Lihua Lu

This is the main program that initializes and runs the seabird records management system.
"""

from presentation.menu_system import MenuSystem

def main():
    """
    Main function that orchestrates the program execution.
    """
    try:
        menu_system = MenuSystem()
        menu_system.run()
    except Exception as e:
        print(f"Program terminated due to error: {e}")
    finally:
        print("Program ended.")

if __name__ == "__main__":
    main()