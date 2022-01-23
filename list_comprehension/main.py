# printing double list elements in given range in list comprehension
double = [2*n for n in range(1,5)]

print(double)

print('--------------------------------------------------------')

# printing names in caps look
names = ['Milos', 'Sanja']

caps_look = [name.upper() for name in names]

print(caps_look)

print('--------------------------------------------------------')

# counting the number of showing each element in a list, and creating a dictionary
MyList = ["a", "b", "a", "c", "c", "a", "c"]

my_dict = {i:MyList.count(i) for i in MyList}

print('number of repetition of each element in a list:{} is: \n{}'.format(MyList, my_dict))

print('--------------------------------------------------------')

# counting the number of showing each word in text
text = "What is the Airspeed Velocity of an Unladen Swallow? What"

word = text.split()

word_counting = {element: word.count(element) for element in word}

print("the number of repetition of each word in text is: {}".format(word_counting))

print('--------------------------------------------------------')

# taking two files and compering the same elements in them
with open("file1.txt") as file1:
    list_1 = file1.readlines()
with open("file2.txt") as file2:
    list_2 = file2.readlines()
# converting lists in a lists with integer numbers
list_1_int = []
for element in list_1:
    element = int(element)
    list_1_int.append(element)
list_2_int = []
for element in list_2:
    element = int(element)
    list_2_int.append(element)
word_counting = [int(element) for element in list_1_int if element in list_2_int]

print('the same elements in those two files,\nfile1:{} and\n file2:{}\nare: {}'.format(list_1_int, list_2_int, word_counting))

print('--------------------------------------------------------')

#translating C degrees from dictionary weather_c to a F degrees in dictionary weather_f, using: temp_f = temp_c*9/5 + 32
weather_c = {
    "Monday":  12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: 9*temp_c/5 + 32 for (day,temp_c) in weather_c.items() }

print('Fahrenheit degrees this weak:{}'.format(weather_f))

print('--------------------------------------------------------')

# creating pandas data frame from a given dictionary of students names, gender and height in cm, and then calculating mean high of male and female
student = {
    'name':['John', 'Michael', 'Joana', 'Ket', 'Lara','Peter', 'Adam','Jessica','Jeff'],
    'gender':['m','m','f','f','f','m','m','f','m'],
    'height':[187,175,168,160,175,185,165,163,196],
}

# importing pandas for creating a data frame
import pandas

student_df = pandas.DataFrame(student)

print('Data Frame made from dictionary of students:{} is \n{}'.format(student, student_df))
# defining the male and female starting height and number of them
male_h = 0
female_h = 0
num_m = 0
num_f = 0
# iterating throw rows in our data frame and calculating the total height of a male and total height of a female, and the number of each of them
for (index,row) in student_df.iterrows():
   if row['gender'] == 'm':
       male_h += row['height']
       num_m += 1
   elif row['gender'] == 'f':
       female_h += row['height']
       num_f += 1
print( 'The average height of a {} students is: {}cm\nMean height of a {} female is: ''{}cm\nMean height of a {} male is: {}cm'
  .format(num_f + num_m, round((male_h + female_h)/(num_m + num_f), 2), num_f,round(female_h/num_f, 2), num_m, round(male_h/num_m, 2)))

print('--------------------------------------------------------')