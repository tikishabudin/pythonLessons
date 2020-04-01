def somethingElse():
    pass

class Base:
    """This is the Base class to rule all classes"""
    someVar = "Some shared value"

    def __init__(self,id='',desc='No Description'):
        print("Base class init fx")
        self.id = id
        self.address = ''
        self.description = desc
        self.data = dict()

    def doSomething(self,someValue):
        """This is the do something function\n
        input: someValue [Should be a string]\n
        output: Garbage print of lalalala
        """
        self.somethingElse()
        return f"Doing something with {someValue} from {self.id}"

    def somethingElse(self):
        print("Lalalala")

    def __str__(self):
        return f"This is Base object id: {self.id}"

class Child(Base):

    def __init__(self):
        super().__init__("whatever","something")
        print("Child class init fx")

    def advFx(self):
        return "This is an added functionality"

class OtherChild(Base):
    pass

class Person:
    name = ""
    age = 0
    id = ''

from tikiClass import Tiki

Tiki().stayAtHome()

# miklasObj = Child()
# # miklasObj.doSomething('child stuff')
# print(miklasObj.advFx())

# tikiObj = Base(desc='Whatever',id='tiki123')

# lorenzoObj = Base("lorenzo23","Lorenzo is suave")

# print(tikiObj.doSomething(42))

# print(tikiObj)

# print(tikiObj.someVar)
# tikiObj.someVar = "Dangit! Tiki changed the value"
# print(tikiObj.someVar)

# print(lorenzoObj.someVar)


# print(tikiObj.id)
# print(tikiObj.description)
# print(lorenzoObj.id)