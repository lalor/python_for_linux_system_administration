class Person(object):
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0 or age > 100:
            raise ValueError('age is illegal')
        self._age = age

jason = Person('Jason Statham', 50)
jason.age = -1
