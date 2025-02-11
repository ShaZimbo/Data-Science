""" This script replaces all "!" with a space,
converts the sentence to uppercase,
and prints the sentence in reverse order. """

# Define the sentence
FOX_STATEMENT = "The!quick!brown!fox!jumps!over!the!lazy!dog."
# Remove all "!" and replace these with a space
FOX_STATEMENT_UPDATE = FOX_STATEMENT.replace("!", " ")
# Convert the sentence to uppercase
FOX_STATEMENT_UPPER = FOX_STATEMENT_UPDATE.upper()
print(f"{FOX_STATEMENT_UPDATE}"
      f"\n{FOX_STATEMENT_UPPER}"
      # Print the sentence in reverse order
      f"\n{FOX_STATEMENT_UPDATE[::-1]}"
      )
