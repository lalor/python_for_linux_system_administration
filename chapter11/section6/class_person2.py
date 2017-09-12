class Person(object):
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0 or age > 100:
            raise ValueError('age is illegal')
        self._age = age
