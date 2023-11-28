from application.birthday.handler import birthday_handler
from application.bot.handler import bot_handler
from application.utilites.constants import Constants
from application.utilites.get_all_users import get_all_users
from application.utilites.logger import logger_instance
from application.utilites.print_birthday import print_birthdays
from application.utilites.print_task import print_task

class Application:
    
    def birthday_task(self):
        print_task(Constants.task_birthday)
        print_birthdays(birthday_handler(get_all_users()))
        return self

    def bot_task(self):
        contacts = {}
        print_task(Constants.task_bot)

        while True:
            logger_instance.info(f"\n" + Constants.enter_command)
            user_input = input()

            result = bot_handler(user_input, contacts)
            if not result:
                logger_instance.warn(Constants.good_bye_message)
                break
            logger_instance.warn(result)
        return self