"""
Block Count, Length & Area

Given a map of a construction site represented by ASCII characters,
calculate the following:

 - Count of the number of blocks
 - Circumference of each block type (in linear feet or LF)
 - Area of each block type (in square feet or SF)

Rules:
 - Each character = 10 x 10 ft
 - Each block = 100 SF
 - When area and circumference are calculated, the same
   characters of each type are accounted for as if they
   were all in the same line

Examples:

Input:  ####
        @@oo
        o*@!
        ****
Output: #: Total SF (400), Total LF (100) - Found 1 block
        @: Total SF (300), Total LF (80) - Found 2 blocks
        o: Total SF (300), Total LF (80) - Found 2 blocks
        *: Total SF (500), Total LF (120) - Found 2 blocks
        !: Total SF (100), Total LF (40) - Found 1 block

Note: This answer does not calculate block counts
"""
from collections import defaultdict


def parse_input(input_file):
    chars = defaultdict(int)
    string = ''
    with open(input_file, 'r') as f:
        for i in f:
            string += i.strip()

    for c in string:
        chars[c] += 1

    return chars


def calculate_area(area_dict):
    area_answers = {}
    for key, value in area_dict.items():
        area_answers[key] = area_dict[key] * 100
    return area_answers


def calculate_circumference(circ_dict):
    circ_answers = {}
    for key, value in circ_dict.items():
        circ_answers[key] = ((circ_dict[key] * 2) + 2) * 10
    return circ_answers

if __name__ == "__main__":
    d = parse_input('168_intermediate.txt')
    areas = calculate_area(d)
    circs = calculate_circumference(d)
    for k, v in areas.items():
        print('{}: Total SF ({}), Total LF ({})'.format(k, areas[k], circs[k]))