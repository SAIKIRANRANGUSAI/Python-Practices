"""
    Encapsulation:  wrapping variablr and methods into single unit.
     -> Encapsulation is known as data hididng
     -> uses protect or private to hiddin data so can't access outside class
     -> it works on implementation
"""


class sai:
    def __init__(self, n, color, age):
        self.number_of_legs = n
        self._color = color
        self.__age = age

    def rsk(self):
        print(f"I have {self.number_of_legs} legs, I'm {self._color} in color, and I'm {self.__age} years old.")

class kiran(sai):
    def rsk(self):
        print(f"I have {self.number_of_legs} legs, I'm {self._color} in color,")
        # {self.__age} is private only that class can access




resultmain = sai(2,"white",24)
resultmain.rsk()   # output: I have 2 legs, I'm white in color,
result = kiran(2, "white", 23)
result.rsk()  # Output: I have 2 legs, I'm white in color, and I'm 23 years old.
print(resultmain.number_of_legs)
print(resultmain._color)
#print(resultmain.__age) # it will get error because it is an private
print(dir(resultmain))

