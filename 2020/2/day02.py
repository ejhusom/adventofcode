#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Day 2 of Advent of code.

Author:   
    Erik Johannes Husom

Created:  
    2020-09-18

"""
import numpy as np

passwords = np.loadtxt("input.txt", dtype=np.str)

valid_passwords = 0

for p in passwords:

    low = int(p[0].split("-")[0])
    high = int(p[0].split("-")[1])
    letter = p[1][:-1]
    password = p[2]

    if password.count(letter) >= low and password.count(letter) <= high:
        valid_passwords += 1

print("Part One - Valid passwords:", valid_passwords)

valid_passwords = 0

for p in passwords:

    pos1 = int(p[0].split("-")[0]) - 1
    pos2 = int(p[0].split("-")[1]) - 1
    letter = p[1][:-1]
    password = p[2]

    if (password[pos1] == letter) ^ (password[pos2] == letter):
        valid_passwords += 1

print("Part Two - Valid passwords:", valid_passwords)
