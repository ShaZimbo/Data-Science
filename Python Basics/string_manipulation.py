""" This program manipulates a sentence in various ways. """
str_manip = input("Please enter a sentence: ")
replace_last = str_manip.replace(str_manip[-1], "@")

# Print manipulated variations of the sentence
print(f"Length of the sentence is: {len(str_manip)}"
      f"\nLast character in the sentence is: {str_manip[-1]}"
      f"\nLast character replaced with @ throughout: {replace_last}"
      f"\nLast three characters in reverse order: {str_manip[:-4:-1]}"
      f"\nFirst three characters and last three characters: "
      f"{str_manip[:3]+str_manip[-2:]}"
      )
