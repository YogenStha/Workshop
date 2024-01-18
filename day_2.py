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
class Music:
    def playMusic():
        return "music has been started"

class Guitar(Music):
    def guitarMusic():
        return "Jhing Jhing Jhak"

guitar= Guitar()
print(Guitar.playMusic())
print(Guitar.guitarMusic())

# static Method
class StaticExample:
    @staticmethod
    def guitarMusic():
        return "jhing jhing" 

print(StaticExample.guitarMusic())
