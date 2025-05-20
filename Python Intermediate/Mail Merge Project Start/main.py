""" Create invitations using the template and names """
LETTER_PATH = (
    ".\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt"
)
NAMES_PATH = (
    ".\\Mail Merge Project Start\\Input\\Names\\invited_names.txt"
)

with open(NAMES_PATH, "r", encoding="utf-8") as names:
    for line in names.readlines():
        name = line.strip("\n")
        READY_PATH = (
                    f".\\Mail Merge Project Start\\Output\\ReadyToSend\\"
                    f"{name}.txt"
        )
        with open(LETTER_PATH, "r", encoding="utf-8") as letter:
            with open(READY_PATH, "w", encoding="utf-8") as invite:
                for lines in letter.readlines():
                    lines.strip()
                    x = lines.replace("[name]", f"{name}")
                    invite.write(x)
