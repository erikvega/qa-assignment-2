def calculateBMI(height, weight):
    weight = convertToKilos(weight)
    height = convertToMeters(height)

    bmi = round((weight / (height * height)), 1)

    return bmi


def printBMI(bmi):
    if bmi < 18.5:
        return "With a BMI of " + str(bmi) + " you are underweight.\n"
    elif bmi >= 18.5 and bmi < 25:
        return "With a BMI of " + str(bmi) + " your weight is normal.\n"
    else:
        return "With a BMI of " + str(bmi) + " you are overweight.\n"


def convertToKilos(weight):
    return weight * 0.45



def convertToMeters(height):
    return height * 0.025


def getWeightInPounds():
    weight = int(input("Please enter your weight in pounds: "))
    
    if weight and weight > 0:
        return weight
    else:
        return -1

def getHeightInInches():
    height = int(input("Please enter your height in INCHES ONLY (ex. 5 foot 7 inches = 67 inches): "))

    if height and height > 0:
        return height
    else:
        return -1