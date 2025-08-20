a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
d = int(input("Enter d:"))
m = int(input("Enter m:"))
n = int(input("Enter n:"))

print("The first equation is:")
print(f"{a}x1 + {b}x2 = {m} ")

print("The second equation is:")
print(f"{c}x1 + {d}x4 = {n}")

if ((a*d) - (c*b) == 0) :
    print("There is no solution ")
else :
    x1 = ((m*d)-(b*n))/((a*d)-(c*d))
    x2 = ((n*a)-(m*c))/((a*d)-(c*b))
    print("The solution is:")
    print(f"X1={x1}")
    print(f"X2={x2}")
