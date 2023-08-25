import csv 
import os
from abc import ABC, abstractmethod

os.chdir("S:\college\programming\python\projects\intro")

class pets:
    # class attribute: (global)
    cuteness_level = 100
    years = 10
    all_ = []

    def __init__(self, name, Type, age) -> None:
        # validation:
        assert name != None
        assert Type in ["cat", "dog", "bear","elephant"], "we only accept cats and dogs and bears"

        # instance attribute:
        self.__name = name # private attribute
        self.type = Type
        self.age = age

        pets.all_.append(self)

    def after_10_years(self):
        return self.age + pets.years

    def cuteness(self):
        return f"{self.cuteness_level}%"

    @classmethod
    def from_csv(cls):
        with open ("pets.csv", "r") as f:
            reader = csv.DictReader(f)
            pets = list(reader)

            for pet in pets:
                print(pet)

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        
    @property
    #It allows you to access the method like an attribute, without using parentheses to invoke it as a function.
    def name(self): #this makes name a read only attribute #this is the getter method
        # we can write code here
        return self.__name    

    @name.setter
    def name(self , value): #the setter method
        # we can write code here
        if len(value) >= 6:
            raise Exception ("name is too long")  # or raise ValueError  
        else:
            self.__name = value

    # Magic Method:
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}( {self.name} , {self.type} , {self.age})"

    def __connect(self , smtp_server):
        pass

    def __body(self):
        return 'hi dude'
    
    def __send(self):
        pass

    def send_email(self):
        self.__connect('aa')
        self.__body()
        self.__send()

    def add(self,a, b ,c=0):#by setting a defult value to the 3rd parameters i could send 2 paramers or 3
        return a+b+c



pet1 = pets("john","cat",4)
pet2 = pets("lola","bear",2)
pet3 = pets("andreia","dog",8)

print(pets.cuteness_level)  # accessing class attributes
print(pet1.cuteness_level)
# print(pet2.__dict__) #all the instance attributes
# print(pets.__dict__) #all the class attributes
# __dict__ is called magic attribute

print(pet1.after_10_years())

pet1.cuteness_level = 70
print(pet1.cuteness())
print(pet2.cuteness())
print(pets.all_)

for instances in pets.all_:
    print(instances.name)

pets.from_csv()    


class elephant(pets):
    all = []
    def __init__(self, name, Type , age, length) -> None:
        #using super method to have access to all methods and attributes without writing them again:
        super().__init__(
            name, Type, age
        )
        
        self.length = length

        pets.all_.append(self)

ele = elephant('momo', 'elephant' , 3 , 4)
print(ele.all_)


class animal(ABC):
    @abstractmethod
    def walk(self):
        pass

class cat(animal):
    def walk(self):
        return 'walking'    
    
soso = cat()
print(soso.walk())    