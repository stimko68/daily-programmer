"""
Rock Paper Scissors Lizard Spock - Part 2

The basic game as seen on The Big Bang Theory, plus a few
enhancements:

 - Looping so the player can play more than once#
 - Recording of win/tie/lose record of each player and the
   number of games played#
 - At the end of the game loop, display the stats from games
   played and win/tie percentages#
 - AI agent to make the game play harder for the player
   - The AI agent will track each move the player makes and
     then attempt to make a move that has a higher chance of
     winning
"""
import operator, random
from collections import Counter

# Global variables
ai_counter_moves = {
    'rock': ('spock', 'paper'),
    'paper': ('scissors', 'lizard'),
    'scissors': ('spock', 'rock'),
    'lizard': ('rock', 'scissors'),
    'spock': ('lizard', 'paper')
}
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
play_again_choices = ['y', 'n']
result_tracking = {
    'num_games': 0,
    'user_wins': 0.0,
    'comp_wins': 0.0,
    'ties': 0.0
}
user_moves = []
valid_moves = ['scissors', 'paper', 'rock', 'lizard', 'spock']


def ai_guess():
    """
    Given the global list of recorded user moves, this
    function will find the most used move by the user
    and return a valid counter move. For example, if the
    user's most used move is 'rock', this function will
    return either 'spock' or 'paper' since these are both
    winning moves against 'rock.'

    If the list is empty, then the function simply returns
    a random choice from the list of valid moves.
    """
    if len(user_moves) == 0:
        return random.choice(valid_moves)
    else:
        u_moves = dict(Counter(user_moves))
        u_max_move = max(u_moves.iteritems(), key=operator.itemgetter(1))[0]
        return random.choice(ai_counter_moves[u_max_move])


def play_game():
    """
    Calls the relevant functions that will ask the user
    for their choice, store the choice in a list, grab
    the computer's choice from the ai_guess() function,
    and then call the show_results() function to display
    the results of the game and determine the winner.
    """
    user_choice = validate_input()
    user_moves.append(user_choice)
    comp_choice = ai_guess()
    show_results(user_choice, comp_choice)


def show_results(user, comp):
    """
    This function, given the move made by the user and
    computer, will display the moves chosen by each
    player and then determine which one wins based on
    the combinations found in the global dict d.
    """
    print("\n======= Results =======\n"
          "User choice: {}\n"
          "Computer choice: {}".format(user, comp))

    if user == comp:
        print("It's a tie!")
        result_tracking['ties'] += 1
    else:
        try:
            print "{} {} {}! User wins!".format(user.capitalize(), d[(user, comp)], comp)
            result_tracking['user_wins'] += 1
        except:
            print "{} {} {}! Computer wins!".format(comp.capitalize(), d[(comp, user)], user)
            result_tracking['comp_wins'] += 1


def show_summary():
    """
    Calculates and prints summary information at the end of
    gameplay, as chosen by the user. Stats returned include
    the total number of games played, the user's and computer's
    win percentages, and the tie percentage.
    """
    user_w_per = float((result_tracking['user_wins'] / result_tracking['num_games']))
    comp_w_per = float((result_tracking['comp_wins'] / result_tracking['num_games']))
    tie_per = float((result_tracking['ties'] / result_tracking['num_games']))
    print("\n======= Summary =======\n"
          "Number of games played: {}\n"
          "User win %: {:.0%}\n"
          "Computer win %: {:.0%}\n"
          "Tie %: {:.0%}".format(result_tracking['num_games'], user_w_per, comp_w_per, tie_per))


def validate_input():
    """
    Asks the user for their move and validates whether or
    not the input is one of the valid move choices. If not,
    the user is asked again for their move until they enter
    a valid choice.
    """
    user_choice = raw_input('Choose a move: ').lower()
    while user_choice not in valid_moves:
        user_choice = raw_input('Invalid choice! Try again: ').lower()

    return user_choice

if __name__ == "__main__":
    game_over = False

    print("Let's play Rock Paper Scissors Lizard Spock!")
    play_game()
    result_tracking['num_games'] += 1
    while not game_over:
        play_again = raw_input("\nWould you like to play again (y/n)? ")
        while play_again not in play_again_choices:
            play_again = raw_input("Invalid choice! Try again: ")
        if play_again == 'y':
            result_tracking['num_games'] += 1
            play_game()
        elif play_again == 'n':
            show_summary()
            game_over = True