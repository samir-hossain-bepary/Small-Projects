#BMI Tracker with History

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_status(bmi):
    if bmi < 18.5:
        return"Under Weight"
    elif bmi <25:
        return "Normal"
    elif bmi < 30:
        return "Over Weight"
    else:
        return "Obese"

name = input("Name:")
weight= float(input("Weight (kg): "))
height= float(input("Height (m): "))

bmi = calculate_bmi(weight,height)
status = get_status(bmi)

with open("bmi_records.txt", "a") as file:
    file.write(f"{name} . BMI: {bmi},Status:{status}\n")

print(f"{name},Your BMI is{bmi} ({status})")