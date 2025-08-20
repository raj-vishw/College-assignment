n = int(input("Enter a number:"))

if (n % 11 == 0) and (n % 13 == 0):
    print(f"{n} is divisible by both 11 and 13")
else:
    print(f"{n} is not divisible by both 11 and 13")
