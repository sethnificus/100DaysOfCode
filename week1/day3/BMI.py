#This is copied code
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#This is my code

bmi = weight / height


if bmi <= 18.5:
    print("You are underweight")
elif (bmi >= 18.5) and (bmi <= 25.0):
    print("you are perfect weight!")
elif (bmi > 25) and (bmi <= 35):
    print("you are almost obese!")
elif bmi > 35:
    print("you are obese!")