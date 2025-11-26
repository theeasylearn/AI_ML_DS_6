'''
    write a program to findout & display person obesity level using B.M.I(body to mass index) technique.
    ---------------------------------------------------------------------
    formula to calculate BMI IS 
    B.M.I. = weight(Kg) / (height_in_meter * height_in_meter)
    obesity level 
        Underweight: BMI less than 18.5
        Normal: BMI between 18.5 to 24.9
        Overweight: BMI between 25.0  29.9
        Obese: BMI between 30.0  34.9
        Extremely Obese: BMI 35.0 and above
    input:
        weight, foot, inch 
    steps 
    1   accept input weight, foot, inch
    2   convert foot and inches into meter 
    3   calculate BMI 
    4   display person obesity level
'''
weight = float(input("Enter your weight in KG"))
print("Enter your height in foot and inches")
foot = int(input("Enter only foot"))
inches = int(input("Enter only inches"))

#calcuate total inches 
total_inch = (foot * 12) + inches
meter = total_inch / 39.37
bmi = weight / (meter * meter)
print(f"bmi = {bmi}")
if bmi>35:
    print("Person is extremely obese")
elif bmi>30:
    print("Person is obese")
elif bmi>25:
    print("Person is overweight")
elif bmi>18.5:
    print("Person is normal")
else:
    print("person is underweight")

print("thank you")