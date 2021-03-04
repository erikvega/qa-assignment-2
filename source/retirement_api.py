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
        return "You would be " + str(ageWhenMet) + " by the time you meet your savings goal. Savings goal not met."

def getAge():
    try: 
        age = int(input("Please enter your age in years: "))
    except ValueError:
        return - 1
    except TypeError:
        return -1 
    else: 
        if age and 100 > age > -1:
            return age
        else:
            return -1

def getSalary():
    try: 
        salary = int(input("Enter your salary in dollar amount (no cents and no commas): "))
    except ValueError:
        return - 1
    except TypeError:
        return -1 
    else: 
        if salary and 500001 > salary > 0:
            return salary
        else:
            return -1 

def getPercentSaved():
    try: 
        percentSaved = int(input("Enter the percent you save from your salary every year (0 - 100): "))
    except ValueError:
        return - 1
    except TypeError:
        return -1 
    else: 
        if percentSaved and 101 > percentSaved > -1:
            return percentSaved / 100
        else:
            return -1

def getGoal():
    try: 
        goal = int(input("Enter the amount you'd like to have saved up for retirement (no cents and no commas): "))
    except ValueError:
        return - 1
    except TypeError:
        return -1 
    else: 
        if goal and goal > 0:
            return goal
        else:
            return -1 