input_number_of_eurosA=input("Enter number of 50 euro banknotes: ")
sumA=int(input_number_of_eurosA)* 50

input_number_of_eurosB=input("Enter number of 20 euro banknotes: ")
sumB=int(input_number_of_eurosB)* 20

input_number_of_eurosC=input("Enter number of 10 euro banknotes: ")
sumC=int(input_number_of_eurosC)* 10

input_number_of_eurosE=input("Enter number of 5 euro banknotes: ")
sumE=int(input_number_of_eurosE)* 5

input_number_of_eurosF=input("Enter number of 2 euro coins: ")
sumF=int(input_number_of_eurosF)* 2

input_number_of_eurosG=input("Enter number of 1 euro coins: ")
sumG=int(input_number_of_eurosG)* 1

TotalSum=sumA+sumB+sumC+sumE+sumF+sumG

print("You have ", TotalSum, "euros.")
