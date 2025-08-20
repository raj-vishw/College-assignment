a = int(input("Enter first side:"))
b = int(input("Enter second side;"))
c = int(input("Enter third side:"))

if ( a == b == c):
    print("It is equilateral triangle")
elif ( a==b or b==c or c == a ):
    print("It is iscosceles triangle")
else :
    print("It is scelene")
