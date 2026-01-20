import re

def main():
    print("=== Regular Expression Demo ===")

    # 1. re.match() for Employee ID
    emp_id = input("\nEnter Employee ID (format EMP123): ")

    emp_pattern = r"(EMP)(\d{3})"
    match = re.match(emp_pattern, emp_id)

    if match:
        print("Valid Employee ID found")
        print("Full Match:", match.group(0))
        print("Group 1 (Prefix):", match.group(1))
        print("Group 2 (Digits):", match.group(2))
    else:
        print("Invalid Employee ID")

    # 2. re.search() for Email ID
    text = input("\nEnter a text containing an email address: ")

    email_pattern = r"([\w.+-]+)@([\w-]+)\.(\w+)"
    search = re.search(email_pattern, text)

    if search:
        print("\nValid Email Found")
        print("Full Email:", search.group(0))
        print("Username:", search.group(1))
        print("Domain Name:", search.group(2))
        print("Domain Extension:", search.group(3))
    else:
        print("No valid email found")

    # 3. Meta-characters and special sequences demo
    print("\n=== Meta-characters & Special Sequences Demo ===")
    sample = input("Enter a sample string: ")

    # .  *  +  ?  \d  \w  \s demonstration
    pattern = r"(\w+)\s+(\d+).*?"
    result = re.search(pattern, sample)

    if result:
        print("Pattern matched")
        print("Word (\\w+):", result.group(1))
        print("Number (\\d+):", result.group(2))
    else:
        print("Pattern not matched")


if __name__ == "__main__":
    main()
