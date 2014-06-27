"""
Final Grades

Given a text file containing a list of students and their grades, the
program calculates the final grades for each student and output them
from highest to lowest. Other rules:

 - Each student can earn a total of 500 points
 - Letter grades are assigned based on a 10 point scale
 - If a score is in the top 3% of the rank it gets a "+" added (e.g., B+)
 - Conversely, the low 3% gets a "-" (e.g., B-)
 - Pluses and minuses do not apply to A's or F's
 - Final grades are rounded to the nearest whole number (e.g., 89.5 = 90 and
   89.4 = 89)
 - In the final output, the student's grades should be sorted left to right
   from highest to lowest, followed by the final grade
"""
import argparse
import re


class Student(object):

    def __init__(self, first, last, grade_list):
        self.first = first
        self.last = last
        self.grade_list = grade_list
        self.final_grade = 0
        self.final_grade_letter = ''
        self.grade_sum = 0

    def calculate_final_grades(self):
        for grade in self.grade_list:
            self.grade_sum += grade

        self.final_grade = (self.grade_sum / len(self.grade_list))

        if 90 <= self.final_grade <= 100:
            self.final_grade_letter = 'A'
        elif 80 <= self.final_grade <= 89:
            if self.final_grade >= 87:
                self.final_grade_letter = 'B+'
            elif self.final_grade <= 82:
                self.final_grade_letter = 'B-'
            else:
                self.final_grade_letter = 'B'
        elif 70 <= self.final_grade <= 79:
            if self.final_grade >= 77:
                self.final_grade_letter = 'C+'
            elif self.final_grade <= 72:
                self.final_grade_letter = 'C-'
            else:
                self.final_grade_letter = 'C'
        elif 60 <= self.final_grade <= 69:
            if self.final_grade >= 67:
                self.final_grade_letter = 'D+'
            elif self.final_grade <= 62:
                self.final_grade_letter = 'D-'
            else:
                self.final_grade_letter = 'D'
        else:
            self.final_grade_letter = 'F'

        self.grade_list.sort(reverse=True)

        #return "%10s, %10s\t\t(%.1f) (%2s): %s" % (self.last, self.first, self.final_grade, self.final_grade_letter, self.grade_list)
        return "{0}, {1} ({2})".format(self.last, self.first, self.final_grade)

    #Used for testing
    def sort_grades(self):
        return self.grade_list.sort(reverse=True)

    #Used for testing
    def print_grades(self):
        return self.grade_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Program to input student grades and output final scores')
    parser.add_argument('-i', '--input', action='store', default=None, dest='input',
                        help='Input file containing list of student names and list of grades.')

    args = parser.parse_args()

    with open(args.input) as f:

        all_students = []

        for line in f:
            match = re.match(r'^([^,]+)\s*,(\s*\D+)+\s*(.*)', line)
            first_name, last_name = match.group(1).strip(), match.group(2).strip()
            scores = [float(x) for x in re.split(r'\s+', match.group(3).strip())]
            student = Student(first_name, last_name, scores)
            print(student.calculate_final_grades())