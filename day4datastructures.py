#Lists
myList = ['Tiki','Lorenzo','Miklas','Maria']
myList2 = list({'Durong','Victor'})

myList.insert(2,"Giovanni")
myList.remove('Tiki')
del myList[0]

for name in myList2:
    myList.append(name)

myList.clear()

print(myList)
print("-"*20)

#Sets
mySet = {'Apples','Bananas','Appelsiini','Karpalo'}
mySet2 = set(['Omena','Sitruuna','Apples','Grapes'])

mySet.add('Apples')
mySet.discard("Bananas")
#del mySet[0]
mySet.clear()

intersectedSet = mySet.intersection(mySet2)
joinedSets = mySet.union(mySet2)

# orderedList = list(mySet)

# print(mySet)
print(intersectedSet)
print(joinedSets)
print("-"*20)

#Tuple
myTuple = ('one','two','three')
myTuple2 = tuple([1,2,3])
# myTuple[0] = 'Something' can't be done

first,second,third = myTuple

print(second)
print("-"*20)

#Dictionary
myDictionary = {'my':'Malaysia','fi':'Finland','it':'Italy','vn':'Vietnam','ru':'Russia'}
myDictionary2 = dict()

myDictionary2['in'] = "India"
myDictionary['fi'] = "Suomi"

for code in myDictionary.values():
    print(code)

del myDictionary2['in']

print(myDictionary2.get('in',"No such country"))
print("-"*20)

students = {
    'victor':{'name':'Victor Wan','id':'12345','country':'Malaysia'}
    ,'durong':{'name':'Durong','id':'34567','country':'Vietname','hobbies':['Skating','Hacking Pentagon Servers']}
    }

print(students['victor']['name'])

fruitGroups = [{'tropical':{'Bananas','Durians','Mangosteens'}},{'mediterranean':{'Pomegranates','Grapes'}}]

print(fruitGroups[0])

