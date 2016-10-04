import math

datea = input("Enter first date using format (dd/mm/yyyy):")
s1=datea.split('/')
print(s1[:])
d1 = eval(s1[0])
m1 = eval(s1[1])
y1 = eval(s1[2])
c1 = 365*y1+ math.floor(y1/4)- math.floor(y1/100)+ math.floor(y1/400)+ math.floor((306*m1+5)/10)+(d1-1)

dateb = input("Enter second date using format (dd/mm/yyyy):")
s2=dateb.split('/')
print(s2[:])
d2 = eval(s2[0])
m2 = eval(s2[1])
y2 = eval(s2[2])
c2 = 365*y2+ math.floor(y2/4)- math.floor(y2/100)+ math.floor(y2/400)+ math.floor((306*m2+5)/10)+(d2-1)

c = abs(c1-c2)
print(c, " days")
