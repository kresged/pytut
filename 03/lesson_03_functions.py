#
# Lesson 03: Functions (introduction)
#

# I'm going to define a little helper function that will allow me to pause/resume the
# program while I'm doing the presentation.  Don't worry about this for now.  If you
# are running this program in "non-presentation" mode, then set PRESENTATION_MODE to False.
PRESENTATION_MODE = False
def pause_program():
    print()
    if PRESENTATION_MODE:
        input("*** Program paused.  Press Enter key to resume...")
    print("*" * 80)
    print()

# In both this lesson and in the prior lessons, you've seen me both define and use a function.
# The pause_program code above is a function.  Functions are defined with the "def" keyword, a
# function name (which actually becomes a variable), and parenthesis ().  Interesting fact - functions
# are actually objects that are assigned a variable name!

# Hey python, what is pause_program?
print("pause_program has the type: {}".format(type(pause_program).__name__))
pause_program()

# And like all variables, they can be reassigned (not that you'd want to do this, but...).
# Save a reference to pause_program so that we can restore it.
save_pause_program = pause_program

pause_program = "Now I'm a string"
print("pause_program now has the type: {}".format(type(pause_program).__name__))
print(pause_program)

print("restoring pause_program back to a function")
pause_program = save_pause_program

pause_program()

# Like all variables, functions must be defined before we can use them!  I know this
# will bomb out, so I'm going to catch the exception so that we can gracefully move on.
# Note that NameError is the same exact error message that's thrown if you attempt to
# use a variable before you define it!  Well, function names are variables, so...
x = 2
try:
    print(f"x ({x}) squared is", squared(x))
except NameError as ex:
    print("Caught {} exception: {}".format(type(ex).__name__, ex))
    print("Gracefully recovering from our mistake!")
pause_program()

# Functions can take arguments (parameters) and can also return value(s).
def squared(num):
    return num*num

print(f"x ({x}) squared is", squared(x))
pause_program()

# Let's take multiple arguments
def add(x, y):
    return x+y

y = 3
print(f"x ({x}) + y ({y}) = {add(x,y)}")
pause_program()

# And let's return multiple values, which is done by comma separating the return values.
# Technically, in this context, a comma separated return value is a tuple, which is another
# data type that we have not covered yet.
def square_and_cube(num):
    return num*num, num*num*num

# If multiple values are returned, we can use multiple comma separated variables to capture the
# returned values.
sq, cb = square_and_cube(x)
print(f"x ({x}) squared {sq} cubed {cb}")
pause_program()

# But to convince ourselves that square_and_cube does really return a tuple, let's assign the
# return value to a single variable.
ret_tuple = square_and_cube(x)
print("ret_tuple has the type: {}".format(type(ret_tuple).__name__))

# tuples are somewhat like lists in that you can use offsets (indexes) to extract items...
print(f"x ({x}) squared {ret_tuple[0]} cubed {ret_tuple[1]}")

# but unlike lists, you can't modify the items.  In geek speak, we say they are immutable (unable to be changed).
# Since I know python will bomb out, we'll catch the exception.
try:
    ret_tuple[0] = 16
except TypeError as ex:
    print("Caught {} exception: {}".format(type(ex).__name__, ex))
    print("Gracefully recovering from our mistake!")
pause_program()

