""" Module to open and read lines in a document,
seperating names from date of birth """

dob_file = open('DOB.txt', 'r+', encoding='utf-8')

lines = dob_file.readlines()

# Create two lists, one for names and one for birthdates.
names = []
birthdates = []

# Store the names and birthdates in separate lists.
for i in lines:
    list_words = i.strip().split()
    FULL_NAME = " ".join(list_words[0:2])
    DATE_OF_BIRTH = " ".join(list_words[2:5])
    names.append(FULL_NAME)
    birthdates.append(DATE_OF_BIRTH)

NAME_STRING = "\n".join(names)
BIRTHDATES_STRING = "\n".join(birthdates)
print("Name\n" + NAME_STRING + "\n")
print("Birthdate\n" + BIRTHDATES_STRING)

dob_file.close()
