input_number =input("Enter 9 digit number:")
input_number.split()
list=[eval(x) for x in input_number] #eval converts input_number to numbers

if len(list)!=9:
    print("This is not 9 digit number!\nPlease enter 9 digit number:")
   

for i in range(0,9):
    if i%3==0:
        print(list[i], end="  ")

print()
print(end=" ")
for i in range(0,9):
    if i%3==1:
        print(list[i], end="  ")      

print()
print(end="  ")
for i in range(0,9):
    if i%3==2:
        print(list[i], end="  ")      
       
