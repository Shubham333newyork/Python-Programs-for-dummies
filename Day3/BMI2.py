print("Welcome to BMI calculator")
height = input("What's your height in cm?")
weight = input("What's your weight in kg?")
bmi = int(weight) / float(height)**2
bmi = round(bmi)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, & you are underweight")
elif 18.5<= bmi < 25:
    print(f"Your bmi is {bmi}, & you are normal weight ")
elif 25<= bmi < 30:
    print(f"YOur bmi is {bmi}, & YOu are overweight. ")
elif 30<= bmi < 35:
    print(f"YOur bmi is {bmi} & you are obese. ")
else:
    print(f"Your bmi is {bmi}, & you are clinically obese. ")
