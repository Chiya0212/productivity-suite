import time
from utils import header, section, stay_or_main, clear

class Timer:

    def menu(self):

        print("""
+--------------------------------------------------+
| 1 | Countdown Timer                              |
| 2 | Stopwatch                                    |
| 3 | Back to Main Menu                            |
+--------------------------------------------------+
""")


    def invalid_option(self):
        print("\n Invalid option!")
        print("Please select a number between 1 and 3.\n")
        input("Press Enter to continue...")


    def run(self):

        while True:

            clear()

            header("TIMER")

            section("TIMER OPTIONS")

            self.menu()

            ch = input("Select option (1-3): ").strip()

            if ch == "3":
                print("\nReturning to Main Menu...")
                input("Press Enter to continue...")
                break


            elif ch == "1":

                clear()
                header("COUNTDOWN TIMER")

                section("SET TIMER")

                try:

                    sec = int(input("Enter time in seconds: "))

                    if sec <= 0:
                        print("\n Please enter a positive number.")
                        input("Press Enter to continue...")
                        continue

                    print("\n Countdown started...\n")

                    while sec > 0:
                        print(f"\rRemaining Time : {sec} seconds ", end="")
                        time.sleep(1)
                        sec -= 1

                    print("\n\n✔ Time finished!")

                except ValueError:
                    print("\n Invalid input! Please enter a number.")

                input("\nPress Enter to continue...")


            elif ch == "2":

                clear()
                header("STOPWATCH")

                section("STOPWATCH MODE")

                print("Press ENTER to start the stopwatch")
                input()

                print("\n Stopwatch started...")
                start = time.time()

                print("Press ENTER again to stop")
                input()

                end = time.time()

                elapsed = round(end - start, 2)

                section("RESULT")

                print(f"Elapsed Time : {elapsed} seconds")
                print("\n Stopwatch stopped successfully!")

                input("\nPress Enter to continue...")


            else:
                self.invalid_option()

            if not stay_or_main():
                break
