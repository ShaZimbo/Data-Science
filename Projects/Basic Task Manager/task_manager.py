# Importing libraries

""" Module to import current date"""
from datetime import date

# Get today's date in task format
today = date.today()
format_today = today.strftime('%d %b %Y')


# Functions to get user and task data
def validate_user(usernames, passwords):
    """ Function to validate username and password """
    user_data = get_user_data()
    return usernames in user_data and user_data[usernames] == passwords


def get_user_data():
    """ Function to open user file and check for user data"""
    user_dict = {}
    with open("user.txt", "r+", encoding="utf-8") as user_data:
        for line in user_data:
            key, value = [
                decode_special_chars(item.strip()) for item in line.split(",")]
            user_dict[key] = value
    return user_dict


def get_tasks_data():
    """ Function to open tasks file and check for task data"""
    tasks = []
    with open("tasks.txt", "r", encoding="utf-8") as tasks_data:
        for line in tasks_data:
            tasks.append([
                decode_special_chars(item.strip()) for item in line.split(",")
                ])
    return tasks


# Functions for menu options
def menu_selection():
    """ Function to provide menu options"""
    print(f"\n{'Select one of the following options:'}\n")
    print('\u2500' * 50)
    print()
    if username == "admin":
        print(f"{'r':<10} - {'register a user'}\n"
              f"{'ds':<10} - {'display statistics'}\n"
              f"{'du':<10} - {'delete user'}\n")
    print(f"{'tm':<10} - {'task management'}\n"
          f"{'va':<10} - {'view all tasks'}\n"
          f"{'vm':<10} - {'view my tasks'}\n"
          f"{'e':<10} - {'exit'}\n")
    selection = input("Selection: ").lower()
    return selection


# Functions for admin management options
def register_user():
    """ Function to register a user"""
    print("\033[33m\n"
          "NOTE: User names and passwords must exceed 4 characters"
          "NOTE: User names and passwords cannot contain \",\" \n\033[0m")
    while True:
        n_user = sanitize_input(input("Input the new username:\n"))
        if len(n_user) < 5:
            print("\033[31m\nThe user name is too short\n\033[0m")
            continue
        if "," in n_user:
            print("\033[31m\nThe user name cannot contain \",\"\n\033[0m")
            continue
        if n_user in get_user_data():
            print("\033[31m\n"
                  "Username already exists."
                  "Create a unique username\n\033[0m"
                  )
            continue
        break
    while True:
        n_password = sanitize_input(
            input("Assign a password to this user:\n")
            )
        if len(n_password) < 5:
            print("\033[31m\nThe password is too short."
                  "It must be at least 5 characters long.\n\033[0m"
                  )
            continue
        if "," in n_password:
            print("\033[31m\nThe user name cannot contain \",\"\n\033[0m")
        r_entry = sanitize_input(input("Confirm the password:\n"))
        if n_password != r_entry:
            print("\033[31m\nThe passwords do not match."
                  "Please try again.\n\033[0m"
                  )
            continue
        break
    with open("user.txt", "a", encoding="utf-8") as u_file:
        u_file.write(
            f"{encode_special_chars(n_user)}, "
            f"{encode_special_chars(n_password)}\n"
            )
    empty_lines("user.txt")
    print(f"\033[32m\n{n_user} has been registered successfully\033[0m\n")


def display_statistics():
    """ Function to display statistics"""
    print(f"\n{'Task statistics'}\n"
          f"{'Number of tasks:':<20}{len(get_tasks_data())}\n")
    print('\u2500' * 30)
    print()
    print(f"{'User statistics'}\n"
          f"{'Number of users:':<20}{len(get_user_data())}\n")
    print('\u2500' * 30)
    print()


def delete_user(u_list, u_name):
    """ Function to delete a user """
    if u_name in u_list:
        u_list.pop(u_name)
        with open("user.txt", "w", encoding="utf-8") as u_file:
            for u, p in u_list.items():
                u_file.write(f"{u}, {p}\n")
        empty_lines("user.txt")
        print(f"\033[32m\n{u_name} has been deleted successfully\033[0m\n")
    else:
        print("\033[31m\nUser not found\033[0m\n")


# Functions for task management options
def task_management_menu():
    """ Function to provide task management menu options"""
    print(f"\n{'Select one of the following options:'}\n")
    print('\u2500' * 50)
    print()
    print(f"{'a':<10} - {'add task'}\n"
          f"{'m':<10} - {'mark task as complete'}\n"
          f"{'e':<10} - {'edit task'}\n"
          f"{'d':<10} - {'delete task'}\n"
          f"{'b':<10} - {'back to main menu'}\n")
    selection = input("Selection: ").lower()
    return selection


# Functions for task management
def add_task(tasks, t_user, t_title, t_desc, t_due):
    """ Function to add a task """
    t_user = sanitize_input(t_user)
    t_title = sanitize_input(t_title)
    t_desc = sanitize_input(t_desc)
    t_due = sanitize_input(t_due)
    tasks.append([
        encode_special_chars(t_user),
        encode_special_chars(t_title),
        encode_special_chars(t_desc),
        format_today,
        encode_special_chars(t_due),
        "No"
        ])
    with open("tasks.txt", "a+", encoding="utf-8") as tasks_file:
        tasks_file.write(
            f"{encode_special_chars(t_user)},"
            f"{encode_special_chars(t_title)},"
            f"{encode_special_chars(t_desc)},"
            f"{format_today},"
            f"{encode_special_chars(t_due)},"
            f"No\n"
            )
    empty_lines("tasks.txt")
    print("\033[32m\nTask has been added successfully\033[0m\n")


def mark_task_complete(tasks, t_index):
    """ Function to mark a task as complete """
    tasks[int(t_index) - 1][5] = "Yes"
    update_task_data(tasks)
    print("\033[32m\nTask has been marked as complete\033[0m\n")


def edit_task(tasks, t_index):
    """ Function to edit a task """
    # Request field to update
    print("\nSelect the field you would like to update:\n")
    print("1. Assigned user\n"
          "2. Task title\n"
          "3. Task description\n"
          "4. Task due date\n"
          "5. Update entire task\n"
          "6. Back to main menu\n"
          )
    field = input("Selection: ")
    while field not in ["1", "2", "3", "4", "5", "6"]:
        print("\033[31m\nInvalid selection. Please try again\033[0m\n")
        field = input("Selection: ")
    # Update field
    if field == "1":
        t_user = sanitize_input(
            input("Input the assigned username for the task:\n").strip()
            )
        while t_user not in get_user_data():
            print("\033[31m\nInvalid username. "
                  "Provide an existing username.\n\033[0m"
                  )
            t_user = sanitize_input(
                input("Input the assigned username for the task:\n").strip())
        tasks[int(t_index) - 1][0] = encode_special_chars(t_user)
        update_task_data(tasks)
        print("\033[32m\nTask has been updated successfully\033[0m\n")
    elif field == "2":
        t_title = sanitize_input(input("Add the task title:\n").strip())
        tasks[int(t_index) - 1][1] = encode_special_chars(t_title)
        update_task_data(tasks)
        print("\033[32m\nTask has been updated successfully\033[0m\n")
    elif field == "3":
        t_desc = sanitize_input(input("Enter the task description:\n").strip())
        tasks[int(t_index) - 1][2] = encode_special_chars(t_desc)
        update_task_data(tasks)
        print("\033[32m\nTask has been updated successfully\033[0m\n")
    elif field == "4":
        t_due = sanitize_input(input("Enter the task due date "
                                     "\033[33m(DD MMM YYYY)\033[0m:\n"
                                     ).strip())
        # Ensure t_due matches the format DD MMM YYYY
        while len(t_due) != 11 or t_due[2] != " " or t_due[6] != " ":
            print("\033[31m\nInvalid date format. "
                  "Provide the date in the format DD MMM YYYY\n\033[0m"
                  )
            t_due = sanitize_input(input("Enter the task due date "
                                         "\033[33m(DD MMM YYYY)\033[0m:\n"
                                         ).strip())
        tasks[int(t_index) - 1][4] = encode_special_chars(t_due)
        update_task_data(tasks)
        print("\033[32m\nTask has been updated successfully\033[0m\n")
    elif field == "5":
        t_user = sanitize_input(
            input("Input the assigned username for the task:\n").strip()
            )
        while t_user not in get_user_data():
            print("\033[31m\nInvalid username. "
                  "Provide an existing username.\n\033[0m"
                  )
            t_user = sanitize_input(
                input("Input the assigned username for the task:\n").strip()
                )
        t_title = sanitize_input(input("Add the task title:\n").strip())
        t_desc = sanitize_input(input("Enter the task description:\n").strip())
        t_due = sanitize_input(input(
            "Enter the task due date\033[33m(DD MMM YYYY)\033[0m:\n"
            ).strip())
        # Ensure t_due matches the format DD MMM YYYY
        while len(t_due) != 11 or t_due[2] != " " or t_due[6] != " ":
            print("\033[31m\nInvalid date format. "
                  "Provide the date in the format DD MMM YYYY\n\033[0m"
                  )
            t_due = sanitize_input(input("Enter the task due date "
                                         "\033[33m(DD MMM YYYY)\033[0m:\n"
                                         ).strip())
        tasks[int(t_index) - 1] = [
            encode_special_chars(t_user),
            encode_special_chars(t_title),
            encode_special_chars(t_desc),
            format_today, encode_special_chars(t_due),
            "No"]
        update_task_data(tasks)
        print("\033[32m\nTask has been updated successfully\033[0m\n")
    elif field == "6":
        return


def update_task_data(tasks):
    """ Function to update tasks file with new task data"""
    with open("tasks.txt", "w", encoding="utf-8") as tasks_data:
        for t in tasks:
            tasks_data.write(f"{t[0]}, {t[1]}, {t[2]}, {t[3]}, {t[4]}, {t[5]}"
                             "\n")
    empty_lines("tasks.txt")


def delete_task(tasks, t_index):
    """ Function to delete a task """
    tasks.pop(int(t_index) - 1)
    update_task_data(tasks)
    print("\033[32m\nTask has been deleted successfully\033[0m\n")


# Display task function
def display_task(task_item):
    """ Function to display a single task """
    print(f"{'Task:':<20}{task_item[1]}\n"
          f"{'Assigned to:':<20}{task_item[0]}\n"
          f"{'Date assigned:':<20}{task_item[3]}\n"
          f"{'Due date:':<20}{task_item[4]}\n"
          f"{'Task complete?':<20}{task_item[5]}\n"
          f"{'Task description:'}\n{task_item[2]}\n")
    print('\u2500'*100)


def empty_lines(file_name):
    """ Function to remove empty lines in a file """
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    with open(file_name, "w", encoding="utf-8") as file:
        for line in lines:
            if line.strip():
                file.write(line)


def encode_special_chars(input_str):
    """ Function to encode special characters """
    return input_str.replace(",", "%2C")


def decode_special_chars(input_str):
    """ Function to decode special characters """
    return input_str.replace("%2C", ",")


def sanitize_input(input_str):
    """ Function to sanitize input by stripping whitespace """
    return input_str.strip()

# Login Section
# Run task to add initial user


ADMIN = "admin, adm1n"

# Remove empty lines in user file
empty_lines("user.txt")
empty_lines("tasks.txt")

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
        # Ensure admin user is logged in
        if username != "admin":
            print("\033[31m\nYou do not have permission to perform this action"
                  "\n\033[0m"
                  )
        else:
            empty_lines("user.txt")
            register_user()

    # Display statistics section
    elif menu_choice == "ds":
        if username != "admin":
            print("\033[31m\nYou do not have permission to perform this action"
                  "\n\033[0m"
                  )
        else:
            display_statistics()

    # Delete user section
    elif menu_choice == "du":
        if username != "admin":
            print("\033[31m\nYou do not have permission to perform this action"
                  "\n\033[0m"
                  )
        else:
            user_list = get_user_data()
            print()
            print('\u2500' * 100)
            for i, user in enumerate(user_list):
                print(f"User {i + 1}: {user}")
            user_index = input(
                "Select the user number you would like to delete.\n"
                "\033[33m\nEnter b to go back to the main menu:\033[0m\n"
                )
            if user_index == "b":
                continue
            elif int(user_index) == 1:
                print("\033[31m\nYou cannot delete the admin user\033[0m\n")
                continue
            while not user_index.isdigit() or int(user_index) not in range(
                    1, len(user_list) + 1):
                print("\033[31m\nInvalid user number."
                      "Please try again\033[0m\n"
                      )
                user_index = input(
                    "Select the user number you would like to delete:\n"
                    )
            user_to_delete = list(user_list.keys())[int(user_index) - 1]
            delete_user(user_list, user_to_delete)

    # Add task management section
    elif menu_choice == "tm":
        # Ensure no blank lines in tasks file
        empty_lines("tasks.txt")
        while True:
            task_menu_choice = task_management_menu()
            # Add task section
            if task_menu_choice == "a":
                task_user = input("Input the assigned username:\n"
                                  ).strip()
                while task_user not in get_user_data():
                    print("\033[31m\nInvalid username. "
                          "Provide an existing username.\n\033[0m"
                          )
                    task_user = input("Input the assigned username:\n")
                task_title = input("Add the task title:\n").strip()
                task_desc = input("Enter the task description:\n").strip()
                task_due = input("Enter the task due date "
                                 "\033[33m(DD MMM YYYY)\033[0m:\n"
                                 ).strip()
                # Ensure task_due matches the format DD MMM YYYY
                while len(task_due) != 11 or task_due[2] != " " or task_due[
                        6] != " ":
                    print("\033[31m\nInvalid date format. "
                          "Provide the date in the format DD MMM YYYY"
                          "\n\033[0m"
                          )
                    task_due = input("Enter the task due date "
                                     "\033[33m(DD MMM YYYY)\033[0m:\n"
                                     ).strip()
                add_task(get_tasks_data(),
                         task_user, task_title, task_desc, task_due)

            # Delete task section
            elif task_menu_choice == "d":
                task_list = get_tasks_data()
                print()
                print('\u2500' * 100)
                for i, task in enumerate(task_list):
                    print(f"Task {i + 1}")
                    display_task(task)
                task_index = input(
                    "Select the task number you would like to delete:\n"
                    )
                while not task_index.isdigit() or int(task_index) not in range(
                        1, len(task_list) + 1):
                    print("\033[31m\n"
                          "Invalid task number. Please try again\033[0m\n"
                          )
                    task_index = input(
                        "Select the task number you would like to delete:\n"
                        )
                delete_task(task_list, task_index)

            # Mark task as complete section
            elif task_menu_choice == "m":
                task_list = get_tasks_data()
                print()
                print('\u2500' * 100)
                for i, task in enumerate(task_list):
                    print(f"Task {i + 1}")
                    display_task(task)
                index = input(
                    "Select the task number to mark complete:"
                    "\n"
                    )
                while not index.isdigit() or int(index) not in range(
                        1, len(task_list) + 1):
                    print("\033[31m\nInvalid task number."
                          "Please try again\033[0m\n"
                          )
                    index = input(
                        "Select the task number to mark complete:\n"
                        )
                mark_task_complete(task_list, index)

            # Edit task section
            elif task_menu_choice == "e":
                task_list = get_tasks_data()
                print()
                print('\u2500' * 100)
                for i, task in enumerate(task_list):
                    print(f"Task {i + 1}")
                    display_task(task)
                task_index = input("Select the task number to update:\n")
                while not task_index.isdigit() or int(task_index) not in range(
                        1, len(task_list) + 1):
                    print("\033[31m\nInvalid task number."
                          "Please try again\033[0m\n"
                          )
                    task_index = input("Select the task number to update:\n")
                edit_task(get_tasks_data(), task_index)

            # Back to main menu section
            elif task_menu_choice == "b":
                break

            # Invalid section
            else:
                print("\033[31m\nYou have entered an invalid input. "
                      "Please try again\033[0m\n"
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
