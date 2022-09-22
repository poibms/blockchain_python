from food import Food


class Fruit(Food):
    def clean(self):
        print('Cleaning my lovely {}'.format(self.name))


peer = Fruit('Peer', 'fruit')
peer.clean()
peer.describe()
