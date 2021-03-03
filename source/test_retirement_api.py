import unittest
from retirement_api import calculateSavingsPerYear, calulateYearsUntilGoal, calculateAgeWhenMet, printRetirementPlan, getAge, getGoal, getPercentSaved, getSalary

class retirementCalculationTest(unittest.TestCase): 
    def testSavingPerYear(self):
        salary = 65000
        percentSaved = 0.1
        savingPerYear = calculateSavingsPerYear(salary, percentSaved)
        self.assertEqual(savingPerYear, 8775)

    def testYearsUntilGoalMet(self):
        goal = 1500000
        savingsPerYear = 65000
        yearsUntilGoal = calulateYearsUntilGoal(goal, savingsPerYear)
        self.assertEqual(yearsUntilGoal, 171)

    def testAgeWhenMet(self):
        age = 25
        yearsUntilGoal = 171
        ageWhenMet = calculateAgeWhenMet(age, yearsUntilGoal)
        self.assertEqual(ageWhenMet, 196)


class retirementPrintTest(unittest.TestCase):
    def testPrintRetirmentPlanOver100(self):
        ageWhenMet = 100
        result = printRetirementPlan(ageWhenMet) 
        self.assertEqual(result, "Savings goal not met.")
    
    def testPrintRetirmentPlanValid(self):
        ageWhenMet = 80 
        result = printRetirementPlan(ageWhenMet)
        self.assertEqual(result, "You will be 80 years old when you meet your goal.")

class retirementUserInputTest(unittest.TestCase):
    def test_bad_age(self):
        result = getAge()
        self.assertEqual(result, -1)

    def test_bad_salary(self):
        result = getSalary()
        self.assertEqual(result, -1)

    def test_base_percentSaved(self):
        result = getPercentSaved()
        self.assertEqual(result, -1)

    def test_bad_goal(self):
        result = getGoal()
        self.assertEqual(result, -1)

