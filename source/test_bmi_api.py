import unittest
from bmi_api import calculateBMI, printBMI, getWeightInPounds, getHeightInInches
from unittest.mock import patch


class bmiCalculationTest(unittest.TestCase):
    def test_bmi_calc_1(self):
        bmi = calculateBMI(67, 100)
        self.assertEqual(bmi, 16.0)

    def test_bmi_calc_2(self):
        bmi = calculateBMI(63, 125)
        self.assertEqual(bmi, 22.7)


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

    def test_overweight_print_edge_1(self):
        result = printBMI(25)
        self.assertEqual(result, "With a BMI of 25 you are overweight.")

    def test_overweight_print_edge_2(self):
        result = printBMI(29.9)
        self.assertEqual(result, "With a BMI of 29.9 you are overweight.")
    
    def test_obese_print_edge(self):
        result = printBMI(30)
        self.assertEqual(result, "With a BMI of 30 you are obese.")

    


class bmiBadUserInputTest(unittest.TestCase):
    stringInput = "hey"
    zeroInput = 0
    noInput = " "

    @patch('builtins.input', side_effect=stringInput)
    def test_word_weight(self, mock_input):
        result = getWeightInPounds()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=zeroInput)
    def test_zero_weight(self, mock_input):
        result = getHeightInInches()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=noInput)
    def test_blank_weight(self, mock_input):
        result = getHeightInInches()
        self.assertEqual(result, -1)
        
    @patch('builtins.input', side_effect=stringInput)
    def test_word_height(self, mock_input):
        result = getHeightInInches()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=zeroInput)
    def test_zero_height(self, mock_input):
        result = getHeightInInches()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=noInput)
    def test_blank_height(self, mock_input):
        result = getHeightInInches()
        self.assertEqual(result, -1)