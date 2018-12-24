class Base:
    _name = "Базовый"

    def __str__(self):
        return "I'm " + self._name + " exemplar!"

    def do_something(self, data):
        for i in range(5):
            print(data)


class Derived(Base):
    _name = "Производный"

    def do_something(self, data):
        print(data*3)


base = Base()
print(base)
base.do_something("ABC")

derived = Derived()
print(derived)
derived.do_something("ABC")
