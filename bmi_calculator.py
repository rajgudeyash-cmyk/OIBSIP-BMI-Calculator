print("==============================")
print("       BMI CALCULATOR")
print("==============================")

try:
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))

    if weight <= 0 or height <= 0:
        print("Error: Values must be positive!")

    else:
        bmi = weight / (height * height)

        print("\nYour BMI:", round(bmi, 2))

        if bmi < 18.5:
            category = "Underweight"

        elif bmi < 25:
            category = "Normal"

        elif bmi < 30:
            category = "Overweight"

        else:
            category = "Obese"

        print("Category:", category)

except ValueError:
    print("Error: Please enter numbers only!")

print("==============================")
print("Thank you for using BMI Calculator!")