#1
name = input('Please input your name: ')
age = int(input('Please input your age: '))

def print_user_info(name, age):
    print('Hi ', name, ' Your age is: ', age)


def decades_calc(age):
  print(age // 10)


print_user_info(name, age);

decades_calc(age);

print('-' * 20)

#2

name_list = ['Aleksei', 'Ben', 'Natasha', 'Alex']

def get_names_length(list):
    for name in list:
      if len(name) > 5 and ('n' in name or 'N' in name):
        print(name, len(name))



def clear_list(list): 
    while len(list) != 0:
      list.pop()
    print(list)


get_names_length(name_list)
clear_list(name_list)

