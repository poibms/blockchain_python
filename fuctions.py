def unlimited_arguments(*args, **key_args):
    print(key_args)
    for argumet in key_args:
        print(argumet)


unlimited_arguments(1,2,3,4,5, name ='Max', age = 12 )