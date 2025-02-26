#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:02:41 2025

@author: vivekmadhav
"""

def add_numbers(a, b):
    return a + b

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def is_even(n):
    return n % 2 == 0

print(add_numbers(5, 10))
print(factorial(5))
print(is_even(4))
