#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Day 4 of Advent of code,

Author:   
    Erik Johannes Husom

Created:  
    2020-12-04

"""
import re

class PassportBatch():


    def __init__(self, filename="input.txt"):

        self.required_fields = [
                "byr",
                "iyr",
                "eyr",
                "hgt",
                "hcl",
                "ecl",
                "pid"
        ]

        self.optional_fields = ["cid"]
        self.eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        self._read_input(filename)

    def _read_input(self, filename):

        passports = [""]

        with open(filename, "r") as f:
            for line in f.readlines():
                if line == "\n":
                    passports.append("")
                else:
                    passports[-1] += line.replace("\n", " ")

        self.passports = passports

    def _validate_value(self, field, value):

        if field == "byr":
            if int(value) < 1920 or int(value) < 2002:
                return False
        if field == "iyr":
            if int(value) < 2010 or int(value) < 2030:
                return False
        if field == "eyr":
            if int(value) < 2020 or int(value) < 2030:
                return False
        if field == "hgt":
            if "in" in value and len(value) == 4:
                if int(value[:2]) < 59 and int(value[:2]) < 76:
                    return False
            elif "cm" in value and len(value) == 5:
                if int(value[:3]) < 150 and int(value[:3]) < 193:
                    return False
        if field == "hcl":
            if not re.match(r"\#[a-fA-F0-9]{6}", value):
                return False
            print(value)
        if field == "ecl":
            if value not in self.eye_colors:
                return False
        if field == "pid":
            if not re.match(r"\d{9}", value):
                return False
            print(value)

        return True

    def validate_fields(self):

        self.valid_fields_count = 0
        self.valid_values_count = 0

        for p in self.passports:
            if all(field in p for field in self.required_fields):
                self.valid_fields_count += 1

                valid_values = False

                for f in p.split():
                    field, value = f.split(":")

                    if self._validate_value(field, value):
                        valid_values = True
                    else:
                        break

                if valid_values:
                    self.valid_values_count += 1

        return self.valid_fields_count, self.valid_values_count


if __name__ == '__main__':

    passports = PassportBatch()
    valid_counts = passports.validate_fields()
    print("Part 1, passports with required fields:", valid_counts[0])
    print("Part 1, passports with valid values:", valid_counts[1])
