year = int(input("Enter year to check leap or not:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is leap year")
else :
    print(f"{year} is not leap year")
