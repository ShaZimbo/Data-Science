""" This script creates a student register for an exam. """
number_of_students = int(
    input("Number of students writing this exam:\n")
    )

with open('reg_form.txt', 'w', encoding='utf-8') as student_register:
    for n in range(number_of_students):
        student_id = input("Please enter the student ID:\n")
        student_register.write(
            f"Student ID: {student_id} - Signed: {'_' * 20}\n"
            )
