class Trees:
    biology_class = 'Plant'

    def __init__(self, name, height, leaf_color):
        self.name = name
        self.height = height
        self.leaf_color = leaf_color

    def bloom(self):                  # методы
        return 'I can blooming'        # я могу расцвести

    def get_name(self):
        return f'The name of the tree is {self.name}'


tree1 = Trees('Palma', 4, 'green')
print(tree1.name)
print(tree1.get_name())
print(tree1.leaf_color)
print(tree1.biology_class)

tree2 = Trees('Apple_tree', 3, 'green')
print(tree2.biology_class)
print(tree2.get_name())