import math

y =int (input("Enter year between 1900 and 2099:"))

a = y%4
b = y%7
c = y%19
d =(19*c+15)%30
e =(2*a+4*b-d+34)%7

month = math.floor(((d+e+114)/31))
day = ((d+e+114)%31)+1

Day = day+13
Month = month

## Orthodox Easter in the Gregorian calendar is in March, April or May.

if (Day>31 and month==3):
    Day -= 31
    Month = month+1
elif (Day>30 and month==4):
    Day -= 30
    Month = month+1

print("Day: ", Day, " Month: ", Month)

     
