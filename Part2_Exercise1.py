TIN =input("Enter Tax Identification Number:")
TIN.split()
list=[eval(x) for x in TIN] #eval converts TIN to numbers
x=list.pop(8) #remove the last digit

sum=0
for i in range(1,9):
    sum= sum+list[-i]*(2**i)

remainder=sum%11
mod=remainder%10
    
if (mod==x):
    print("Tax Identification Number valid.")
else:
    print("Tax Identification Number not valid.")
