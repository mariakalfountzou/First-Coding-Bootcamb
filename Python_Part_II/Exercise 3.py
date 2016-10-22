input_number =input("Enter 10 digit number:")
input_number.split()
list=[eval(x) for x in input_number] #eval converts input_number to numbers

if len(list)!=10:
    print("This is not 10 digit number!\nPlease enter 10 digit number:")

for i in range(0,10):
    if i%2==0:
        print(list[i], end=" ")
print()
print(end=" ")

for i in range(0,11):
    if i%2!=0:
        print(list[i], end=" ")      
       
