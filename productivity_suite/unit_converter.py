from utils import header, section, stay_or_main, clear


class UnitConverter:

    def menu(self):

        print("""
+--------------------------------------------------+
| 1 | Kilometers → Miles                           |
| 2 | Miles → Kilometers                           |
| 3 | Celsius → Fahrenheit                         |
| 4 | Fahrenheit → Celsius                         |
| 5 | Back to Main Menu                            |
+--------------------------------------------------+
""")


    def invalid_option(self):
        print("\n Invalid option selected!")
        print("Please choose a number between 1 and 5.")
        input("\n Press Enter to continue...")


    def run(self):

        while True:

            clear()

            header("UNIT CONVERTER")

            section("CONVERSION OPTIONS")

            self.menu()

            ch = input("Select option (1-5): ").strip()

            if ch == "5":
                print("\nReturning to Main Menu...")
                input("Press Enter to continue...")
                break


            elif ch in ["1", "2", "3", "4"]:

                try:

                    clear()
                    header("UNIT CONVERTER")

                    section("ENTER VALUE")

                    if ch == "1":
                        km = float(input("Enter Kilometers: "))
                        result = km * 0.621371

                        section("RESULT")
                        print(f"{km} KM = {round(result,3)} Miles")


                    elif ch == "2":
                        miles = float(input("Enter Miles: "))
                        result = miles * 1.60934

                        section("RESULT")
                        print(f"{miles} Miles = {round(result,3)} KM")


                    elif ch == "3":
                        c = float(input("Enter Celsius: "))
                        result = (c * 9/5) + 32

                        section("RESULT")
                        print(f"{c} °C = {round(result,2)} °F")


                    elif ch == "4":
                        f = float(input("Enter Fahrenheit: "))
                        result = (f - 32) * 5/9

                        section("RESULT")
                        print(f"{f} °F = {round(result,2)} °C")


                    print("\n Conversion completed successfully!")

                except ValueError:
                    print("\n Invalid input! Please enter numeric values only.")

                input("\n Press Enter to continue...")


            else:
                self.invalid_option()


            if not stay_or_main():
                break
            