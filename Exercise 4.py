import math

a = input("Enter the value for a, not 0!:")
b = input("Enter the value for b:")
c = input("Enter the value for c:")

d= (float(b)**2-4*float (a)* float (c))

if (float (d) >=0):
    x1= (-float(b)+math.sqrt(d)) / (2*float (a))                           
    x2= (-float(b)- math.sqrt(d)) / (2*float (a))
    if (x1==x2):
        print("The equation has a double solution: ", x1)
    else:
        print("The first solution is:", x1)
        print("The second solution is:", x2)  
  
  
else:
    print("This equation has no real-valued solutions.")
    
