import pandas

# reading a nato_phonetic_alphabet file that is csv file and after iterating throw rows
nato_phonetic_df = pandas.read_csv('nato_phonetic_alphabet.csv')
# creating a comprehension dictionary with {new_key:new_value for (index, row) in data_frame.iterrows() if test}
nato_phonetic_dictionary = {row['letter']: row['code'] for (index, row) in nato_phonetic_df.iterrows()}
#creating a list of nato phonetic code for the entered name
nato_phonetic_code = []
ind = 0
while ind == 0:
    # taking a name from a user
    name = input('Type your name using letters: ').upper()

    if name.isalpha():
        ind = 1
        nato_phonetic_code = [nato_phonetic_dictionary[element] for element in name]

    else:
        print('You should enter your name using letters, not numbers or special characters')

print('\nnato phonetic code for a name {} is :'.format(name.capitalize()))
# printing only the elements of a list, separated with , and space, without brackets
print(*nato_phonetic_code, sep=', ')