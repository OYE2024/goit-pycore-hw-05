def input_error(func):
    """
    Декоратор input_error обробляє вийнятки та всі помилки введеня користувача. 
    """
    def wroper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone, please."
        except KeyError:
            return "User didn't found."
        except IndexError:
            return "Enter user name, please."
    return wroper


def parse_input(user_input):
    """
    Функція parse_input розбирає введений користувачем рядок на команду та її аргументи.
    Команди та аргументи розпізнаються незалежно від регістру введення.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    """
    Функція add_contact додає нового користувача до словника, приймаючи команду, ім'я та телефон.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    """
    Функція change_contact вносить зміни в існуючий контакт у словнику, приймаючи команду, ім'я та телефон.
    """
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(args, contacts):
    """
    Функція show_phone повертає користувачу контакт із словника, приймаючи команду та ім'я.
    """
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number: {contacts[name]}"
    elif name not in contacts:
        raise KeyError
    else:
        raise IndexError


@input_error
def show_all(contacts):
    """
    Функція show_all повертає всі контакти із словника, приймаючи команду.
    """
    if len(contacts) > 0:
        result = ''
        for name in contacts:
            result += f"{name}'s phone number: {contacts[name]}"
        return result
    else:
        raise KeyError


def main():
    """
    Функція main управляє основним циклом обробки команд.
    Команди розпізнаються незалежно від регістру введення або зайвих пропусків.
    """
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print('Invalid command')


if __name__ == "__main__":
    main()
