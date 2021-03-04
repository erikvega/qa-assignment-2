import unittest
from retirement_api import calculateSavingsPerYear, calulateYearsUntilGoal, calculateAgeWhenMet, printRetirementPlan, getAge, getGoal, getPercentSaved, getSalary
from unittest.mock import patch

class retirementCalculationTest(unittest.TestCase): 
    def testSavingsPerYear(self):
        salary = 65000
        percentSaved = 0.1
        savingPerYear = calculateSavingsPerYear(salary, percentSaved)
        self.assertEqual(savingPerYear, 8775)

    def testYearsUntilGoalMet(self):
        goal = 1500000
        savingsPerYear = 8775
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
        self.assertEqual(result, "You would be 100 by the time you meet your savings goal. Savings goal not met.")
    
    def testPrintRetirmentPlanValid(self):
        ageWhenMet = 80 
        result = printRetirementPlan(ageWhenMet)
        self.assertEqual(result, "You will be 80 years old when you meet your goal.")

class retirementBadUserInputTest(unittest.TestCase):
    stringInput = "hey"
    zeroInput = 0
    ageBoundaries = [zeroInput, 100]
    salaryBoundaries = [zeroInput, 500001]
    percentageBoundaries = [-1, 101]
    noInput = " "

    @patch('builtins.input', side_effect=stringInput)
    def test_word_age(self, mock_input):
        result = getAge()
        self.assertEqual(result, -1)    
    
    @patch('builtins.input', side_effect=ageBoundaries[0])
    def test_zero_age(self, mock_input):
        result = getAge()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=ageBoundaries[1])
    def test_100_age(self, mock_input):
        result = getAge()
        self.assertEqual(result, -1)
    
    @patch('builtins.input', side_effect=noInput)
    def test_blank_age(self, mock_input):
        result = getAge()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=stringInput)
    def test_word_salary(self, mock_input):
        result = getSalary()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=salaryBoundaries[0])
    def test_zero_salary(self, mock_input):
        result = getSalary()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=salaryBoundaries[1])
    def test_over_max_salary(self, mock_input):
        result = getSalary()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=noInput)
    def test_blank_salary(self, mock_input):
        result = getSalary()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=stringInput)
    def test_word_percentSaved(self, mock_input):
        result = getPercentSaved()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=-percentageBoundaries[0])
    def test_negative_percentSaved(self, mock_input):
        result = getPercentSaved()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=-percentageBoundaries[1])
    def test_over_max_percentSaved(self, mock_input):
        result = getPercentSaved()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=noInput)
    def test_blank_percentSaved(self, mock_input):
        result = getPercentSaved()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=stringInput)
    def test_word_goal(self, mock_input):
        result = getGoal()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=zeroInput)
    def test_zero_goal(self, mock_input):
        result = getGoal()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=noInput)
    def test_blank_goal(self, mock_input):
        result = getGoal()
        self.assertEqual(result, -1)