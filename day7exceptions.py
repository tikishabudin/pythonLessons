if True: print('lalala')

try:
    x = int(input("Enter a value for x: "))
    y = int(input("Enter a value for y: "))

    print(x//y)

    # with open('Somefile.dat','r') as thefile:
    #     thefile.write('djkfhaskdjf')

except(ZeroDivisionError) as err:
    print("Can't divide by zero")
    print(err.args)
    try:
        raise ValueError(('slkdjhfaskljfhslk'))
    except(ValueError) as err:
        print(err)
except(ValueError,OSError):
    print("Must be a number")
except:
    print("Something went wrong")
finally:
    print("This is the end of the error handling process")