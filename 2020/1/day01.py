#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Advent of code, day 1.

Author:   
    Erik Johannes Husom

Created:  
    2020-12-01

"""


def read_expense_report():
    """Read the numbers if expense report."""

    numbers = []

    with open("expense-report.txt", "r") as f:
        for line in f.readlines():
            numbers.append(int(line.strip()))

    return numbers


def solve_puzzle_1():
    """Find the two numbers that sum to 2020.

    Returns:
        product (int): The product of the two numbers that sum to 2020.

    """

    numbers = read_expense_report()

    for i, number1 in enumerate(numbers):
        for number2 in numbers[i + 1 :]:
            if number1 + number2 == 2020:
                return number1 * number2


def solve_puzzle_2():
    """Find the three numbers that sum to 2020.

    Returns:
        product (int): The product of the three numbers that sum to 2020.

    """

    numbers = read_expense_report()

    for i, number1 in enumerate(numbers):
        for j, number2 in enumerate(numbers[i + 1 :]):
            for number3 in numbers[j + 1 :]:
                if number1 + number2 + number3 == 2020:
                    return number1 * number2 * number3


if __name__ == "__main__":

    print(f"Puzzle 1: {solve_puzzle_1()}")
    print(f"Puzzle 2: {solve_puzzle_2()}")
