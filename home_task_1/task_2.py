def hello_command_handler(*args):
    return "How can I help you?"


def add_contact_handler(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact_handler(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact with '{name}' name is not found."


def show_phone_handler(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact with '{name}' name is not found."


def show_all_handler(args, contacts):
    all_contacts = []
    for name, phone in contacts.items():
        all_contacts.append(f"{name} - {phone}")
    return "\n".join(all_contacts)


COMMANDS = {
    "hello": hello_command_handler,
    "add": add_contact_handler,
    "change": change_contact_handler,
    "phone": show_phone_handler,
    "all": show_all_handler,
}


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command in COMMANDS:
            print(COMMANDS[command](args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
