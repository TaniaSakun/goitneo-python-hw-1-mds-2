from application.utilites.logger import logger_instance

def print_birthdays(birthday_by_day_dict):
    for weekday, users in birthday_by_day_dict.items():
        logger_instance.info(f"{weekday}: {', '.join(users)}")
    print("\n")