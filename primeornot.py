number = int(input("What number do you want to prime check? "))

for i in range (2,number-1):
    if number%i==0:
        primeFlag=False;
    else:
        primeFlag=True;
if primeFlag==True:
    print("Prime number")
else:
    print("Not prime")