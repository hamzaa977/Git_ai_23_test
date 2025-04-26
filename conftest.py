from calculator import Calculator
import pytest


class PreciseCalculator(Calculator):
    def __init__(self, precision=2):
        super().__init__()
        self.precision = precision

    def add(self, a, b):
        result = super().add(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def subtract(self, a, b):
        result = super().subtract(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def multiply(self, a, b):
        result = super().multiply(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def divide(self, a, b):
        result = super().divide(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def factorial(self, n):
        result = super().factorial(n)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def fibonacci(self, caluculator_Instance, n):
        result = super().fibonacci(n)
        if isinstance(result, float):
            return round(result, self.precision)
        return result