class Sai:
    def __init__(self, n, color, age):
        self.ns = n
        self._colors = color
        self.__ages = age

    def saikiran_age(self):
        print(f"{self.__ages}")

    def saikiran_color(self):
        print(f"{self._colors}")

    def nu(self):
        print(f"{self.ns}")
class kiran(Sai):
    def show(self):
        print(f"{self._colors}, {self.__ages}")
h = kiran(2,"white",23)
h.show()