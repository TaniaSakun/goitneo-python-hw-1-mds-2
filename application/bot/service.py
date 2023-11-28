from application.utilites.objects import Contact
from application.utilites.constants import Constants
from typing import List, Dict

def parse_input(user_input: str) -> List[str]:
    cmd, *args = user_input.split()
    return [cmd.strip().lower(), *args]

def add_contact(args: List, contacts: Dict[str, str]) -> str:
    try:
        name, phone = args
        contacts[name] = phone
        return Constants.contact_added
    except: 
        return Constants.invalid_input

def change_contact(args: List, contacts: Dict[str, str]) -> str:
    try:
        name, phone = args
        contacts[name] = phone
        return Constants.contact_changed
    except: 
        return Constants.invalid_input

def get_help() -> str:
    return Constants.help_text

def get_phone(args: List, contacts: Dict[str, str]) -> str:
    try:
        return contacts.get(args[0], Constants.contact_not_found)
    except: 
        return Constants.invalid_input

def get_all_contacts(contacts: Dict[str, str]) -> str:
    try:
        if not contacts:
            return Constants.no_contacts_text
        return "\n".join(f"{name} {phone}" for name, phone in contacts.items())
    except: 
        return Constants.invalid_input