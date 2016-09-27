input_number = input("Enter number of pronic numbers: ")

for n in range (1,int (input_number)+1):
    x = n*(n+1)
    print(x, end=" ")
    n+=1
