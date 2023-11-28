from typing import Union
from application.bot.service import (parse_input, add_contact, change_contact, get_phone, get_help, get_all_contacts)
from application.utilites.constants import Constants

def bot_handler(user_input: str, contacts: dict) -> Union[str, None]:
    cmd, *args = parse_input(user_input)

    match cmd:
        case "add":
            return add_contact(args, contacts)
        case "change":
            return change_contact(args, contacts)
        case "phone":
            return get_phone(args, contacts)
        case "all":
            return get_all_contacts(contacts)
        case "help":
            return get_help()
        case "hello":
            return Constants.help_question
        case "exit":
            return None
        case "close":
            return None
        case _:
            return Constants.invalid_command