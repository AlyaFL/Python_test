""" Home task calculator module """
import math


class Calculator:
    """ Calculator implementation """
    def is_number(self, x, y=1) -> bool:
        """Checks the type of x and y"""
        return isinstance(x, int) and isinstance(y, int)

    def add(self, x: int, y: int) -> int:
        """ Add to attributes to each other """
        if self.is_number(x, y):
            return x + y
        return TypeError("Invalid value entered")

    def subtract(self, x: int, y: int) -> int:
        """ Subtract one attribute from another """
        if self.is_number(x, y):
            return x - y
        return TypeError("Invalid value entered")

    def divide(self, x: int, y: int) -> float:
        """ Divide x attribute on y """
        if y == 0:
            return ZeroDivisionError("Division by zero")
        elif self.is_number(x, y):
            return x / y
        return TypeError("Invalid value entered")

    def multiply(self, x: int, y: int) -> int:
        """ Multiply x attribute on y """
        if self.is_number(x, y):
            return x * y
        return TypeError("Invalid value entered")

    def mod(self, x: int, y: int) -> int:
        """ Take mod of one attribute from another """
        if y == 0:
            return ZeroDivisionError("Division by zero")
        elif self.is_number(x, y):
            return x % y
        return TypeError("Invalid value entered")

    def power(self, x: int, y: int) -> int:
        """ Raise attributes x to a power y """
        if self.is_number(x, y):
            return x ** y
        return TypeError("Invalid value entered")

    def root(self, x: int) -> float:
        """ Take a root from attributes """
        if self.is_number(x):
            if x > 0
                return math.sqrt(x) 
        return TypeError("Invalid value entered")
