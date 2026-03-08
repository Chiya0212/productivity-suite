from utils import header, section, stay_or_main, clear


class Calculator:

    def menu(self):

        print("""
+--------------------------------------------------+
| 1 | Addition                                     |
| 2 | Subtraction                                  |
| 3 | Multiplication                               |
| 4 | Division                                     |
| 5 | Power (a^b)                                  |
| 6 | Back to Main Menu                            |
+--------------------------------------------------+
""")


    def run(self):

        while True:

            clear()

            header("CALCULATOR")

            section("CALCULATOR OPERATIONS")

            self.menu()

            choice = input("Select operation (1-6): ").strip()

            if choice == "6":
                print("\nReturning to Main Menu...")
                input("Press Enter to continue...")
                break

            if choice not in ["1", "2", "3", "4", "5"]:
                print("\n Invalid option! Please choose between 1 and 6.")
                input("Press Enter to try again...")
                continue

            try:

                section("ENTER NUMBERS")

                a = float(input("Enter first number  : "))
                b = float(input("Enter second number : "))

                if choice == "1":
                    result = a + b
                    operation = "Addition"

                elif choice == "2":
                    result = a - b
                    operation = "Subtraction"

                elif choice == "3":
                    result = a * b
                    operation = "Multiplication"

                elif choice == "4":

                    if b == 0:
                        print("\n Error: Division by zero is not allowed.")
                        input("Press Enter to continue...")
                        continue

                    result = a / b
                    operation = "Division"

                elif choice == "5":
                    result = a ** b
                    operation = "Power"

                section("RESULT")

                print(f"Operation : {operation}")
                print(f"Result    : {result}")

                print("\n✔ Calculation completed successfully!")

                if not stay_or_main():
                    break

            except ValueError:
                print("\n Invalid input! Please enter numeric values only.")
                input("Press Enter to continue...")