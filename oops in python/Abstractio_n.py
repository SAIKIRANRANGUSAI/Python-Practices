"""
    Abstraction:  abstraction is the process of hiding the implementaion deteils from user.
    -> Abstraion is actually finding which functionality is hidden from the user
       and which is shown to user (allowing them to focus on the essential features rather than the internal)
    -> It works in design phase
    -> abstracion methods are usefull blueprints that ensure that we don't forget to implement methods
        from a class and they are usefull because they really help us to stay comsistence.
    -> we should import abc and abstractmethos and in class inherate abc
    -> In function use decorator like @abstractmethod
By using abstraction, developers can create clear and consistent interfaces,
 making it easier for users to understand and interact with the system

"""
from abc import ABC,abstractmethod
class main(ABC):
    def __init__(self,n):
        self.no_of_tyres = n

    @abstractmethod
    def tyres(self):
        pass
    def display(self):
        print("im' calling from main class ")
class bike(main):
    def __init__(self,n,color,gares):
        super().__init__(n)
        self.color = color
        self.gares = gares
    def tyres(self):
        print(f"i have only {self.no_of_tyres}")
    def display(self):
        print("only two members can travell by me")
    def gare_s(self):
        print(f"i have {self.gares}")
class car(main):
    def __init__(self,n,color,gares,model):
        super().__init__(n)
        self.color = color
        self.gares = gares
        self.model_year = model
    def tyres(self):
        print(f"i have only {self.no_of_tyres}")
    def display(self):
        print("only two members can travell by me")
    def gare_s(self):
        print(f"i have {self.gares}")
    def mode_l(self):
        print(f"made in  {self.model_year}")
    def colors(self):
        print(f"{self.color} in color")
sai = bike(2,"black",5)
kiran = car(4,"white",6,2025)
sai.display()
sai.tyres()
sai.gare_s()
kiran.display()
kiran.tyres()
kiran.model_year
kiran.gare_s()
kiran.colors()