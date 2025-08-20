a = int(input("Enter first subject marks: "))
b = int(input("Enter second subject marks: "))
c = int(input("Enter third subject marks: "))

avg = (a + b + c) / 3

if avg >= 90:
    print("Grade A")
elif avg >= 80:
    print("Grade B")
elif avg >= 70:
    print("Grade C")
elif avg >= 60:
    print("Grade D")
else:
    print("Grade F")
