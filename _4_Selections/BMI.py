weightInPounds = eval(input("Enter weight in pounds : "))
heightInInch = eval(input("Enter height in inch : "))

weightInKg = weightInPounds * 0.45359237
heightInMeters = heightInInch * 0.0254
bmi = (weightInKg / (heightInMeters * heightInMeters))

if bmi < 18.5:
    interpretation = "Underweight"
elif bmi < 24.5:
    interpretation = "Normal"
elif bmi < 29.9:
    interpretation = "Overweight"
else:
    interpretation = "Obese"

print("BMI is", format(bmi, ".2f"), interpretation)
