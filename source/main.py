from bmi_api import calculateBMI, printBMI, getWeightInPounds, getHeightInInches
from retirement_api import getAge, getGoal, getPercentSaved, getSalary, printRetirementPlan, calculateAgeWhenMet, calculateSavingsPerYear, calulateYearsUntilGoal

def main():
    print("Hello!")
    print("To calculate BMI enter 1")
    print("To calualte retirement goals enter 2")
    print("To stop the program enter 0")
    choice = int(input("Enter your choice: "))
    print("\n")

    if choice == 1:
        bmiProgram()
    elif choice == 2:
        retirementProgram()
    elif choice == 0:   
        print("Stopping the program gracefully.")
    
    print("Goodbye.")
    return
    
def bmiProgram():   
    height = getHeightInInches()
    while(height == -1):
        print("Not a valid height.")
        height = getHeightInInches()
    
    weight = getWeightInPounds()
    while(weight == -1):
        print("Not a valid weight.")
        weight = getWeightInPounds()

    bmi = calculateBMI(height, weight)
    printStatement = printBMI(bmi)
    print(printStatement)
    return

def retirementProgram():
    age = getAge()
    while(age == -1):
        print("Not a valid age.")
        age = getAge()

    salary = getSalary()
    while(salary == -1):
        print("Not a valid salary.")
        salary = getSalary()


    percentSaved = getPercentSaved()
    while(percentSaved == -1):
        print("Not a valid percent saved.")
        percentSaved = getPercentSaved()
    
    goal = getGoal()
    while(goal == -1):
        print("Not a valid goal.")
        goal = getGoal()

    

    savingsPerYear = calculateSavingsPerYear(salary, percentSaved)
    yearsUntilGoal = calulateYearsUntilGoal(goal, savingsPerYear)
    ageWhenMet = calculateAgeWhenMet(age, yearsUntilGoal)
    printStatement = printRetirementPlan(ageWhenMet)
    print(printStatement)


main()