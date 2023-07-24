

def main():
    full_name = get_full_name()
    print()
    
    password = get_password()
    print()
    
    first_name = get_first_name(full_name)

    email = get_email()
    print()

    phone_number = get_phone_number()

    print(f"Hi {first_name}, thanks for creating an account.")
    print(f"We'll text your confirmation code to this number: "
          f"{phone_number[:3]}.{phone_number[3:6]}.{phone_number[6:]}")


def get_email():
    while True:
        at = False
        domain = False
        email = input("Enter email address:   ").strip()
        if "@" in email and email.endswith(".com"):
            return email
        else:
            print("Invalid email, try again.")


def get_phone_number():
    while True:
        phone_number = input("Enter phone number:    ").strip()
        phone_number = phone_number.replace(".", "")
        phone_number = phone_number.replace("-", "")
        phone_number = phone_number.replace("(", "")
        phone_number = phone_number.replace(")", "")
        phone_number = phone_number.replace(" ", "")

        digit = True
        if len(phone_number) == 10 and phone_number.isdigit():
            return phone_number
        else:
            print("Invalid number, try again.")


def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")
    

def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name
    

def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit is False or cap_letter is False or len(password) < 8:
            print(f"Password must be 8 characters or more \n"
                  f"with at least one digit and one uppercase letter.")
        else:
            return password


if __name__ == "__main__":
    main()
