#!/usr/bin/env python3
import math
import random
import numpy as np
import copy
from pathlib import Path

def EquationRoots(a, b, c):
    print(f"\nQuadratic equation: y = {a}x^2+{b}x+{c}\n")

    delta = b * b - 4 * a * c

    if delta > 0:
        sqrtdelta = math.sqrt(delta)
        x1 = (-b + sqrtdelta)/(2 * a)
        x2 = (-b - sqrtdelta) / (2 * a)
        print(f"Delta > 0, X1 = {x1}, X2 = {x2}")
    elif delta == 0:
        x0 = -b / (2 * a)
        print(f"Delta = 0, X0 = {x0}")
    else:
        print("Delta less than zero")
        return

def Sort(nums):
    flag = True
    while flag:
        flag = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp
                flag = True

    print(f"Sorted numbers: {nums}")

def ScalarProduct():
    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]

    if len(a) != len(b):
        print("Dimensions of vectors don't match")
        return

    scalar = 0
    for i in range(len(a)):
        scalar += a[i] * b[i]

    print(f"Scalar product of vectors a and b: {scalar}")

def AddMatrix():
    dimension = 128
    A = np.random.randint(10, size=(dimension,dimension))
    B = np.random.randint(10, size=(dimension,dimension))
    sum = [[A[i][j] + B[i][j] for j in range(dimension)] for i in range(dimension)]

    if np.allclose(sum, np.add(A, B)):
        print("Correct result of adding matrices")
    else:
        print("Wrong result of adding matrices")

def ProductOfMatrix():
    dimension = 8
    A = np.random.randint(10, size=(dimension, dimension))
    B = np.random.randint(10, size=(dimension, dimension))
    product = np.zeros((dimension,dimension))

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                product[i][j] += A[i][k] * B[k][j]

    if np.allclose(product, np.array(A) @ np.array(B)):
        print(f"Correct result of multiplying matrices")
    else:
        print("Wrong result of multiplying matrices")

def CountDeterminant(A):

    if len(A) == 1:
        return A[0][0]
    else:
        det = 0
        for i in range(len(A[0])):
            #Making smaller matrix
            B = copy.deepcopy(A)
            B = np.delete(B, 0, 0)
            B = np.delete(B, i, 1)

            det += ((-1) ** i) * A[0][i] * CountDeterminant(B)
        return det

def Determinant():
    #
    dimension = np.random.randint(1, 5)
    A = np.random.randint(10, size=(dimension, dimension))
    det = CountDeterminant(A)
    if np.allclose(det, np.linalg.det(A)):

        print(f"Correct determinant of matrix A: det A = {det}")
    else:
        print("Wrong result of counting determinant")

if __name__ == '__main__':
    EquationRoots(2, 5, 3)

    randomNumbers = [random.randint(0, 100) for _ in range(50)]
    Sort(randomNumbers)

    ScalarProduct()

    AddMatrix()

    ProductOfMatrix()

    Determinant()