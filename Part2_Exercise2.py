input_A = input("Enter an 8-bit binary number:")

input_A.split()
list=[eval(x) for x in input_A] #eval converts TIN to numbers

for i in range(0,7):
    if list[i]!=0 and list[i]!=1:
        print("This is not a binary number!")
        break;
    elif list.count(1)%2==0:
        print("Parity check OK.")
        break;
    else:
        print("Parity check not OK.")
        break;    
    
