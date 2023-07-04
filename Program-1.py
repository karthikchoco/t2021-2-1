class Calculator:
    def _init_(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
            return self.a / self.b
a = float(input())
b = float(input())
op = input()
calculator = Calculator(a, b)
if op == '+':
    result = calculator.add()
elif op == '-':
    result = calculator.sub()
elif op == '*':
    result = calculator.mul()
elif op == '/':
    result = calculator.div()
else:
    result = "Invalid operation."
print(result)
