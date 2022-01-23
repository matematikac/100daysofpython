# weather = []
# with open('weather_data.csv') as file:
#     for line in file:
#         weather.append(line.strip())
# print(weather)
#
# import csv
#
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temp = []
#     for row in data:
#         if row[1] == 'temp':
#             continue
#         else:
#             temp.append(int(row[1]))

import pandas


#data = pandas.read_csv('weather_data.csv')
# print(data ['temp'])
#
# #converting to dictionary
# data_dict = data.to_dict()
# print(data_dict)
#
# # converting of a row with temperature to a list
# temp_list = data['temp'].to_list()
# print(temp_list)
# average = sum(temp_list) / len(temp_list)
# print(average)
# # iz bibiloteke pandasa mozemo odmah da iskoristimo funkciju za aritmeticku sredinu, ili medianu
# print(data['temp'].mean(), data['temp'].median())
# print(data['temp'].max(),data['temp'].min())

# rad sa redovima umesto sa kolonama

#print('hello',data[data['temp'] == data['temp'].max()]) #secemo po maksimalnoj temperaturi
# sunny =data[data['condition'] == 'Sunny']
# print('hy',sunny,sunny['temp'],type(sunny['temp'][0]))

# #converting monday temperature from C to F with formula F = 1.8*C + 32
#
# monday_t = data[data['day'] == 'Monday']
# print(1.8*float(monday_t['temp'])+32) # ovo je sada temperatura u Farenhajtu

# creating a dataframe from scratch
#
# data_dict = {'city':['Beograd','Nis','Novi Sad'],
#              'population':[3.4, 0.9, 1.2],
#              }
# data = pandas.DataFrame(data_dict)
# #print(data)
# data.to_csv('new_csv.csv')

# creating a squirrel_count.csv
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
num_gray = len(data[data['Primary Fur Color'] == 'Gray'])
num_cinnamon = len(data[data['Primary Fur Color'] == 'Cinnamon'])
num_black = len(data[data['Primary Fur Color'] == 'Black'])
dict_squirrel_count = { 'Fur Color':['Gray','Cinnamon','Black'],
                        'Count': [num_gray,num_cinnamon,num_black],
                        }
squirrel_count = pandas.DataFrame(dict_squirrel_count)
squirrel_count.to_csv('squirrel_count.csv')
print(squirrel_count)
