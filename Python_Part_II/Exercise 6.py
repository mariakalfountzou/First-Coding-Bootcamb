input_number = input("Enter 9 numbers in the form x xx xxx:")

input_number.split()
print(input_number)

for i in range(0,26,9):
    print("  ",input_number[i],"|", end=" ")
print()    
for i in range(2,26,9):
    print(" ",input_number[i:i+2],"|", end=" ")
print()    
for i in range(5,26,9):
    print("", input_number[i:i+3],"|",end=" ")


    
