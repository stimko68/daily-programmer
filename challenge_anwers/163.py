# Displays a graph showing the probability of
# rolling certain numbers on a six sided di
from collections import Counter
import random

def roll():
    return random.randint(1, 6)

def roll_dice(num_rolls):
    output = []
    counter = Counter(roll() for _ in range(num_rolls))
    for num, cnt in counter.iteritems():
        if num == 1:
            dice_one = (cnt / float(num_rolls)) * 100
        elif num == 2:
            dice_two = (cnt / float(num_rolls)) * 100
        elif num == 3:
            dice_three = (cnt / float(num_rolls)) * 100
        elif num == 4:
            dice_four = (cnt / float(num_rolls)) * 100
        elif num == 5:
            dice_five = (cnt / float(num_rolls)) * 100
        elif num == 6:
            dice_six = (cnt / float(num_rolls)) * 100
    output.append(dice_one)
    output.append(dice_two)
    output.append(dice_three)
    output.append(dice_four)
    output.append(dice_five)
    output.append(dice_six)
    return output

def output(input, num_rolls):

    print("# of Rolls\t1s\t\t2s\t\t3s\t\t4s\t\t5s\t\t6s")
    print("===========================================================")

    for i in input:
        print("%2d\t\t%2.2f%%\t%2.2f%%\t%2.2f%%\t%2.2f%%\t%2.2f%%\t%2.2f%%"
              % (num_rolls, input[0], dice_two, dice_three, dice_four,
                 dice_five, dice_six))


