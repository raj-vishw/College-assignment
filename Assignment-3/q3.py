n = int(input("Enter number:"))

s = 1

for i in range(1,n+1):
    s = (n ** i) + s

print(s)
