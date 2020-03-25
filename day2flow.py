#if statements

#x = 5, y = 11
x,y = 5,11

# if(x == y)
# {
#     //sadfasdf
# }
# else
# {

# }

# Relational
# ==,!=,<,<=,>,>=

# Logical
# and
# or
# ! Not


if(x!=y and (x < 3 or y == 11)):
    print('TRUE')
else:
    print('FALSE')

# if(x == y):
#     pass
#     # print('TRUE')
#     # print('Something else to do')
# elif(x >= 10):
#     print("wow")
# elif(y <= 100):
#     print("Meh!")
# else:
#     print('FALSE')
#     print('Nothing to do')



print("The end")

print("-" *50)

counter = 0
while(counter < 5):
    print("Moi")
    counter += 1
    if(counter == 3):
        break #continue
    print("Hei hei")

print("-" * 50)

numbers = [10,20,30,40,50]

for number in numbers:
    print(number)