"""
Rock Paper Scissors Lizard Spock

The basic game as seen on The Big Bang Theory. The player is
prompted to choose a hand, one is randomly chosen
for the computer, and then the results are displayed.
"""
import random

valid_moves = ['scissors', 'paper', 'rock', 'lizard', 'spock']

d = {
    ('paper', 'scissors'): 'cuts',
    ('spock', 'scissors'): 'smashes',
    ('paper', 'rock'): 'covers',
    ('rock', 'lizard'): 'crushes',
    ('lizard', 'spock'): 'poisons',
    ('lizard', 'paper'): 'eats',
    ('rock', 'scissors'): 'crushes',
    ('scissors', 'lizard'): 'decapitates',
    ('paper', 'spock'): 'disproves',
    ('spock', 'rock'): 'vaporizes'
}


def play_game():
    print("Let's play Rock Paper Scissors Lizard Spock!")
    user_choice = raw_input('Choose a move: ').lower()
    while user_choice not in valid_moves:
        user_choice = raw_input('Invalid choice! Try again: ').lower()

    comp_choice = random.choice(valid_moves)
    show_results(user_choice, comp_choice)


def show_results(user, comp):
    print("\n======= Results =======\n"
          "User choice: {}\n"
          "Computer choice: {}".format(user, comp))

    if user == comp:
        print("It's a tie!")
    else:
        try:
            print "{} {} {}! User wins!".format(user.capitalize(), d[(user, comp)], comp)
        except:
            print "{} {} {}! Computer wins!".format(comp.capitalize(), d[(comp, user)], user)

if __name__ == "__main__":
    play_game()