# #always start the class name with capital letter
# class Robot:
#     new_var= "this is token"
# robot = Robot()
# print(Robot.new_var)

# #constructor

# class Fruit:
#     def __init__(self,name:str,price:int):
#         self.name = name
#         self.price = price

#     def __str__(self) -> str:
#         return f"this fruit is {self.name} and price is {self.price}"
# #function
#     def getFruitValue(self):
#         return "this is fruit value function"

# fruit = Fruit("apple",410)

# fruit1 = Fruit("apple",210)
# #function call
# print(fruit.getFruitValue())
# #print(fruit1)

#inherentance
# class Music:
#     def playMusic():
#         return "music has been started"

# class Guitar(Music):
#     def guitarMusic():
#         return "Jhing Jhing Jhak"

# guitar= Guitar()
# print(Guitar.playMusic())
# print(Guitar.guitarMusic())

# # static Method
# class StaticExample:
#     @staticmethod
#     def guitarMusic():
#         return "jhing jhing" 

# print(StaticExample.guitarMusic())

#encapulation
class EncapulationClass:
    def __init__(self,name,age):
        self.name = name
        self._age = age  #protected
    def get_age(self):
        return self._age
    def set_age(self,age):
        if age>0:
            self._age = age

my_entry = EncapulationClass('Hari',23)
print(f"Name: {my_entry.name}")
#print(f"age: {my_entry.age}") #invalid
print(f"age: {my_entry.get_age()}")
