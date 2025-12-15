#!/usr/bin/env python3
import os

def maximum_digit(digit_string : str):
    d_max = digit_string[0]
    max_id = 0
    for i, d in enumerate(digit_string):
        if d > d_max:
            d_max = d
            max_id = i
        if d == '9': 
            break

    return max_id, d_max


with open(os.path.dirname(os.path.realpath(__file__)) + '/input_sb') as f:

    n = 0

    for line in f:
        line = line.strip()
        first_idx, first_digit = maximum_digit(line[:-1])
        second_idx, second_digit = maximum_digit(line[first_idx+1:])

        number = int(first_digit)*10 + int(second_digit)
        print(f"line: {line} - {number}")
        n+=number


    print(f"Total n1: {n}")
