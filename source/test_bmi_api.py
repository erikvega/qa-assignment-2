import unittest
from bmi_api import calculateBMI, printBMI, getWeightInPounds, getHeightInInches


class bmiCalculationTest(unittest.TestCase):
    def test_underweight_bmi(self):
        bmi = calculateBMI(67, 100)
        self.assertEqual(bmi, 16.0)

    def test_normal_bmi(self):
        bmi = calculateBMI(63, 125)
        self.assertEqual(bmi, 22.7)

    def test_overweight_bmi(self):
        bmi = calculateBMI(67, 200)
        self.assertEqual(bmi, 32.1)


class bmiPrintTest(unittest.TestCase):

    def test_underweight_print_edge(self):
        result = printBMI(18.4)
        self.assertEqual(result, "With a BMI of 18.4 you are underweight.")

    def test_normal_print_edge_1(self):
        result = printBMI(18.5)
        self.assertEqual(result, "With a BMI of 18.5 your weight is normal.")

    def test_normal_print_edge_2(self):
        result = printBMI(24.9)
        self.assertEqual(result, "With a BMI of 24.9 your weight is normal.")

    def test_overweight_print_edge(self):
        result = printBMI(25)
        self.assertEqual(result, "With a BMI of 25 you are overweight.")


class bmiUserInputTest(unittest.TestCase):

    def test_bad_weight(self):
        result = getWeightInPounds()
        self.assertEqual(result, -1)
        
    def test_bad_height(self):
        result = getHeightInInches()
        self.assertEqual(result, -1)
