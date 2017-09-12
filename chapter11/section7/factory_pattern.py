class Shape(object):pass
class Circle(Shape):pass
class Square(Shape):pass

for name in ["Circle", "Square"]:
    cls = globals()[name]
    obj = cls()
