""" Converting alternative characters / words """
phrase = input("Enter a phrase: ")

CHARACTER_PHRASE = []
split_phrase = phrase.split()
word_phrase = []

# Make alternate characters upper and lower case
for i, c in enumerate(phrase):

    if i % 2 == 0:
        CHARACTER_PHRASE.append(phrase[i].upper())

    else:
        CHARACTER_PHRASE.append(phrase[i].lower())

CHARACTER_PHRASE = "".join(CHARACTER_PHRASE)
print(CHARACTER_PHRASE)

# Make alternate words upper and lower case
for index, word in enumerate(split_phrase):
    if index % 2 == 0:
        word_phrase.append(word.upper())
    else:
        word_phrase.append(word.lower())

WORD_PHRASE = " ".join(word_phrase)
print(WORD_PHRASE)
