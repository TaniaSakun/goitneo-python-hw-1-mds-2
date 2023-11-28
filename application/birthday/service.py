from datetime import datetime, timedelta
from collections import defaultdict
from application.utilites.constants import Constants

def validate_data(user):
    # Username validation
    if not user.name:
        print(Constants.invalid_username_error)
        return False

    return True

def get_birthdays_per_week(users: list) -> defaultdict(list):
    today = datetime.today().date()
    birthdays_by_day = defaultdict(list)

    for user in users:
        date_format = "%Y-%m-%d"
        if not validate_data(user):
            continue
        
        name = user.name
        birthday = datetime.strptime(user.birthday, date_format).date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            day_of_week = (today + timedelta(days=delta_days)).strftime("%A")
            if birthday_this_year.weekday() >= 5:
                day_of_week = Constants.monday
            birthdays_by_day[day_of_week].append(name)
                
    return birthdays_by_day