class Constants:
    invalid_username_error = "Error: Username cannot be empty. Skip the user with date."
    monday = "Monday"
    
    contact_added = "Contact added."
    contact_changed = "Contact changed."
    contact_not_found = "Contact not found."
    help_text = """
    These are common commands used in various situations:
    start commands
        hello       Starting command
    set commands 
        add         Adds a new user with a phone number. Note: takes name and phone number as parameters
        change      Changes phone number for the concrete user. Note: takes name and phone number as parameters
               
    get commands
        all         Gets list of all created users with phone numbers
        help        In case you need help with detailed commands names and descriptions
        phone       Gets phone number of the concrete user. Note: takes a name as a parameter
    
    end commands
        close       Ends the interaction
        exit        Ends the interaction
    """
    no_contacts_text = """Contacts have not been added yet. To add a contact, please enter the following command: 
    'add username phone', where username is the name of user, and phone is a user phone number"""
    invalid_input = "Invalid command. Try again"
    invalid_command = "Invalid command."
    help_question = "How can I help you?"
    good_bye_message = "Good bye!"
    
    task_birthday = "Birthday task"
    task_bot = "Bot task"
    enter_command = "Enter a command: "
    
