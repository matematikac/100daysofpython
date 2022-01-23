# creating the empty list of names
name_list = []
# reading from txt with names and appending them in list of names
with open('/Users/Riznica Mudrosti/PycharmProjects/Mail Merge Project/Input/Names/invited_names.txt') as file: # apsolutna putanja do fajla
    for line in file:
        name_list.append(line.strip())
# creating a letter for each person in a name_list
for name in name_list:
    invitation = 'letter_for_' + name
# taking the starting format of letter and replacing the content
    with open('./Input/Letters/starting_letter.txt') as file: # relativna putanja do fajla
        f = file.read()
        f = f.replace('[name]', name)
# writing the letter
    with open('Output/ReadyToSend/{}.txt'.format(invitation),'w') as file: # relativna putanja do fajla moze bez ./
        file.write(f)