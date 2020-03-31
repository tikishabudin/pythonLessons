name,age = 'Tiki',47
print("My name is " + name + ", and I am " + str(age) + " years old")
print(f"My name is {name}, and I am {age} years old")
print("My name is {1}, and I am {0} years old".format(name,age))

print("-"*20)

import math

PI = math.pi
print(PI)
print(f"PI: {PI:.4f}")
print("PI: {0:8.4f}".format(PI))

print("-"*20)

members = {
    'my':{'name':'Malaysia','population':'30m'}
    ,'fi':{'name':'Finland','population':'5.5m'}
}

for country in members.keys():
    print("{0} has a population of {1} people".format(members[country]['name'],members[country]['population']))

print("-"*20)

userInput = input("Please enter something: ")
print(f'You entered: {userInput}')

print("FILE I/O",end='\t')
print("-"*20)

# fileObj = open('sample.tikiisthecoolest','w')
# fileObj.write('The quick brown fox jumps over the lazy dog\n')
# fileObj.close()

# fileObj = open('sample.tikiisthecoolest','r')
# print(f"Retrieved from file: {fileObj.read()}")
# print(fileObj.readlines())
# fileObj.close()

with open('data.sample','w') as thefile:
    thefile.write("Some sample data")

# if thefile.closed():
#     print("closed")

import json
person = {'name':'Whatever'}
personFile = 'personData.json'

personString = json.dumps(person)
# json.dump(person,file)

# with open(personFile,'w') as fileWriter:
#     fileWriter.write(personString)

with open(personFile,'r') as fileReader:
    result = json.loads(fileReader.readline())
    print(result['name'])

# result = json.load(file)