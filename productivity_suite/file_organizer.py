import os
import shutil
from utils import header, section, stay_or_main, clear


class FileOrganizer:

    def menu(self):

        print("""
+--------------------------------------------------+
| 1 | Organize Files by Extension                  |
| 2 | Back to Main Menu                            |
+--------------------------------------------------+
""")

    def invalid_option(self):
        print("\n Invalid option selected!")
        print("Please choose a number between 1 and 2.")
        input("\nPress Enter to continue...")


    def organize_files(self, path):

        files_moved = 0
        extensions = set()

        for file in os.listdir(path):

            file_path = os.path.join(path, file)

            # Skip directories
            if os.path.isdir(file_path):
                continue

            # Skip files without extension
            if "." not in file:
                continue

            ext = file.split(".")[-1].lower()
            extensions.add(ext)

            folder = os.path.join(path, ext)

            if not os.path.exists(folder):
                os.mkdir(folder)

            try:
                shutil.move(file_path, os.path.join(folder, file))
                files_moved += 1
            except Exception:
                pass

        return files_moved, extensions


    def run(self):

        while True:

            clear()
            header("FILE ORGANIZER")
            section("OPTIONS")

            self.menu()

            choice = input("Select option (1-2): ").strip()

            if choice == "2":
                print("\nReturning to Main Menu...")
                input("Press Enter to continue...")
                break


            elif choice == "1":

                clear()
                header("FILE ORGANIZER")
                section("ENTER FOLDER PATH")

                path = input("Enter folder path to organize: ").strip()

                if not os.path.exists(path):

                    print("\n Folder not found!")
                    print("Please check the path and try again.")
                    input("\nPress Enter to continue...")
                    continue


                if not os.path.isdir(path):

                    print("\n The path you entered is not a folder.")
                    input("\nPress Enter to continue...")
                    continue


                section("ORGANIZING FILES")

                moved, extensions = self.organize_files(path)

                section("RESULT")

                if moved == 0:
                    print("No files needed organizing.")
                else:
                    print(f"✔ Files organized successfully!")
                    print(f"Total files moved : {moved}")

                if extensions:
                    print("\nCreated folders for extensions:")
                    for ext in sorted(extensions):
                        print(f"• .{ext}")

                print("\nFiles are grouped into folders based on file type.")

                input("\nPress Enter to continue...")


            else:
                self.invalid_option()

            if not stay_or_main():
                break
            