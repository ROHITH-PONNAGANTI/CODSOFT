class InputFormatter:

    def __init__(self):
        self.expression = input("Enter the expression in the format 'number operator number': ")

    def format_input(self):
        components = self.expression.split(" ")
        try:
            num1 = float(components[0])
            operator = components[1]
            num2 = float(components[2])
            return num1, num2, operator
        except ValueError:
            print("Please enter valid numbers!")

class BasicCalculator:

    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
        self.result = 0

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Cannot divide by zero!"

    def perform_operation(self):
        if self.operator == '+':
            self.result = self.add()
        elif self.operator == '-':
            self.result = self.subtract()
        elif self.operator == '*' or self.operator == 'x':
            self.result = self.multiply()
        elif self.operator == '/':
            self.result = self.divide()
        else:
            self.result = "Invalid operator!"
        return self.result

if __name__ == '__main__':
    while True:
        user_input = InputFormatter()
        try:
            num1, num2, operator = user_input.format_input()
            print(f"First Number = {num1}\nOperator = {operator}\nSecond Number = {num2}")
            calculator = BasicCalculator(num1, num2, operator)
            result = calculator.perform_operation()
            print(f"{num1} {operator} {num2} = {result}")
        except TypeError:
            print("Please enter valid numbers and try again!")
        finally:
            user_choice = input("Do you want to continue calculations? (Y/N): ")
            if user_choice.lower() != 'y':
                break
