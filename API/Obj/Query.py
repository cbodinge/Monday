from .Node import Node
from .Boards import Boards
from .Items import Items

class Query(Node):
    def __init__(self):
        self.boards = Boards(parent=self, name='boards')
        self.items = Items(parent=self, name='items')

        super().__init__(active=True, name='query')

    def __str__(self) -> str:
        return 'query ' + super().__str__()

