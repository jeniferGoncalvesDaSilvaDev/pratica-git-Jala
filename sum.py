class Sum:

    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def sum(self, num1: float | None = None, num2: float | None = None) -> float:
        a = self.num1 if num1 is None else num1
        b = self.num2 if num2 is None else num2
        return a + b

    def __str__(self) -> str:
        return f"Sum({self.num1}, {self.num2}) = {self.sum()}"


calculator = Sum(4, 5)
print(calculator.sum())  # 9
print(calculator)  # Sum(4, 5) = 9
