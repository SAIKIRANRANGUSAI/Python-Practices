"""
    Method Overriding:
  -> It's a form of runtime polymorphism.
  -> Methods should have the same name and parameters (order and type).
  -> Must involve two classes: a superclass and a subclass,
    where the method in the subclass overrides the method with the same signature in the superclass.

"""
class father():
    def sleep(self):
        print("father sleep at 9 pm")
    def eat(self):
        print("eats vegitables")
class son(father):
    def sleep(self):
        print("son sleep's at 11pm")

    def eat(self):
        print("non veg")

sai = father()
kiran = son()
sai.sleep()
sai.eat()
kiran.sleep()
kiran.eat()