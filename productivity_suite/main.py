from calculator import Calculator
from notes_manager import NotesManager
from timer import Timer
from file_organizer import FileOrganizer
from unit_converter import UnitConverter
from data_analysis import DataAnalysis
from utils import clear, header, pause, backup_notes


def show_menu():
    print("\n" + "="*60)
    print("                PERSONAL PRODUCTIVITY SUITE")
    print("="*60)

    print("""
+-------------------------------------------------------------+
|  1  | Calculator                                            |
|  2  | Notes Manager                                         |
|  3  | Timer & Stopwatch                                     |
|  4  | File Organizer                                        |
|  5  | Unit Converter                                        |
|  6  | Notes Data Analysis                                   |
|  7  | Backup Notes                                          |
|  8  | Exit Application                                      |
+-------------------------------------------------------------+
""")


def invalid_option():
    print("\n" + "!"*50)
    print("  Invalid option selected!")
    print("  Please enter a number between 1 and 8.")
    print("!"*50)


def main():

    calc = Calculator()
    notes = NotesManager()
    timer = Timer()
    organizer = FileOrganizer()
    converter = UnitConverter()
    analysis = DataAnalysis()

    while True:

        clear()
        header("WELCOME TO PRODUCTIVITY SUITE")

        show_menu()

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            print("\nOpening Calculator...")
            calc.run()

        elif choice == "2":
            print("\nOpening Notes Manager...")
            notes.run()

        elif choice == "3":
            print("\nOpening Timer...")
            timer.run()

        elif choice == "4":
            print("\nOpening File Organizer...")
            organizer.run()

        elif choice == "5":
            print("\nOpening Unit Converter...")
            converter.run()

        elif choice == "6":
            print("\nOpening Notes Data Analysis...")
            analysis.run()

        elif choice == "7":
            print("\nCreating Backup...")
            backup_notes()

        elif choice == "8":
            print("\nThank you for using the Personal Productivity Suite!")
            print("Goodbye!")
            break

        else:
            invalid_option()

        pause()


if __name__ == "__main__":
    main()