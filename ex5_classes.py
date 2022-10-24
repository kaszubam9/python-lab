#!/usr/bin/env python3
import cmath
from pathlib import Path

class ComplexNumber:

    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return f"({self.real}{'+' if self.imag >= 0 else '-'}{abs(self.imag)}j)"

    def __add__(self, element):
        if isinstance(element, (float, int)):
            element = ComplexNumber(element)
        return ComplexNumber(self.real + element.real, self.imag + element.imag)

    def __radd__(self, element):
        if isinstance(element, (float, int)):
            element = ComplexNumber(element)
        return self.__add__(element)

    def __sub__(self, element):
        if isinstance(element, (float, int)):
            element = ComplexNumber(element)
        return ComplexNumber(self.real - element.real, self.imag - element.imag)

    def __rsub__(self, element):
        return self.__sub__(element)

    def __mul__(self, element):
        if isinstance(element, (float, int)):
            element = ComplexNumber(element)
        return ComplexNumber(self.real * element.real - self.imag * element.imag,
                             self.imag * element.real + self.real * element.real)

    def __truediv__(self, element):
        if isinstance(element, (float, int)):
            element = ComplexNumber(element)
        divisor = (element.real ** 2 + element.imag ** 2)
        return ComplexNumber((self.real * element.real) - (self.imag * element.imag) / divisor,
                             (self.imag * element.real) + (self.real * element.imag) / divisor)


def ComplexCalculator():

    while True:
        params = []
        params.append(input("Enter real of the first number: "))
        params.append(input("Enter imag of the first number: "))
        params.append(input("Enter real of the second number: "))
        params.append(input("Enter imag of the second number: "))

        try:
            areal = float(params[0])
            aimag = float(params[1])
            breal = float(params[2])
            bimag = float(params[3])
            break
        except ValueError:
            print("Wrong values, try again entering integer or float")
            continue

    a = ComplexNumber(areal, aimag)
    b = ComplexNumber(breal, bimag)

    while True:
        op = input("Enter the operator: + - * /: ")
        if op == '+':
            result = a + b
            break
        elif op == '-':
            result = a - b
            break
        elif op == '*':
            result = a * b
            break
        elif op == '/':
            result = a / b
            break
        elif op == 'q':
            return
        else:
            print("\nWrong operator, try again or quit by entering: \"q\" ")
            continue

    print(f"The result of {a} {op} {b} == {result}")

if __name__ == '__main__':
    ComplexCalculator()
