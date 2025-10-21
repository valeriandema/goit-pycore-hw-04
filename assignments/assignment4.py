from typing import Dict, List, Tuple


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    parts = user_input.split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.strip().lower(), args


def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        return "Invalid command."
    name, new_phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = new_phone
    return "Contact updated."


def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 1:
        return "Invalid command."
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]


def show_all(contacts: Dict[str, str]) -> str:
    if not contacts:
        return "No contacts found."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)

def main():
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
