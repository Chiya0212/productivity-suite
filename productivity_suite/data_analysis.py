import json
from utils import header, section, stay_or_main, clear


class DataAnalysis:

    FILE = "data/notes.json"

    def load(self):
        try:
            with open(self.FILE, "r") as f:
                return json.load(f)
        except:
            return []

    def menu(self):

        print("""
+--------------------------------------------------+
| 1 | Notes Word Count                             |
| 2 | Show Longest Note                            |
| 3 | Back to Main Menu                            |
+--------------------------------------------------+
""")

    def invalid_option(self):
        print("\n Invalid option selected!")
        print("Please choose a number between 1 and 3.")
        input("\nPress Enter to continue...")

    def word_count(self):

        notes = self.load()

        section("WORD COUNT ANALYSIS")

        if not notes:
            print("No notes available for analysis.")
            return

        words = 0

        for n in notes:
            words += len(n.split())

        print(f"Total Notes : {len(notes)}")
        print(f"Total Words : {words}")

    def longest(self):

        notes = self.load()

        section("LONGEST NOTE")

        if not notes:
            print("No notes available.")
            return

        longest = max(notes, key=len)

        print("Longest note found:\n")
        print(longest)
        print(f"\nCharacters : {len(longest)}")

    def run(self):

        while True:

            clear()
            header("NOTES DATA ANALYSIS")
            section("OPTIONS")

            self.menu()

            ch = input("Select option (1-3): ").strip()

            if ch == "3":
                print("\nReturning to Main Menu...")
                input("Press Enter to continue...")
                break

            elif ch == "1":

                clear()
                header("NOTES DATA ANALYSIS")

                self.word_count()

                input("\nPress Enter to continue...")

            elif ch == "2":

                clear()
                header("NOTES DATA ANALYSIS")

                self.longest()

                input("\nPress Enter to continue...")

            else:
                self.invalid_option()

            if not stay_or_main():
                break
            