class Pet:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    def sleep(self):
        return "I can sleep"

    def eat(self):
        return "Feed me now!"


class Cat:
    def __init__(self, name, weight, color):
        super().__init__(name, weight, color)
        self.paws = paws

