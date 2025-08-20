a = int(input("Enter a:"))
b = int(input("Enter b:"))

print("Enter +, -, *, /")
c = input()

if ( c == '+'):
    print("The result:",a+b)
elif (c == '-'):
    print("The result:",a-b)
elif ( c == '*'):
    print("The result:",a*b)
elif ( c == '/'):
    print("The result:",a/b)
else :
    print("Enter a valid choice")
