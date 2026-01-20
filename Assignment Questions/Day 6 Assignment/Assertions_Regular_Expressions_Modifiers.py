import re


def validate_password(password):
    """
    Validates a strong password using regex lookahead assertions.
    """

    pattern = (
        r"^(?=.*[A-Z])"      # at least one uppercase letter
        r"(?=.*[a-z])"       # at least one lowercase letter
        r"(?=.*\d)"          # at least one digit
        r"(?=.*[@$!%*?&])"   # at least one special character
        r".{8,}$"            # minimum length 8
    )

    match = re.match(
        pattern,
        password,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL
    )

    if match:
        print("Password is STRONG")
    else:
        print("Password is NOT STRONG")


def main():
    print("=== Strong Password Validator ===")
    print("Password Rules:")
    print("1. Minimum 8 characters")
    print("2. At least one uppercase letter (A-Z)")
    print("3. At least one lowercase letter (a-z)")
    print("4. At least one digit (0-9)")
    print("5. At least one special character (@, $, !, %, *, ?, &)")

    password = input("\nEnter password: ")
    validate_password(password)


if __name__ == "__main__":
    main()
