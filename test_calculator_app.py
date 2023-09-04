#create untit tests for basic_calculator.py
import unittest
import tkinter as tk
from basic_calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.calculator = Calculator(self.root)

    def test_add(self):
        self.calculator.num1_entry.insert(0, "10")
        self.calculator.num2_entry.insert(0, "5")
        self.calculator.add()
        self.assertEqual(self.calculator.result_label["text"], "Result: 15.0")

    def test_subtract(self):
        self.calculator.num1_entry.insert(0, "10")
        self.calculator.num2_entry.insert(0, "5")
        self.calculator.subtract()
        self.assertEqual(self.calculator.result_label["text"], "Result: 5.0")

    def test_multiply(self):
        self.calculator.num1_entry.insert(0, "10")
        self.calculator.num2_entry.insert(0, "5")
        self.calculator.multiply()
        self.assertEqual(self.calculator.result_label["text"], "Result: 50.0")

    def test_divide(self):
        self.calculator.num1_entry.insert(0, "10")
        self.calculator.num2_entry.insert(0, "5")
        self.calculator.divide()
        self.assertEqual(self.calculator.result_label["text"], "Result: 2.0")

    def test_invalid_input(self):
        self.calculator.num1_entry.insert(0, "abc")
        self.calculator.num2_entry.insert(0, "5")
        self.calculator.add()
        self.assertEqual(self.calculator.result_label["text"], "Result: ")

    def test_divide_by_zero(self):
        self.calculator.num1_entry.insert(0, "10")
        self.calculator.num2_entry.insert(0, "0")
        self.calculator.divide()
        self.assertEqual(self.calculator.result_label["text"], "Result: ")

if __name__ == "__main__":
    unittest.main()
# Run the test_calculator.py file. You should see the following output: