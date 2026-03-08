from utils import header, section, stay_or_main, clear
import json

class NotesManager:

    FILE = "data/notes.json"

    def load(self):
        try:
            with open(self.FILE, "r") as f:
                return json.load(f)
        except:
            return []


    def save(self, data):
        with open(self.FILE, "w") as f:
            json.dump(data, f, indent=4)


    def menu(self):
        print("""
+--------------------------------------------------+
| 1 | Add Note                                     |
| 2 | View Notes                                   |
| 3 | Delete Note                                  |
| 4 | Back to Main Menu                            |
+--------------------------------------------------+
""")


    def invalid_option(self):
        print("\n Invalid option selected!")
        print("Please choose a number between 1 and 4.\n")
        input("Press Enter to continue...")


    def run(self):

        while True:

            clear()

            header("NOTES MANAGER")

            section("MENU")

            self.menu()

            ch = input("Select option (1-4): ").strip()

            notes = self.load()

            if ch == "4":
                print("\nReturning to Main Menu...")
                input("Press Enter to continue...")
                break


            elif ch == "1":

                clear()
                header("ADD NOTE")

                note = input("Write your note: ").strip()

                if note == "":
                    print("\n Note cannot be empty.")
                else:
                    notes.append(note)
                    self.save(notes)
                    print("\n✔ Note saved successfully!")

                input("\nPress Enter to continue...")


            elif ch == "2":

                clear()
                header("VIEW NOTES")

                section("YOUR NOTES")

                if not notes:
                    print("No notes available.")
                else:
                    for i, n in enumerate(notes, 1):
                        print(f"{i}. {n}")

                input("\nPress Enter to continue...")


            elif ch == "3":

                clear()
                header("DELETE NOTE")

                if not notes:
                    print("\nNo notes available to delete.")
                    input("\nPress Enter to continue...")
                    continue

                section("SELECT NOTE")

                for i, n in enumerate(notes, 1):
                    print(f"{i}. {n}")

                try:
                    idx = int(input("\nEnter note number to delete: ")) - 1

                    if idx < 0 or idx >= len(notes):
                        print("\n Invalid note number.")
                    else:
                        deleted = notes.pop(idx)
                        self.save(notes)
                        print(f"\n✔ Note deleted: {deleted}")

                except ValueError:
                    print("\n Please enter a valid number.")

                input("\nPress Enter to continue...")


            else:
                self.invalid_option()

            if not stay_or_main():
                break