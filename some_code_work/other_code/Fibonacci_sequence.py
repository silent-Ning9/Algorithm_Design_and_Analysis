#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project    : ADA
@File       : Fibonacci_sequence.py
@IDE        : PyCharm
@Author     : silent
@Date       : 2025/11/7 15:47
@Desc       : 
'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    n = int(input("Enter a number of fibonacci numbers to generate: "))
    print(fibonacci(n))