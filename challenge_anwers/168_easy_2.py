"""
String Index

Given an input string and a series of integers, create indexes for each
valid word in the string and then return a string based on the given
integers.

Example:

Input string:   "The lazy cat slept in the sunlight."
Input ints:     1 3 4
Output: "The cat slept"
"""
import re

input_string = "...You...!!!@!3124131212 Hello have this is a --- " \
               "string Solved !!...? to test @\n\n\n#!#@#@%$**#$@ " \
               "Congratz this!!!!!!!!!!!!!!!!one ---Problem\n\n"
indexes = [12, -1, 1, -100, 4, 1000, 9, -1000, 16, 13, 17, 15]


def parse_string(int_list, in_string):
    answer = ''
    cleaned_input = []
    strings = re.findall(r'[a-zA-Z0-9]+', in_string)
    for i in int_list:
        if 0 < i <= len(strings):
            cleaned_input.append(strings[i-1])

    for j in cleaned_input:
        answer += j + " "

    return answer

if __name__ == "__main__":
    print parse_string(indexes, input_string)