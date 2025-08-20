n = int(input("Enter a number:"))

s=0

while n > 0:
    temp = n % 10
    s = s + temp
    n = n / 10

print(f"Sum:{int(s)}")

