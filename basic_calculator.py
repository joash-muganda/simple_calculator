import tkinter as tk
from tkinter import messagebox
#add more functions such modulus, square root, and exponent

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")

        # Create input fields
        self.num1_entry = tk.Entry(self.root)
        self.num2_entry = tk.Entry(self.root)

        # Create buttons and associate them with their operations
        self.add_button = tk.Button(self.root, text="Add", command=self.add)
        self.sub_button = tk.Button(self.root, text="Subtract", command=self.subtract)
        self.mul_button = tk.Button(self.root, text="Multiply", command=self.multiply)
        self.div_button = tk.Button(self.root, text="Divide", command=self.divide)

        # Label to display the result
        self.result_label = tk.Label(self.root, text="Result: ")

        # Place the widgets on the window
        self.num1_entry.grid(row=0, column=0)
        self.num2_entry.grid(row=0, column=1)
        self.add_button.grid(row=1, column=0)
        self.sub_button.grid(row=1, column=1)
        self.mul_button.grid(row=2, column=0)
        self.div_button.grid(row=2, column=1)
        self.result_label.grid(row=3, columnspan=2)
#create add function
    def add(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = num1 + num2
            self.result_label["text"] = "Result: " + str(result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
#create subtract function
    def subtract(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = num1 - num2
            self.result_label["text"] = "Result: " + str(result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
#create multiply function
    def multiply(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = num1 * num2
            self.result_label["text"] = "Result: " + str(result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
#create divide function
    def divide(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
            else:
                result = num1 / num2
                self.result_label["text"] = "Result: " + str(result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
