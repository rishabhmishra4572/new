class Calculator:
    def __init__(self):
        # You could initialize state here if needed (e.g., storing a running total)
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero."
        return a / b

    def square(self, a, b = None):
        if a != 0:
            return a * a
        else:
            return 0

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    
    print("Addition (10 + 5):", calc.add(10, 5))
    print("Subtraction (10 - 5):", calc.subtract(10, 5))
    print("Multiplication (10 * 5):", calc.multiply(10, 5))
    print("Division (10 / 5):", calc.divide(10, 5))
    print("Division by zero (10 / 0):", calc.divide(10, 0))
    print("Square: ", calc.square(5))
