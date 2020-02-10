#
# Lesson 02:
#  Conditional Logic (introduction)
#

# I'm going to define a little helper function that will allow me to pause/resume the
# program while I'm doing the presentation.  Don't worry about this for now.  If you
# are running this program in "non-presentation" mode, then set PRESENTATION_MODE to False.
PRESENTATION_MODE = True
def pause_program():
    print()
    if PRESENTATION_MODE:
        input("*** Program paused.  Press Enter key to resume...")
    print("*" * 80)
    print()

# Take a moment to look at the pause_program function that was defined above.
# Specifically, look at the indentation (spacing) on the lines following the
# "def pause_program():" line.  Notice how they are all indented with leading
# white space.  This leading white space is *very* important in Python.  Statements
# that have the same exact indentation (typically 4 spaces) are part of the same
# block of code.  The nice thing about editors like Visual Studio Code is that
# they "magically" take care of this for you.  They even make it graphically
# appealing by drawing vertical lines to show you what statements belong to
# what block of code, and you can even shrink/expand the block (I'll show you
# how to do this in the presentation).

# So how do we change the flow of execution of a program?  One way is with the
# "if" statement.  A basic "if" statement starts with the keyword "if" and then lists
# the conditional logic that will be applied to determine whether or not to
# enter the block of code.  Let's see an example.
weather = 'sunny'
if weather == 'sunny':
    print("It's a beautiful day!  Let's go to the beach.")
pause_program()

# Notice the double equal sign in the condition.  A single equal sign is used
# for variable assigment, whereas a double equal sign is used for testing equality.

# How about testing for inequality (2 things not equal)?
if weather != 'rainy':
    print("Yes!  Since it's not raining, I think we should play outside.")
pause_program()

# What if we want to do something different if the condition fails?  Enter the
# 'else' keyword.
if weather == 'rainy':
    print("So sad that it's raining.")
else:
    print("Awesome!  It's not raining.  The weather is {}.".format(weather))
pause_program()

# What if we want to test multiple conditions, taking the first one that succeeds?
# Enter the 'elif' keyword.
if weather == 'rainy':
    print("So sad that it's raining.")
elif weather == 'cloudy':
    print("Hmmm... should we take a chance and go to the pool?")
elif weather == 'snowy':
    print("Yes!  It's snowing!  No school today!!!")
elif weather == 'sunny':
    print("Let's get our swimsuits on and head to the pool.")
else:
    print("None of our conditions matched.  The weather is {}.".format(weather))
pause_program()

# Do you have to use the "else" keyword if you use "elif"?  Nope.
if weather == 'rainy':
    print("Boo hoo.  It's raining.")
elif weather == 'sunny':
    print("Wow, it's hot outside.  Let's go get some popsicles.")
pause_program()

# The "if/elif/else" logic is great for controlling the flow of a program, but it's
# somewhat of a "one-shot" thing.  What if we want to keep doing something while some
# condition is met?  Enter the "while" statement / keyword.
x = 1
while x <= 5:
    print(f"x is {x}")
    x = x + 1
pause_program()

# In short, while the condition after the "while" keyword evaluates to True, we'll
# keep repeating the indented block of code.  WARNING!  WARNING!  WARNING!  If you
# are not careful, you could get stuck in an infinite loop!!!  That might be what you
# want, but more often than not, that's not the case.

# Another Python keyword that is often seen within a "while" loop is the "break"
# keyword.  A "break" statement will break / exit the innermost (closest)
# enclosing while loop.  Here's another way of coding the above while loop:
x = 1
while True:
    if x <= 5:
        print(f"x is {x}")
        x = x + 1
    else:
        break

# Which is a "cleaner" way of coding?  The first one, as it clearly shows what
# condition causes the while loop to continue running.  In the second method,
# you have to go hunting for the logic that would cause the while loop to terminate.
# Cleaner code makes it easier for others to understand!!!


