from math import ceil

def calculateSavingsPerYear(salary, percentSaved):
    return (salary * percentSaved) * 1.35

def calulateYearsUntilGoal(goal, savingsPerYear):
    years = goal/savingsPerYear
    return ceil(years)

def calculateAgeWhenMet(age, yearsUntilGoal):
    return age + yearsUntilGoal

def printRetirementPlan(ageWhenMet):
    if ageWhenMet < 100:
        return "You will be " + str(ageWhenMet) + " years old when you meet your goal."
    else:
        return "Savings goal not met."

def getAge():
    age = int(input("Please enter your age in years: "))

    if age and 100 > age > -1:
        return age
    else:
        return -1

def getSalary():
    salary = int(input("Enter your salary in dollar amount (no cents and no): "))

    if salary and 500001 > salary > 0:
        return salary
    else:
        return -1 

def getPercentSaved():
    percentSaved = int(input("Enter the percent you save from your salary every year (0 - 100): "))

    if percentSaved and 101 > percentSaved > -1:
        return percentSaved / 100
    else:
        return -1

def getGoal():
    goal = int(input("Enter the amount you'd like to have saved up for retirement (no cents and no commas): "))

    if goal and goal > 0:
        return goal
    else:
        return -1 
