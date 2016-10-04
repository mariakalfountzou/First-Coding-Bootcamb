import math

upper_limitA = input("Enter limit:")

upper_limit = eval(upper_limitA)

power_index = 0
power = 1

while power <= (upper_limit/2):
    power_index+=1
    power = power*2

list=[]
for i in range(3,upper_limit+1):
    list.append(i)


for i in range(power_index,1,-1):
    list.remove(int (math.pow(2,i)))

length = len(list)
for i in range (0,length+1,10):
    print (list[i:i+10])

