#
# Let's create a little math game that tests how well a user can add 2 numbers
# together.  We'll use what we've learned so far - lists, if/else, while, variables,
# and print.  We'll also introduce a few more things that we'll eventually cover in a
# future lesson.
#

# We have not discussed import statements yet, but what this basically is saying
# is that we wish to import the randint and choice functions from Python's standard "random"
# module (by standard we mean that this module is present in all Python
# installations).  randint will pick a random integer between 2 values, and choice will
# pick a random item from a list.  For more information, check out:
#  https://docs.python.org/3/library/random.html
from random import randint, choice

# When the user gets the answer correct, we'll randomly pick one of these responses.
correct_responses = ["Great job!", "Correct!", "Awesome!", "You're a genius!"]

# When the user answers incorrectly, we'll randomly pick one of these responses.
incorrect_responses = ["Say what?!?", "Go back to first grade!",
    "You guessed incorrectly.", "You're making me cry."]

# The maximum number to use for each operand of the addition.  We will randomly
# pick a number between 0 and this number (inclusive, which means that the starting
# and ending values will be used as well).
maximum_number = 10

# Let's keep track of how many correct and incorrect answers the user had.  We'll
# display this when the user chooses to end the game with Ctrl-C.
correct_answers = 0
incorrect_answers = 0

# For some fanciness, we're going to use some ANSI escape sequences in our print statements
# that can output color.  In Visual Studio Code, the "TERMINAL" window is capable of properly
# dealing with these sequences, so we'll see our desired colors.  If this doesn't work for you and
# you see some gibberish on the screen, just set USECOLORS = False.  For the geeky details and to
# see what other colors are available, see the "Colors" section of:
#  https://en.wikipedia.org/wiki/ANSI_escape_code
# Note that in the print statements, we'll "bracket" what we want to print with a color (e.g. CRED)
# at the beginning of the print statement and a reset (CEND) at the end.  You can also change the
# background color as well, so for instance, red foreground (text) on a white background is '\033[91;107m'.
USECOLORS = True
if USECOLORS:
    CRED = '\033[91m'
    CGREEN = '\033[92m'
    CYELLOW = '\033[93m'
    CCYAN = '\033[96m'
    CEND = '\033[0m'
else:
    CRED = ''
    CGREEN = ''
    CYELLOW = ''
    CCYAN = ''
    CEND = ''

print(f"Let's play the addition game.  I will think of 2 numbers between 0 and {maximum_number}.")
print("You add them together and tell me the answer.  Press Ctrl-C to exit the game.")

# We haven't touched upon try/except blocks, so don't sweat this too much.  In short, when the user
# presses Ctrl-C to exit the game, Python will detect this and throw a KeyboardInterrupt exception.
# We'll catch this exception and gracefully exit the game.
try:
    while True:
        # Get 2 random integers between 0 and maximum_number (inclusive)
        x = randint(0, maximum_number)
        y = randint(0, maximum_number)
        sum = x + y

        # When getting input from a user, it's important to validate what the user enters.  We need to 
        # check that the user entered an integer.  The most straight-forward, "Pythonic" way to do this is to attempt to
        # convert the user's answer (which is a string) to an integer.  If this fails, Python will raise an exception, which
        # we'll catch.  This is a bit advanced, but it really is the "easiest" way.
        # First we set user_answer_integer to None, and then we'll loop until we're able to successfully convert
        # the user's string to an integer (meaning user_answer_integer gets assigned a value instead of an exception
        # being raised).
        user_answer_integer = None
        while user_answer_integer == None:
            # Ask the user for the answer to the question
            user_answer = input(f"What is {x} + {y}? ")
            try:
                user_answer_integer = int(user_answer)
            except ValueError:
                print(f"{CYELLOW}=> How about entering an integer next time!  Let's try this again...{CEND}")
        
        if user_answer_integer == sum:
            # Correct!
            correct_answers = correct_answers + 1
            # Now let's pick a random entry from the correct_responses list (note that the choice method that we imported does exactly this!)
            # and display it to the user.
            print(f"{CGREEN}=> {choice(correct_responses)}{CEND}")
        else:
            # Incorrect
            incorrect_answers = incorrect_answers + 1
            # Display a random entry from the incorrect_responses list as well as the answer.
            print(f"{CRED}=> {choice(incorrect_responses)}  The correct answer is {sum}.{CEND}")

except KeyboardInterrupt:
    print()
    print(f"{CCYAN}Thanks for playing.  You had {CGREEN}{correct_answers}{CCYAN} correct and {CRED}{incorrect_answers}{CCYAN} incorrect answers.{CEND}")

