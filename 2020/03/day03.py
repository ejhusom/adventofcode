#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Advent of code day 3.

Author:   
    Erik Johannes Husom

Created:  
    2020-12-03

"""
import numpy as np

def read_input(filename="input.txt"):

    landscape = []

    with open("input.txt", "r") as f:
        for l in f.readlines():
            landscape.append(list(l.strip()))

    return np.array(landscape)

def find_encountered_trees(landscape, right, down):

    x = 0
    y = 0
    encountered_trees = 0

    while y < landscape.shape[0] - down:
        x = (x + right) % landscape.shape[1]
        y += down

        if landscape[y,x] == "#":
            encountered_trees += 1

    print(f"Right {right}, down {down}: {encountered_trees}")

    return encountered_trees

if __name__ == '__main__':

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    landscape = read_input()
    product = 1

    for s in slopes:
        product *= find_encountered_trees(landscape, s[0], s[1])

    print("Product:", product)



