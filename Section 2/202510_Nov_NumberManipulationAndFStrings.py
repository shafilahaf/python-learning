height = 154
weight = 63

bmi = weight / (height/100) ** 2
bmi_as_int = int(bmi)
bmi_rounded = round(bmi, 2)

print("Your BMI (integer) is " + str(bmi_as_int))
print(f"Your BMI (rounded) is {bmi_rounded}")

# F-string example
score = 85
height = 1.75
is_winning = True
print(f"Your score is {score}, your height is {height}, and you are winning: {is_winning}")