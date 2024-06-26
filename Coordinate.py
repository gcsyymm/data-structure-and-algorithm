class Coordinate:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Coordinate(x, y)

    def __repr__(self):
        return f"({self.x}, {self.y})"


coord1 = Coordinate(1, 2)
coord2 = Coordinate(2, 4)
print(coord1 + coord2)
