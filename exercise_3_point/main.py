# Create objects with class Point, with a tridimensional representation (x, y and z)
# put the string representation and compare with other objects

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"This point contains X={self.x}, Y={self.y} and Z={self.z}"

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def show_x(self):
        return self.x

    def show_y(self):
        return self.y

    def show_z(self):
        return self.z


point_a = Point(2, 4, 6)
point_b = Point(3, 5, 8)
point_c = Point(2, 4, 6)
print(point_a)
print(point_a == point_b)
print(point_b == point_c)
print(point_a == point_c)
