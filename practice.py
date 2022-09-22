import pickle
import json
import random
import datetime

#1
# name = input('Please input your name: ')
# age = int(input('Please input your age: '))

# def print_user_info(name, age):
#     print('Hi ', name, ' Your age is: ', age)


# def decades_calc(age):
#   print(age // 10)


# print_user_info(name, age);

# decades_calc(age)

# print('-' * 20)

# #2

# name_list = ['Aleksei', 'Ben', 'Natasha', 'Alex']

# def get_names_length(list):
#     for name in list:
#       if len(name) > 5 and ('n' in name or 'N' in name):
#         print(name, len(name))



# def clear_list(list): 
#     while len(list) != 0:
#       list.pop()
#     print(list)


# get_names_length(name_list)
# clear_list(name_list)


#3

# person_list = [
#     {
#       'name': 'Max',
#       'age': 29,
#       'hobbies': 'cycling'
#     },
#     {
#       'name': 'Anna',
#       'age': 13,
#       'hobbies': 'coocking'
#     },
#      {
#       'name': 'Bob',
#       'age': 21,
#       'hobbies': 'workout'
#     },
#   ]

# names_list = [name["name"] for name in person_list]
# print(names_list)

# print(all(person["age"] > 20 for person in person_list))

# copy_person_list = [person.copy() for person in person_list]
# copy_person_list[0]["name"] = 'Vlad'
# print(copy_person_list)
# print(person_list)

# a,b,c = person_list
# print(a)
# print(b)
# print(c)

#4

# a = [10, 50, 75, 20]

# def result_print(f):
#     print(f(29))

# result_print(lambda el: el * 2)


# def result_print2(f, *args):
#     for argumet in args:
#         print(f(argumet))

# result_print2(lambda el: el * 2, 4, 10, 24, 52)


# def result_print3(f, *args):
#     for argumet in args:
#         print('Result {:^20.2f}'.format(f(argumet)))

# result_print2(lambda el: el / 2, 4, 10, 24, 51)


# #5


# print('Random 0 - 1 numbers', random.randint(0, 1))
# print('Random 0 - 10 numbers',random.randint(0, 10))

# rn = random.random()

# print(str(rn) + str(datetime.datetime.now()))

#6

# user_input_status = True
# file = []
# binary = []
#
#
# def save_data():
#     file_input = input('write somthing: ');
#     file.append(file_input)
#     with open('infinite_file.txt', mode='w') as f:
#         f.write(json.dumps(file))
#
#
# def load_data():
#     with open('infinite_file.txt', mode='r') as f:
#         file_content = json.loads(f.read())
#         for line in file_content:
#             print(line)
#             line = f.readlines()
#
#
# def save_binary_data():
#     file_input = input('write somthing: ');
#     binary.append(file_input)
#     with open('infinite_file.p', mode='wb') as f:
#         f.write(pickle.dumps(binary))
#
#
# def load_binary_data():
#     with open('infinite_file.p', mode='rb') as f:
#         file_content = pickle.loads(f.read())
#         for line in file_content:
#             print(line)
#
#
# while user_input_status:
#     user_input = input('choose: ')
#     if user_input == 'q':
#         user_input_status = False
#     elif user_input == 'r':
#         load_data()
#     elif user_input =='w':
#         save_data()
#     elif user_input == 'wb':
#         save_binary_data()
#     elif user_input == 'rb':
#         load_binary_data()


