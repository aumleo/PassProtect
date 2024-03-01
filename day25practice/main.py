# with open('weather_data.csv') as file:
#     c=file.readlines()
#     print(c)

'''USING INBUILT CSV reader'''
# import csv
# from re import template

# data_list = []
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     for r in data:
#         data_list.append(r)

# temperatures = []
# for val in data_list[1:]:
#     temperatures.append(int(val[1]))
# print(temperatures)

'''Pandas'''

import pandas
data = pandas.read_csv('weather_data.csv')

#convert data to a list
temp = data['temp'].to_list()

#dataseries.max() similarly can do other math functions
print(data['temp'].max())
print('\n')

#directly accsessing the columns (without [])
print(data.condition)
print('\n')

#Accessing ROWS -
print(data[data.day == 'Monday']) #monday specific row
print('\n')
data[data.temp == data.temp.max()] #to get the row where the temp was max
#Get the specific col for a specific row
monday = data[data.day == 'Monday']
print(monday.condition)
print('\n')


#Create a DataFrame
data_d = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
data = pandas.DataFrame(data_d)
print(data)
#OP -
#       Name  Age         City
# 0    Alice   25     New York
# 1      Bob   30  Los Angeles
# 2  Charlie   35      Chicago
data.to_csv('new_data.csv')



