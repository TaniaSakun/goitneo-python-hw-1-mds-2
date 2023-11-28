import os
from application.utilites.objects import Birthday
from pathlib import Path

users_path = Path(os.getcwd(), "company_users", "users.csv")

def get_all_users() -> list[Birthday]:
    with open(users_path, "r") as file:
        users = [Birthday(name, birthday) for line in file for name, birthday in [line.strip().split(",")]]

    return users