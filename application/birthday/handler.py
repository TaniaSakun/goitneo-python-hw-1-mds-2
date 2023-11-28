from application.birthday.service import get_birthdays_per_week

def birthday_handler(users):
    if not len(users):
        return {}

    return get_birthdays_per_week(users)