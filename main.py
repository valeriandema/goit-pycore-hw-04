from assignments.assignment1 import total_salary
from assignments.assignment2 import get_cats_info
from assignments.assignment3 import display_folder_structure
from assignments.assignment4 import (
    parse_input,
    add_contact,
    change_contact,
    show_phone,
    show_all,
)

def main():
    test_total_salary()
    test_get_cats_info()
    display_folder_structure('picture')
    test_bot_helper()
    

def test_total_salary():
    total, average = total_salary('assets/salaries.txt')
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

def test_get_cats_info():
    cats_info = get_cats_info('assets/cats.txt')
    print(f"{cats_info}")

def test_bot_helper():
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")
    
if __name__ == '__main__':
    main()