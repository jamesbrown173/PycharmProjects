

with open("/Users/jamesbrown/PycharmProjects/Mail Merge Project Start/Input/Names/invited_names.txt", 'r') as names_file:
    names = [name.strip() for name in names_file.readlines()]

with open("/Users/jamesbrown/PycharmProjects/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as letter_file:
    new_letter = [new_letter.replace('[name]', 'chicken')]



#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



