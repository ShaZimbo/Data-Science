# Importing libraries

""" Module to import current date"""
from datetime import date

# Get today's date in task format
today = date.today()
format_today = today.strftime('%d %b %Y')


# Functions
def get_user_data():
    """ Function to open user file and check for user data"""
    user_dict = {}
    with open("user.txt", "r+", encoding="utf-8") as user_data:
        for line in user_data:
            key, value = [item.strip() for item in line.split(",")]
            user_dict[key] = value
    return user_dict


def get_tasks_data():
    """ Function to open tasks file and check for task data"""
    task_list = []
    with open("tasks.txt", "r", encoding="utf-8") as tasks_data:
        for line in tasks_data:
            task_list.append([item.strip() for item in line.split(",")])
    return task_list


def menu_selection():
    """ Function to provide menu options"""
    print(f"\n{'Select one of the following options:'}\n")
    print('\u2500' * 50)
    print()
    if username == "admin":
        print(f"{'r':<10} - {'register a user'}\n"
              f"{'ds':<10} - {'display statistics'}")
    print(f"{'a':<10} - {'add task'}\n"
          f"{'va':<10} - {'view all tasks'}\n"
          f"{'vm':<10} - {'view my tasks'}\n"
          f"{'e':<10} - {'exit'}\n")
    selection = input("Selection: ").lower()
    return selection


def display_task(task_item):
    """ Function to display a single task """
    print(f"{'Task:':<20}{task_item[1]}\n"
          f"{'Assigned to:':<20}{task_item[0]}\n"
          f"{'Date assigned:':<20}{task_item[3]}\n"
          f"{'Due date:':<20}{task_item[4]}\n"
          f"{'Task complete?':<20}{task_item[5]}\n"
          f"{'Task description:'}\n{task_item[2]}\n")
    print('\u2500'*100)


def validate_user(usernames, passwords):
    """ Function to validate username and password """
    user_data = get_user_data()
    return usernames in user_data and user_data[usernames] == passwords


# Login Section
# Run task to add initial user
ADMIN = "admin, adm1n"

with open("user.txt", "a+", encoding="utf-8") as user_file:
    user_file.seek(0)
    content = user_file.read()

    if ADMIN not in content:
        user_file.write(f"{ADMIN}\n")

# Request login details:
print("Welcome to the task manager\n")
username = input("Please enter your username:\n")
password = input("Please enter your password:\n")

# Validate username and password against user file
while not validate_user(username, password):
    print("\n\033[31mIncorrect username or password. "
          "Please try again\n\033[0m"
          )
    username = input("Please enter your username:\n")
    password = input("Please enter your password:\n")

print("\033[32m\nYou have successfully logged in\033[0m")

# Menu section
while True:
    menu_choice = menu_selection()
    # Register a user section
    if menu_choice == "r":
        if username != "admin":
            print("\033[31m\n"
                  "You do not have permission to perform this action\n\033[0m"
                  )
        else:
            print("\033[33m\nNOTE: "
                  "User names and passwords must exceed 4 characters"
                  "\n\033[0m"
                  )
            while True:
                new_user = input("Please input the new username:\n")
                if len(new_user) < 5:
                    print("\033[31m\nThe user name is too short\n\033[0m")
                    continue
                if new_user in get_user_data():
                    print("\033[31m\nUsername already exists. "
                          "Please create a unique username\n\033[0m"
                          )
                    continue
                break
            while True:
                new_password = input("Please assign a password to this user:"
                                     "\n"
                                     )
                if len(new_password) < 5:
                    print("\033[31m\nThe password is too short. "
                          "It must be at least 5 characters long.\n\033[0m"
                          )
                    continue
                re_entry = input("Please confirm the password:\n")
                if new_password != re_entry:
                    print("\033[31m\nThe passwords do not match. "
                          "Please try again.\n\033[0m"
                          )
                    continue
                break
            with open("user.txt", "a", encoding="utf-8") as user_file:
                user_file.write(f"\n{new_user}, {new_password}")
            print(f"\033[32m\n"
                  f"{new_user} has been registered successfully\033[0m\n"
                  )

    # Display statistics section
    elif menu_choice == "ds":
        if username != "admin":
            print("\033[31m\nYou do not have permission to perform this action"
                  "\n\033[0m"
                  )
        else:
            print(f"\n{'Task statistics'}\n"
                  f"{'Number of tasks:':<20}{len(get_tasks_data())}\n")
            print('\u2500' * 30)
            print()
            print(f"{'User statistics'}\n"
                  f"{'Number of users:':<20}{len(get_user_data())}\n")
            print('\u2500' * 30)
            print()

    # Add task section
    elif menu_choice == "a":
        task_user = input("Please input the assigned username for the task:\n"
                          ).strip()
        while task_user not in get_user_data():
            print("\033[31m\nInvalid username. "
                  "Please provide an existing username.\n\033[0m"
                  )
            task_user = input(
                "Please input the assigned username for the task:\n"
            )
        task_title = input("Please add the task title:\n").strip()
        task_desc = input("Please enter the task description:\n").strip()
        task_due = input("Please enter the task due date "
                         "\033[33m(DD MMM YYYY)\033[0m:\n"
                         ).strip()
        with open("tasks.txt", "a+", encoding="utf-8") as tasks_file:
            tasks_file.write(f"\n"
                             f"{task_user}, "
                             f"{task_title}, "
                             f"{task_desc}, "
                             f"{format_today}, "
                             f"{task_due}, No"
                             )
        print(f"\033[32m\nTask {task_title} has been added successfully"
              f"\n\033[0m"
              )

    # View all tasks section
    elif menu_choice == "va":
        print()
        print('\u2500' * 100)
        for task in get_tasks_data():
            display_task(task)

    # View my tasks section
    elif menu_choice == "vm":
        user_tasks = [task for task in get_tasks_data() if username == task[0]]
        if user_tasks:
            print()
            print('\u2500' * 100)
            for task in user_tasks:
                display_task(task)
        else:
            print("\nYou have no assigned tasks\n")

    # Exit section
    elif menu_choice == 'e':
        print(f"\nGoodbye {username}!!!\n")
        exit()

    # Invalid section
    else:
        print("\033[31m\nYou have entered an invalid input. "
              "Please try again\033[0m\n"
              )
