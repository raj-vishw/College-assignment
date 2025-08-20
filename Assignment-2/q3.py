a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if (a>b) and (a>c):
    print(f"{a} is biggest")
elif(b>a) and (b>c):
    print(f"{b} is biggest")
else :
    print(f"{c} is biggest")
