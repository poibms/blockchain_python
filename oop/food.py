class Food:
    def __init__(self, name, kind='normal'):
        self.name = name
        self.kind = kind

    # @classmethod
    def describe(cls):
        print('Name: {}, Kind: {}'.format(cls.name, cls.kind))

food = Food('apple', 'bad')
food.describe()

food2 = Food('banana', 'new')
food2.describe()

# Food.__dict__
