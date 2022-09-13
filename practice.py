name = input('Please input your name: ')
age = int(input('Please input your age: '))

def print_user_info(name, age):
    print('Hi ', name, ' Your age is: ', age)


def decades_calc(age):
  print(age // 10)


print_user_info(name, age);

decades_calc(age);