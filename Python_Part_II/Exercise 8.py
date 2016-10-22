input_sequence = input("Enter number sequence:")
input_sequence.split()
list=[eval(x) for x in input_sequence] #eval converts input_number to numbers
l = len(list)
sum = 0
if l%2==0:
    for i in range(0,l,2):
        sum += list[i]*list[i+1]
else:
    x=list.pop()
    l = len(list)
    for i in range(0,l,2):
        sum += list[i]*list[i+1]
    sum += x

print(sum)
    
