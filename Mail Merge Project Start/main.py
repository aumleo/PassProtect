#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

TEMP = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names=names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    contents=letter_file.read()
    for name in names:
        _name = name.strip()
        new_letter = contents.replace(TEMP, _name)
        with open(f"./Output/ReadyToSend/Letter_for_{_name}.txt", mode='w') as the_letter:
             the_letter.write(new_letter)
