import math

input_a=input("Give me the first side of the triangle:")
input_b=input("Give me the second side of the triangle:")
input_c=input("Give me the third side of the triangle:")

r= (float(input_a)+ float (input_b)+ float (input_c))*(-float (input_a)+ float (input_b)+ float (input_c))*(float (input_a)- float (input_b)+ float (input_c))*( float (input_a)+ float (input_b)- float (input_c))
A= (1/4)* math.sqrt(r)
print("The triangle's area is:", A)
