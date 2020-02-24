import os
import sys
from math import log2

# So I wrote some utility functions that I'm going to be using in this
# program and future programs.  I've been putting each lesson in its own
# folder/directory, but I want my utility functions to be in a "common" libs
# (libraries) directory that all of the lessons can use.  The "libs" directory
# is at the same directory level as the lessons themselves.  This next little bit
# of fanciness figures out the directory name (program_base) based on the
# pathname to this program (which Python makes available as sys.argv[0]).
# I then go up one directory and tack on 'libs' to the path.  This new path
# is placed at the front of the sys.path list that Python uses to determine where
# to look for modules.  If you want to see the value, just "print(sys.path)".
program_base = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.insert(0, os.path.dirname(program_base) + os.sep + 'libs')

# Bring in some utility functions that I wrote in the UserInput module.  By using
# modules, I achieve "code-reuse" (I'll use these functions in this program and
# others), I only have to make modifications in one place if I want to add new features
# or fix bugs, and I can make this program much easier to read without all that code
# cluttering it up.  It makes it much easier for you to get to the "business logic"
# of this code (e.g. what, exactly, am I trying to do in this code?).
#
# To get the Python auto complete to work in Visual Studio Code (where you can hover over a word
# and click on it to get to the code, for instance) for things placed in the libs directory (such as
# UserInput), at the top level of your workspace, create a .vscode directory and then create a
# settings.json in the .vscode directory.  Put the following in it (minus the "pound" # signs that
# mean comments in Python):
# {
#   "python.autoComplete.extraPaths": ["./libs"]
# }
from UserInput import get_integer, get_yes_no, get_choice

# Neat little trick to make long strings -- the triple quote
print("""
We're going to play a number guessing game.  First I'll ask you for an integer >= 1
which will be the maximum number for our game.  Then I'll ask you to think of a number between 1
and the maximum number.  If you want to play the game interactively, please respond 'y'
and I'll start guessing your number.  If you don't want to play the game interactively,
please respond 'n' and then enter the number that you picked.  I'll then play out the game
to see how many guesses it would have taken me to guess your number.
""")

# Get the maximum integer to use from the user
max_integer = get_integer(minInt=1)

# The maximum number of guesses we'll need, based on the maximum integer that the
# user wants to play with.  Note that if y = 2**x, then x = log2(y).  They are inverses
# of one another.  An example:
#  8 = 2**3   (2*2*2 = 8)
#  3 = log2(8)
# So, if the user specified max_integer = 8, then we'd int(log2(8)) + 1 = 3 + 1 = 4 guesses
# maximum.  We'll talk more about this in person while going over the program.
max_guesses = int(log2(max_integer)) + 1

print(f"I think I can guess your number in {max_guesses} tries!")

print(f"Please think of a number >= 1 and <= {max_integer}.")

# If the user does not want to play interactively, then get their number so that
# we can "play out the algorithm" for the user.
interactive = get_yes_no("Would you like to play interactively?")
if interactive == False:
    num_to_guess = get_integer(minInt=1, maxInt=max_integer, prompt="What was the number that you picked? ")

# At the beginning, our range is 1 <= max_integer.  lower and upper keep track of
# the lower and upper values of our range as the algorithm plays out.
lower = 1
upper = max_integer
current_guesses = 0

# Note that by keeping track of our guesses, we can exit the while loop should
# the user mess up.  In theory, assuming the user answers honestly and doesn't make
# a mistake, the while loop should never exit because of this conditional.  But, just
# in case, it's nice to know that we won't get stuck in an infinite loop.
while current_guesses < max_guesses:
    # We'll cut the current range in half (remember that // is the floor or integer part
    # of a division) and add it to the lower end of our range.  This will be our guess.
    # Effectively, we are eliminating half the range at each guess.  This algorithm
    # is known as a binary search, which *only* works if things are in sorted order.
    # We didn't have to sort anything, because implicitly, an integer range is already
    # in sorted order.  We'll talk more about binary search in person.
    increment = (upper - lower) // 2
    this_guess = lower + increment
    current_guesses += 1

    print(f"-- Guess {current_guesses}/{max_guesses}: {this_guess}")
    # If interactive, find out how our guess did.
    if interactive:
        user_choice = get_choice(prompt="Is your number equal to (e), lower (l), or higher(h)?", choices=['e','h','l'])
    else:
        # Mimic the user response (which we can do since we know num_to_guess)
        if this_guess == num_to_guess:
            # We got it!
            user_choice = 'e'
        elif this_guess < num_to_guess:
            # We guessed too low.  User would have responded that their number was higher.
            user_choice = 'h'
        else:
            # We guessed too high.  User would have responded that their number was lower.
            user_choice = 'l'
        print(f"Is your number equal to (e), lower (l), or higher(h)? [e/l/h] {user_choice}")

    if user_choice == 'e':
        print(f"FOUND IT!  It took me {current_guesses} guess(es) to find your number.")
        break
    elif user_choice == 'h':
        # We guessed too low, so set the new lower range to be one more than what we guessed.
        lower = this_guess + 1
    else:
        # We guessed too high, so set the new upper range to be one less than what we guessed.
        upper = this_guess - 1
else:
    # In theory, we should never get here, because we should have found the user's
    # number and invoked the 'break' statement (remember - else is only run if the while
    # loop never encountered a break).  Since we *know* our algorithm is correct, we'll
    # chide the user.
    print(f"\nDid you forget your number or make a mistake?  I could not find your number in {max_guesses} guess(es)!")