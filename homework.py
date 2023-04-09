class Boat:
        engine_class = 'engined'
        def __init__(self, name, power, color):
            self.name = name
            self.power = power
            self._color = color

        def seal(self):
            return 'It can seal in the ocean'

        def get_color(self):
            return f'This boat color is {self._color}'


boat1 = Boat('Bull', 56, 'red')
print(boat1.name)
print(boat1.get_color)
print(boat1.engine_class)

boat2 = Boat('Whale', 30, 'blue')
print(boat2.name)
print(boat2.get_color())
print(boat2.engine_class)


class flatboat(Boat):
    def __init__(self, name, power, color):
        self.name = name
        self.power = power

    def get_color(self):
        return f'This boat has no color'



boat3 = flatboat('Lodka', 10, 'Null')

print(boat3.get_color())
