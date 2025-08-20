age = int(input("Enter your age: "))

if age <= 12:
    category = "Child"
elif age <= 19:
    category = "Teenager"
elif age <= 59:
    category = "Adult"
else:
    category = "Senior Citizen"

print(f"You are classified as: {category}")
