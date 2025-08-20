weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Classification: Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Classification: Normal weight")
elif 25.0 <= bmi <= 29.9:
    print("Classification: Overweight")
else:
    print("Classification: Obese")
