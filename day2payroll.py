#Calculate gross,tax,nett values based on number of hours worked
# basic pay = 15.00
# OT rate = 1.5
# OT is calculated ONLY after 40 hours
# Tax rate = 18%

hours = 10 # only 5 hours is overtime
otrate = 1.5
taxrate = 0.18
basic = 15
reghours = 40
gross,tax,nett = 0,0,0

if(hours > reghours):
    gross = ((hours - reghours) * otrate * basic) + (reghours * basic)
else:
    gross = hours * basic

tax = gross * taxrate
nett = gross - tax

print("Gross:\t\t " + str(gross))
print("(-)Tax:\t\t ", tax)
print("Nett:\t\t ", nett)