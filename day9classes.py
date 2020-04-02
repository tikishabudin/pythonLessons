class Sample:
    def someFx(self):
        print("Sample class someFx")

    __someFx = someFx

class Other(Sample):
    def someFx(self):
        print("Other class someFx")

otherObj = Other()
otherObj.someFx()
otherObj._Sample__someFx()

print("-"*20)

class Looppy:
    def __init__(self,receivedData=[]):
        self.data = receivedData
        self.index = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

loopObj = Looppy([1,2,3,4,5,6])

for num in loopObj:
    print(num)

print("-"*20)

numList = [0,1]
compList = range(0,1)

# for num in compList:
#     numList.append(num)

print(numList)
print(list(compList))

import sys
from random import randint

print(f"The size of numList is {sys.getsizeof(numList)} bytes")
print(f"The size of compList is {sys.getsizeof(compList)} bytes")



def digitGenerator(numDigit=1):
    for digit in range(0,numDigit):
        yield randint(0,9)

testGen = digitGenerator(5000)

for num in digitGenerator(4):
    print(num,end='')

print(sys.getsizeof(testGen))