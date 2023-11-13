import unittest
from math_quiz import randomInteger, randomOperator, computeByOperator

class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = randomInteger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if random operator generated are within the specified range 
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test the random operator
            rand_operator = randomOperator()
            self.assertTrue(rand_operator in operators)

    def test_function_C(self):
        # The test cases
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 4, '-', '8 - 4', 4),
            (3, 6, '*', '3 * 6', 18),
            (7, 4, '+', '7 + 4', 11),
            (3, 6, '-', '3 - 6', -3),
            (4, 7, '*', '4 * 7', 28)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            # Get the result of the calculation and adjust.
            problem, answer = computeByOperator(num1, num2, operator)
            self.assertTrue(problem == expected_problem)
            self.assertTrue(answer == expected_answer)

if __name__ == "__main__":
    unittest.main()
