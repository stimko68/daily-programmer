"""
Final Grades - Test Data

Generate a random data (first and last name and grades) to use
as the input for the challenge answer to 167 Intermediate, which
is designed to take in a list of students and grades, calculate the
final averages for each, and then output the list to the terminal.

Each record should look like:
(first name), (last name) (score 1) (score 2) (score 3) (score 4) (score 5)
"""
import argparse
import names
import time
from random import randint


def generate_records(n):
    student_records = []
    for i in range(n):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        g1 = randint(0, 100)
        g2 = randint(0, 100)
        g3 = randint(0, 100)
        g4 = randint(0, 100)
        g5 = randint(0, 100)
        record = "{}, {} {} {} {} {} {}".format(first_name, last_name, g1,
                                                g2, g3, g4, g5)
        student_records.append(record)
    return check_dupes(student_records)


def check_dupes(input_list):
    output = []
    for i in input_list:
        if i not in output:
            output.append(i)
    return write_output(output)


def write_output(source_list):
    with open('records_{}.txt'.format(time.strftime('%m-%d-%Y_%H%M%S')), 'w+') as f:
        for item in source_list:
            f.write("%s\n" % item)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Program to generate random student records')
    parser.add_argument('-n', '--number', action='store', type=int, default=1, dest='input',
                        help='Integer used to determine how many records to generate. Default is 1')

    args = parser.parse_args()

    generate_records(args.input)