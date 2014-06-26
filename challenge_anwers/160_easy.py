"""
Asks the user for measurements of sides and one or more angles
to calculate other properties of a right triangle.
"""
import math

sides = {'a': 0, 'b': 0, 'c': 0}
angles = {'A': 0, 'B': 0, 'C': 0}
angles['C'] = math.radians(90)


def get_int_range(low, high, prompt="", errmsg=""):
    if prompt == "":
        prompt = "Enter an integer between %d and %d: " % (low, high)
    if errmsg == "":
        errmsg = "Please enter a valid integer (%d-%d): " % (low, high)

    good_input = False
    n = 0

    while not good_input:
        inp = raw_input(prompt)
        try:
            n = int(inp)
            if str(n) == inp and low <= n <= high:
                good_input = True
        except:
            pass

        if not good_input:
            print errmsg

    return n

num_prompts = get_int_range(3, 4)

if num_prompts == 3:
    sides['a'] = int(raw_input("a="))
    sides['b'] = int(raw_input("b="))

    if sides['a'] > sides['b']:
        print("Sides are invalid length (a cannot be greater than b).")
    else:
        angles['B'] = math.radians(int(raw_input("B=")))
        sides['c'] = math.sqrt(sides['a']**2 + sides['b']**2)
        angles['A'] = math.asin(math.radians(sides['a'] / sides['c']))

        for i in sides:
            print("{}={}".format(i, sides[i]))
        for i in angles:
            print("{}={}".format(i, math.degrees(angles[i])))
elif num_prompts == 4:
    sides['a'] = int(raw_input("a="))
    sides['b'] = int(raw_input("b="))

    if sides['a'] > sides ['b']:
        print("Sides are invalid length (a cannot be greater than b).")
    else:
        angles['A'] = int(raw_input("A="))
        angles['B'] = int(raw_input("B="))
        if angles['A'] + angles['B'] + angles['C'] > 180:
            print("Angles add up to more than 180! Not a valid right triangle!")
        else:
            sides['c'] = math.sqrt(sides['a']**2 + sides['b']**2)

