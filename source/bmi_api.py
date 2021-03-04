def calculateBMI(height, weight):
    weight = convertToKilos(weight)
    height = convertToMeters(height)

    bmi = round((weight / (height * height)), 1)

    return bmi


def printBMI(bmi):
    if bmi < 18.5:
        return "With a BMI of " + str(bmi) + " you are underweight."
    elif bmi >= 18.5 and bmi < 25:
        return "With a BMI of " + str(bmi) + " your weight is normal."
    elif bmi >= 25 and bmi < 30:
        return "With a BMI of " + str(bmi) + " you are overweight."
    else:
        return "With a BMI of " + str(bmi) + " you are obese."


def convertToKilos(weight):
    return weight * 0.45



def convertToMeters(height):
    return height * 0.025


def getWeightInPounds():
    try: 
        weight = int(input("Please enter your weight in pounds: "))
    except TypeError:
        return - 1
    except ValueError:
        return -1 
    else: 
        if weight and weight > 0:
            return weight
        else:
            return -1

def getHeightInInches():
    try: 
        height = int(input("Please enter your height in INCHES ONLY (ex. 5 foot 7 inches = 67 inches): "))
    except TypeError: 
        return -1
    except ValueError:
        return -1 
    else: 
        if height and height > 0:
            return height
        else:
            return -1