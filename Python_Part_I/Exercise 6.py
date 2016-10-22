
for i in range (1,4):
    n = input("Enter number of triangle numbers: ")
    

    for n in range (1,int (n)+1):
        x = int (n)* (int (n)+1)/2
        print(int (x), end=" ")
        
        n+=1
    print(" ")
    i+=1
