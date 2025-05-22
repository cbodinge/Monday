from .Node import Node
from .Items import Items

class ItemsPage(Node):
    def __init__(self, **kwargs):
        self.items = Items(parent=self, name='items')

        super().__init__(**kwargs)
