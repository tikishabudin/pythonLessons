def myFx():
    print("This is my function")

def myFx2(dog, dog2, param3):
    print("This is the dog: ", dog)
    print("This is the other dog: ", dog2)
    print("I'm not even sure what this is: ", param3)
    print("-"*20)

def myFx3(param1 = "Something", param2 = "Hahahaha", param3 = 42):
    print("This is param1: ", param1)
    if(param2 == None):
        print("Param 2 does not have a value")
    else:
        print("Param 2 is : ", param2)
    print("Param 3:", param3)
    print("-"*20)

myFx3(23)
myFx3("Tiki", 123)
myFx3(1,2,3)
myFx3("Allu", param3="Good boy!")
myFx3(param3=567890)

def myFx4(param1,param3,param2=None):
    print("P1:", param1)
    print("P2:",param2)
    print("P3:",param3)
    print("-"*20)

myFx4(param3=10,param1=10)

def myFx5(x,y):
    return x**y

result = myFx5(2,63)
print(result)