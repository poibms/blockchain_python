from food import Food


class Meat(Food):
    def __init__(self, name):
        super().__init__(name)

    def cook(self):
        print('cooking my lovely {} Condition: {}'.format(self.name, self.kind))


peer = Meat('Chicken')
peer.cook()