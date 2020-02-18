#
# This is a continuation of our math game from lesson 02.  This time, we're going to use what
# we've learned about functions to add in support for letting the user choose what game they
# want to play (addition, subtraction, multiplication, division).  We'll also let the user
# choose the maximum_number in addition to whether or not they'd like to allow negative
# numbers.
import sys
# An example of how you can import different things based on the version of Python being used
if sys.version_info >= (3, 6):
    # Python 3.6 introduced the secrets module - let's use it if we can
    from secrets import SystemRandom
else:
    # Else use the older random module
    from random import SystemRandom

# Make things a bit more "cryptographically secure" by using SystemRandom
sys_random = SystemRandom()

# When the user gets the answer correct, we'll randomly pick one of these responses.
correct_responses = ["Great job!", "Correct!", "Awesome!", "You're a genius!"]

# When the user answers incorrectly, we'll randomly pick one of these responses.
incorrect_responses = ["Say what?!?", "Go back to first grade!",
    "You guessed incorrectly.", "You're making me cry."]

# The default maximum number to use for each operand.  We will randomly
# pick a number between 0 and this number (inclusive, which means that the starting
# and ending values will be used as well) if the user only wants to play with
# positive numbers.  If they want to play with negative numbers, we'll broaden the range
# to be "-max_number" to "+max_number".
default_max_number = 10

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

def print_color(color, msg):
    print(f"{color}{msg}{CEND}")

def get_random_number(min_number, max_number):
    return sys_random.randint(min_number, max_number)

def get_random_numbers(min_number, max_number):
    return get_random_number(min_number, max_number), get_random_number(min_number, max_number)

def addition(min_number, max_number):
    x, y = get_random_numbers(min_number, max_number)
    result = x + y
    return x, y, result

def subtraction(min_number, max_number):
    x, y = get_random_numbers(min_number, max_number)
    result = x - y
    return x, y, result

def multiplication(min_number, max_number):
    x, y = get_random_numbers(min_number, max_number)
    result = x * y
    return x, y, result

def division(min_number, max_number):
    # We want to keep the division operands within min_number and max_number.

    # We'll be returning x, y, x/y

    # Get x
    x = get_random_number(min_number, max_number)

    if x == 0:
        # User got an easy one (0/y = 0)
        # We can pick anything in the requested range for y (other than 0).
        # Get a random y
        y = get_random_number(min_number, max_number)

        # So that we don't risk a division by 0, we require that y be non-zero.
        # We'll just increment it by 1 should it be 0.
        if y == 0:
            y = y + 1
    else:
        # Our approach will be to get all the possible divisors that don't produce a
        # remainder.  Note that the '//' operator is the floor divide operation - in the event
        # of a remainder, just chop it off and give back the integer part.  abs is the absolute
        # value function (turn a negative number into its positive equivalent).
        abs_x = abs(x)
        # The range iterator does not include the end value, so we need to add 1 more so that we include abs_x//2.
        range_top = abs_x//2 + 1
        # 1 is always a divisor
        divisors = [1]
        for i in range(2, range_top):
            # % is the "modulo" (remainder) operator - if the remainder is 0, it's an integer divisor
            if x % i == 0:
                divisors.append(i)
        # And the number itself is also always a divisor
        divisors.append(abs_x)
        
        # Pick a random number from divisors for y.  I know random is supposed to be random, but for whatever reason,
        # in testing this code, the end values tend to get picked a lot (e.g. 1 and abs_x).
        y = sys_random.choice(divisors)

        # If the user is allowing negative numbers, we'll randomly pick whether y will be
        # positive or negative
        if min_number < 0:
            y = y * sys_random.choice([-1, 1])

    result = int(x / y)
    return x, y, result

# Remember - function names are variables!  We're forming a list of functions!
operations = [addition, subtraction, multiplication, division]
# Symbols that correspond to the operations.  We use these in our print statment to the user.
# Note how each item in the list correlates with the same spot in the operations list.
symbols = ["+", "-", "*", "/"]

# Index of the default game to play - default to addition.  Yes, we could just hard-code it to 0, but
# we'll find the index position of the function instead.
default_game_to_play = operations.index(addition)

# Get the game to play
game_to_play = None
while game_to_play == None:
    game_to_play_in = input(f"What game would you like to play?  Addition (0), Subtraction (1), Multiplication (2), or Division (3) [{default_game_to_play}] ")
    # If the user pressed the enter key or entered all white space, we'll take that as wanting to play the default game
    if game_to_play_in == "" or game_to_play_in.isspace():
        game_to_play = default_game_to_play
    else:
        try:
            user_answer_integer = int(game_to_play_in)
            # Validate that the integer is between 0 and the length of our operations list (less 1).  If it's not,
            # we'll raise the same exact exception that python would yield for an invalid integer!
            if user_answer_integer < 0 or user_answer_integer > len(operations)-1:
                raise ValueError
            else:
                game_to_play = user_answer_integer
        except ValueError:
            print_color(CYELLOW, f"=> How about entering an integer between 0 and {len(operations)-1}.  Let's try this again...")

# Get the maximum number to play with
max_num_integer = None
while max_num_integer == None:
    max_num = input(f"What is the maximum number you'd like to use?  0 is not allowed!  Enter a negative number if you want to use negative numbers [{default_max_number}] ")
    # If the user pressed the enter key or entered all white space, we'll take that as wanting to play with the default max
    if max_num == "" or max_num.isspace():
        max_num_integer = default_max_number
    else:
        try:
            max_num_integer = int(max_num)
            # Don't let the user specify 0
            if max_num_integer == 0:
                max_num_integer = None
                raise ValueError
        except ValueError:
            print_color(CYELLOW, f"=> How about entering a non-zero integer next time!  Let's try this again...")

# If the user specified a negative number, that becomes the minimum
if max_num_integer < 0:
    min_num = max_num_integer
# Otherwise 0 is the minimum
else:
    min_num = 0
# abs is a function that returns the absolute value of a number (turning all negative numbers positive)
max_num = abs(max_num_integer)

print(f"I will think of 2 numbers between {min_num} and {max_num}.  You do the math and tell me the answer.  Press Ctrl-C to exit the game.")
# We haven't touched upon try/except blocks, so don't sweat this too much.  In short, when the user
# presses Ctrl-C to exit the game, Python will detect this and throw a KeyboardInterrupt exception.
# We'll catch this exception and gracefully exit the game.
try:
    while True:
        # operations[game_to_play] yields a variable that is really a function (e.g. addition).
        # We can now call this variable (function) with arguments.  For instance, if the user wanted
        # addition, game_to_play will be 0, and operations[0] will be the function addition.  It will
        # be as if we called addition(min_num, max_num).  Yes, this is advanced stuff, but I think you can
        # get the hang of it!
        x, y, result = operations[game_to_play](min_num, max_num)

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
            user_answer = input(f"What is {x} {symbols[game_to_play]} {y}? ")
            try:
                user_answer_integer = int(user_answer)
            except ValueError:
                print_color(CYELLOW, f"=> How about entering an integer next time!  Let's try this again...")
        
        if user_answer_integer == result:
            # Correct!
            correct_answers = correct_answers + 1
            # Now let's pick a random entry from the correct_responses list (note that the choice method does exactly this!)
            # and display it to the user.
            print_color(CGREEN, f"=> {sys_random.choice(correct_responses)}")
        else:
            # Incorrect
            incorrect_answers = incorrect_answers + 1
            # Display a random entry from the incorrect_responses list as well as the answer.
            print_color(CRED, f"=> {sys_random.choice(incorrect_responses)}  The correct answer is {result}.")

except KeyboardInterrupt:
    print()
    print_color(CCYAN, f"Thanks for playing.  You had {CGREEN}{correct_answers}{CCYAN} correct and {CRED}{incorrect_answers}{CCYAN} incorrect answers.")
    total_answers = correct_answers + incorrect_answers
    if total_answers != 0:
        score = (correct_answers / total_answers) * 100.0
        # The :.2f is something we haven't seen yet - it means to display as a floating point number with 2 places after the decimal point
        print_color(CCYAN, f"Your final score is {score:.2f}%.")
    else:
        print_color(CCYAN, f"Chicken!  Did the first question scare you?")
