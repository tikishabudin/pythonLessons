'''
Enter hours: 12
Gross:
Tax:
Nett:
Another calculation? Y/N
[If N -> Write last value to a file (HTML)]
'''

hours = 0
otrate = 1.5
taxrate = 0.18
basic = 15
reghours = 40
gross,tax,nett = 0,0,0
quit = False
userInput = None

while(quit != True):
    hours = float(input("Enter hours worked:"))
    if(hours > reghours):
        gross = ((hours - reghours) * otrate * basic) + (reghours * basic)
    else:
        gross = hours * basic

    tax = gross * taxrate
    nett = gross - tax

    print(f"Gross:\t\t {gross:7.2f}")
    print(f"(-)Tax:\t\t {tax:7.2f}")
    print(f"Nett:\t\t {nett:7.2f}")
    print()
    userInput = input("Another calculation? Y/N")
    if (userInput == 'Y' or userInput == 'y'):
        quit = False
    elif (userInput == 'N' or userInput == 'n'):
        quit = True
        with open('result.html','w') as resultWriter:
            resultStr = '''
            <html>
                <head>
                </head>
                <body>
                    <h1>Your Salary Info</h1>
                    <div>Gross: {0:.2f}</div>
                    <div>Gross: {1:.2f}</div>
                    <div>Gross: {2:.2f}</div>
                </body>
            </html>
            '''.format(gross,tax,nett)
            resultWriter.write(resultStr)
    else:
        print("Invalid entry. Resuming program")