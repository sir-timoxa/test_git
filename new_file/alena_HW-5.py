# 5.1. Создайте любой класс с произвольным количеством подклассов,
# экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private.
# Соответственно, для получания значений этого атрибута
#     нужно использовать методы get и set

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

    def make_a_bite(self):
        return "I've already made a bite! "