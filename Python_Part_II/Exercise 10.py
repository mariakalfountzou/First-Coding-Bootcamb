input_A = input("Enter binary sequence:")

input_A.split()
list=[eval(x) for x in input_A]

invalid_sequence=0
for i in range(0,len(list)):
    if list[i]!=0 and list[i]!=1:
        print("This is not binary sequence!")
        invalid_sequence=1
        break

if invalid_sequence==0:
    counter=1
    counter_max=1
    digit_0=0
    digit_1=0
    for i in range (1,len(list)):
        if list[i] == list[i-1]:
            counter += 1
            if counter>counter_max :
                counter_max=counter
                if list[i]  ==0:
                    digit_0=1
                    digit_1=0
                else:
                    digit_0=0
                    digit_1=1
            elif counter==counter_max:
                if list[i]==0:
                    digit_0 = 1
                else:
                    digit_1=1
        else:
            counter = 1

    if digit_0==1 and digit_1==1:
        print("Equal longest run of ones and zeros with length:",counter_max) 
    elif digit_0==1:
        print("Longest run was zeros with length:",counter_max)
    elif digit_1==1:
        print("Longest run was ones with length:",counter_max)
    else:
        print("Zeros and ones come one after the other !")
