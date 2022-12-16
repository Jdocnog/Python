#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

text_to_remove = "[name]"
list_of_names = []
list_of_correct_names = []

with open("./Input/Names/invited_names.txt") as invited_names:
    list_of_names = invited_names.readlines()
    for name in list_of_names:
        list_of_correct_names.append(name.strip())

print(list_of_correct_names)
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter_text = starting_letter.read()
    for letter in range(len(list_of_correct_names)):
        change_text = letter_text
        name = list_of_correct_names[letter]
        print(name)
        change_text = change_text.replace(text_to_remove, name)
        print(change_text)
        file = open(f"./Output/ReadyToSend/{name}_Letter.txt", "w")
        file.write(change_text)

file.close()
