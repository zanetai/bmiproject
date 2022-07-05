def GetWeight():
    while True:
        try:
            weight = int(input("What is your weight - kg?: "))
            if weight <= 0:
                print("Your weight can't be 0 or less!")
                continue
        except ValueError:
            print("You have to type a number!")
            continue
        else:
            return weight

def GetHeight():
    while True:
        try:
            height = float(input("what is your height - m?: "))
            if height <= 0:
                print("Your height can't be 0 or less!")
                continue
        except ValueError:
            print("You have to type a number!")
            continue
        else:
            return height

def GetBMI():
    weight = GetWeight()
    height = GetHeight()
              
    bmi = round(weight / (height**2), 1)
    return bmi


def CountBMI():
    bmi = GetBMI()

    if bmi < 18.5:
        result = "underweight"

    elif bmi >= 18.5 and bmi < 25:
        result = "normal"

    elif bmi >= 25:
        result = "overweight"

    print(f"Your BMI is {bmi} and this is considered {result}.")


CountBMI()
