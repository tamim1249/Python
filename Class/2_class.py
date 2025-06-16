class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x):
        self.result += x

    def subtract(self, x):
        self.result -= x

    def multiply(self, x):
        self.result *= x

    def divide(self, x):
        if x != 0:
            self.result /= x
        else:
            print("Cannot divide by zero.")

    def show_result(self):
        print("Result:", self.result)

# Object তৈরি করে কাজ করো
calc = Calculator()
calc.add(10)
calc.multiply(2)
calc.subtract(5)
calc.show_result()  # Output: Result: 15
