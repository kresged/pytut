#
# Lesson 01:
#  Comments
#  Variables (introduction)
#  Print (introduction)
#

# This is a comment in Python.  It is good to comment your code!
# Just make the first non-blank character on the line a '#' (pound, hash, or whatever
# you'd like to call it).  For multi-line comments like this one, just keep starting
# lines with a '#'.

# I'm going to define a little helper function that will allow me to pause/resume the
# program while I'm doing the presentation.  Don't worry about this for now.  If you
# are running this program in "non-presentation" mode, then set PRESENTATION_MODE to False.
PRESENTATION_MODE = True
def pause_program():
    print()
    if PRESENTATION_MODE:
        enter_key = input("*** Program paused.  Press Enter key to resume...")
    print("*" * 80)
    print()
        
# Let's define a variable
team_name = 'Coders R Us'

# That was easy!  The variable is on the left hand side of the equal sign, and
# we assigned it to the string 'Coders R Us'.  We'll talk more about
# strings at a later date, but they should be enclosed in either '' or "".

# Can we name our variables whatever we'd like?  Almost.  Most languages
# have reserved words, or keywords, that cannot be used as variable names.
# Python's list of keywords is not that long and can be found under the Keywords
# section at: https://docs.python.org/3/reference/lexical_analysis.html
#
# Here's the list:
#
# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield
#
# Don't worry about what all of these keywords mean yet, just know that
# you should stay away from them for variable names!

# Python does have some general guidelines though.  For now, we'll just
# stick with the following:
#  1. Start with a letter or underscore (_).  At this moment in time,
#     just stick with starting with a letter, even though underscores
#     are allowed.
#  2. Follow with any number of letters, digits, or underscores.

# Be aware that variable names *are* case sensitive, so the following
# variable is completely different from the one defined above!
team_Name = 'Coders R Us '

# To convince ourselves of that, let's display (print) both variables.
# We'll talk more about the print function at a later time.  Note how
# I enclosed the {} in parentheses ().  This is a nice programmer trick
# that can be used to see "white space" - see the space at the end
# of team_Name above?  If we didn't enclose it in parentheses (or some
# other pairing like <> or ||), we'd never know from the print statement
# that there was a space lurking at the end of the line.
print("team_name = ({})".format(team_name))
print("team_Name = ({})".format(team_Name))
pause_program()

# All variables must first be set before attempting to use them.
# If you try to use a variable that has not been previously assigned,
# Python will stop running your code and exit with a nice error message.
# So that our code does not exit here, I'm doing a little bit of
# advanced coding to catch Python's exception message and carry on.
# Don't try to understand this yet -- just know that had I not done this,
# the "print(team_location)" statement would have crashed our program!
try:
    print(team_location)
except NameError as ex:
    print("Caught {} exception: {}".format(type(ex).__name__, ex))
    print("Gracefully recovering from our mistake!")
pause_program()

# Can we assign things other than strings to variables?  Sure.
# Lots of other things.  Let's assign some numbers.
x = 2
y = 3

# Can we use a variable on the right hand side of the equal sign?  Yep.
sum = x + y

# Care to guess what 'sum' is set to at the moment?  You guessed it... 5.
print("{} + {} = {}".format(x, y, sum))
pause_program()

# So Python "magically" seems to know that team_name is a string and
# sum is a number (technically an integer in the "computer world").
# What happens if we try to divide an integer by a string?
# Again, I know that Python won't be happy with this, so I'll catch
# the exception so that we can move on.
try:
    result = sum / team_name
except TypeError as ex:
    print("Caught {} exception: {}".format(type(ex).__name__, ex))
    print("Gracefully recovering from our mistake!")
pause_program()

# But can other "mathematical" operations be performed with strings?
# Yes.

# Addition turns into something we call concatenation...
combined_string = "Hello " + "everybody!" 
print(combined_string)

# Like regular math, multiplication is a series of additions...
repeated_string = "Nyuk " * 3
print(repeated_string)
pause_program()

# Can we ask Python what type it thinks a variable is?  Sure.
# Again, don't dwell on the details, just know that Python is keeping
# track, as you saw above.
print("sum has the type: {}".format(type(sum).__name__))
print("team_name has the type: {}".format(type(team_name).__name__))
pause_program()

# Geeky Note: Python is what's known as a dynamically typed language.  Python
# doesn't know about the type (string, integer, etc.) of the variable until it's
# "dynamically" assigned when the code is run!  As proof of this, let's
# change what sum is from an integer to a string simply by assigning it a new value.
sum = "I once was an integer, but now I am a string"
print("sum has been reassigned and now has the type: {}".format(type(sum).__name__))
pause_program()

# Is that good coding?  In general, no, but the point is that it can be done.  It also goes to
# show you that you should name your variables something that makes sense.  If I saw the
# variable name 'sum' in someone's code, I'd guess that it was probably holding the
# result of some addition (like our original x + y).  I would not expect it to be a string.
# Remember... not only does naming your variable something that makes sense help you out
# when you're trying to understand your own code, it helps others as well!

# We've been using it above, but the print function is a pretty invaluable tool when
# learning to code or for debugging.  Even this seemingly simple function can take a while
# to master.  For some of the gory details, see section 7.1 at:
#  https://docs.python.org/3/tutorial/inputoutput.html
# We'll cover a few basic things now.

# If you list multiple arguments to the print function separated by commas,
# print will automatically separate them by a space.
print("This", "is", "a", "string", "with", "spaces")
pause_program()

# But what if we want print to separate by something other than a space?
# Use the 'sep' argument.
print("123", "456", "789", sep="|")
pause_program()

# In all of our print statements above, the print function automatically added a
# "new line" at the end.  What if we don't want that?
# Use the 'end' argument.
print("Two", "print", "calls", end=' ')
print("but only one line of output")
pause_program()

# Printing strings is fairly straight-forward.  What if we want to start printing
# variables?  If you read over enough Python code, you're going to see that there are
# 3 major ways of doing this.

# Method 1 - "Old string formatting".  Old timers like me are very comfortable with
# this method, since it originates from the sprintf function in the C programming
# language, which was the first "big" programming language many, many years ago.
# When a % sign is encountered in the string, it carries special meaning.  Here's
# an example where we'll print a string (%s) and a number (%d).  In short, each
# % sign in the string should be "paired up" with a corresponding entry in the () tuple.
print("%s is %d" % ("x", x))
pause_program()

# Method 2 - "str.format()".  This is the format that I used in the bulk of my
# print functions above.  Instead of a % sign like method 1, curly braces {} carry special
# meaning in this method.
print("{} is {}".format("x", x))
pause_program()

# However, there is no requirement for things to be "paired up" like in method 1.
# If you put a number in the curly braces, then it refers to the position of the
# argument to the format() method.  It may seem strange, but positions start at 0, which
# is something you'll encounter a lot in computer programming.  So get used to it!  :-)
print("{0} is {1}".format("x", x))

# Is this the same?
print("{1} is {0}".format(x, "x"))
pause_program()

# And if we use numbers in the curly braces, do things need to be "paired up" from a counting
# standpoint?  Here's an example with 3 pairs of braces yet only 1 argument in the
# format method.  Just so happens that all 3 pairs of braces reference the same thing!
print("{0} {0} {0}".format("Nyuk"))
pause_program()

# Although some of this may be a bit much for a beginner, the following web site shows
# some examples of methods 1 and 2.  Don't try to make sense of everything (yet).
#  https://pyformat.info/

# Method 3 - "Formatted string literals (f-strings)".  This is the newest method, introduced in
# Python 3.6.  So, for the EV3, which has Python 3.4.0 if you use Lego's image, you
# can't use this!  Consider yourself forewarned!!!  Similar to method 2, this one
# relies on curly braces {} again, and the string should be prefixed with an 'f' (hence the
# term 'f-strings').  What's inside the curly braces is really an expression that is
# evaluated while the code is running.

# In this case, the expression is just a variable.
print(f"x is {x}")

# But it could be any valid Python expression...
print(f"I think 2 + 3 is {2+3}")

# Including calling a method
print(f"{team_name.lower()} is team name in lower case")

# To learn more about f-strings by example, visit:
#  https://www.datacamp.com/community/tutorials/f-string-formatting-in-python
