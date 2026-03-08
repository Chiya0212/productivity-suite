import os
import datetime
import shutil


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def header(title="PERSONAL PRODUCTIVITY SUITE"):
    clear()
    print("="*60)
    print(title.center(60))
    print("="*60)


def section(title):
    print("\n" + "-"*60)
    print(title.center(60))
    print("-"*60)


def pause():
    input("\nPress ENTER to continue...")


def stay_or_main():

    while True:

        print("\n1 Stay on this page")
        print("2 Go to Main Menu")

        choice = input("Select option: ")

        if choice == "1":
            clear()
            return True

        elif choice == "2":
            clear()
            return False

        else:
            print("Invalid choice. Please select 1 or 2.")


def backup_notes():

    source = "data/notes.json"
    folder = "data/backups"

    if not os.path.exists(folder):
        os.makedirs(folder)

    time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    dest = f"{folder}/notes_{time}.json"

    shutil.copy(source, dest)

    print("\nBackup created:", dest)
    