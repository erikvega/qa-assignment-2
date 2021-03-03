# Objective
Apply test-driven development (TDD) to implement a set of software requirements. Write unit
tests to provide adequate coverage of a code-base using your chosen unit testing framework and
test runner.

# Scenario
You have the responsibility to build an application interface to support various types of
decision-making tools for the app end-users. The users accessing the app come from a wide
range of disciplines and have different questions that the app will respond to. The application
will provide users with a list of functions that they can execute. You are to create an application
that allows the user to select and run each function and receive a correct response from the
program. The new development manager requires that you code the application using a testdriven development approach. We define a unit as a function or method in a class with a single
responsibility. The project should be developed and maintained using a GitHub repository. You
will develop a single application with a central interface allowing access to the functionality
listed below.

# Requirements
Command Line Interface - Develop a command line app that prompts the user to select a
function to execute and allows the user to gracefully exit the app when desired. The menu
should be displayed after each function (although a GUI is not required, you are permitted to
create one) unless the user exits. For now, the app must have the following functionalities.
1. __Body Mass Index__ - Input height in feet and inches. Input weight in pounds. Return
BMI value and category: Underweight = <18.5; Normal weight = 18.5–24.9;
Overweight = 25–29.9; Obese = BMI of 30 or greater (see formula linked in the Notes
& Resources section).

1. __Retirement__ - Input user's current age, annual salary, percentage saved (employer
matches 35% of savings). Input desired retirement savings goal. Output what age
savings goal will be met. You can assume death at 100 years (therefore, indicate if the
savings goal is not met).

# How to Run
Run main.py and it will take care of getting all the functionality from bmi_api.py and retirement_api.py
