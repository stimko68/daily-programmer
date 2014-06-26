"""
Reproduction of the hacking mini game found in Fallout 3.
Asks user for a difficulty level and then returns a list
of words. The program chooses one of these words at random,
and the user must guess the correct one. The user only has
four tries.
"""
import operator
import random


"""
Takes an integer and returns a tuple that contains two integers,
one for the number of words the user will have to choose from,
and another for the length of the words in the choice list.
"""
def difficulty_level(difficulty_choice):
    num_choices = 0
    word_length = 0
    if difficulty_choice == 1:
        num_choices = 5
        word_length = 5
    elif difficulty_choice == 2:
        num_choices = 8
        word_length = 9
    elif difficulty_choice == 3:
        num_choices = 10
        word_length = 13
    elif difficulty_choice == 4:
        num_choices = 12
        word_length = 17
    elif difficulty_choice == 5:
        num_choices = 15
        word_length = 21
    return num_choices, word_length


"""
Given two integers returns a list of randomly chosen words
from an external text file. The words are chosen based on
their length defined by the word_length parameter and the
number of items in the list is determined by the num_choices
parameter.
"""
def generate_word_list(num_choices, word_length):
    matching_words = []
    word_choice_list = []
    with open("enable1.txt", 'r') as word_source:
        for word in word_source:
            if len(word) == word_length + 1:
                matching_words.append(word.rstrip())
    for i in range(num_choices):
        word_choice_list.append(random.choice(matching_words))
    return word_choice_list


"""
Takes a list of strings, prints them out, randomly selects one
as the answer, and asks the user to guess which one was selected.
If the user chooses incorrectly, the function will tell the user
how many of the characters in the guessed string match the selected
string.
"""
def user_guesses(word_choice_list):
    guesses = 4
    game_over = False

    for word in word_choice_list:
        print word.upper()

    selected_word = random.choice(word_choice_list)
    selected_word_length = len(selected_word)

    while not game_over:
        guess_word = (raw_input("Guess (%s left)? " % guesses)).lower()
        if guess_word == selected_word:
            game_over = True
            print("You win!")
        else:
            num_correct_letters = map(operator.eq, guess_word, selected_word).count(True)
            guesses -= 1
            print("%s/%s correct" % (num_correct_letters, selected_word_length))


"""
Main function asks the user to choose a difficulty level, and then
calls the other functions of the program to generate the list of
guessed words and handle the user's guesses.
"""
def main():
    game_level = int(raw_input("Difficulty (1-5)? "))
    main_num_choices, main_word_length = difficulty_level(game_level)
    word_list = generate_word_list(main_num_choices, main_word_length)
    user_guesses(word_list)

main()