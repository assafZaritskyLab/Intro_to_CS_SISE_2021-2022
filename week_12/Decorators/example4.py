class Person:
    def __init__(self, gender):
        self._gender = gender
        pass

    @staticmethod
    def static():
        return "ve ben ellll"

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        """Set the gender"""
        if not isinstance(value, str):
            raise TypeError("must be string")
        self._gender = value

    @property
    def toilet_type(self):
        return 'M' if self._gender in ['M', 'G', 'B', 'Etc.'] else 'W'

    @classmethod
    def give_birth(cls):
        return cls('T')

    def __repr__(self):
        return "I'm a: %s\nAnd i use the %s" % (self.gender, self.toilet_type)


p = Person('M')
p.gender = 'G'
p.gender = 'G'
print(p.toilet_type)
p.toilet_type = 'ATGC'
print(p.give_birth())
