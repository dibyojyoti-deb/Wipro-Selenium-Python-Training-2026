def write_numbers_to_file(filename):
    try:
        with open(filename, "w") as file:
            for i in range(1, 101):
                file.write(str(i) + "\n")
        print("Numbers written successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"Unexpected error: {e}")


def read_file_safely(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File Content:\n")
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"Unexpected error: {e}")


filename = input("Enter the filename to write numbers to: ")

write_numbers_to_file(filename)

choice = input("Do you want to read the file content? (yes/no): ")

if choice.lower() == "yes":
    read_file_safely(filename)
