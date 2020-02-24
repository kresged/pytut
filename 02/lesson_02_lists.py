#
# Lesson 02:
#  Lists (introduction)
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

# Think of a List as a collection of objects (things).  In everyday life, we use
# Lists for lots of things - a shopping list, a to-do list, etc.  Lists in Python
# are written as a comma-separated series of values enclosed in square brackets.

# We can create an empty list
fruits = []

# And then we can add objects to the list with the append method, which puts the object at
# the end of the list.
fruits.append("pear")
fruits.append("banana")
fruits.append("apple")

print("fruits:", fruits)
pause_program()

# Notice how Python displayed the fruits as a comma-separated series of values in
# square brackets.  We could have set/initialized the fruits List in a similar fashion
# as to how Python displayed our fruits List:
fruits = ['pear', 'banana', 'apple']

print("fruits:", fruits)
pause_program()

# Recall from lesson 1 that Python is tracking the types of all variables.  The "fruits"
# variable happens to be of type list.  Let's ask Python (don't dwell on the details).
print("fruits has the type: {}".format(type(fruits).__name__))
pause_program()

# As mentioned in lesson 1 when we were discussing the str.format() method for
# printing, lots of things in programming start at index / offset 0.  The first
# position in a List is index / offset 0.
print("First item in the list is at position 0:", fruits[0])

# We can get the length of the List using the len function
print("The fruits list has {} items".format(len(fruits)))

pause_program()

# What if we wanted to insert something at the beginning of the List?
fruits.insert(0, "kiwi")
print("fruits:", fruits)
pause_program()

# The insert method is actually pretty generic in that we can insert an object
# at a specific index / offset.  The rest of the objects will "move right" in the list.
fruits.insert(1, "cherry")
print("fruits:", fruits)

pause_program()

# Note that a List can have the same object more than once
fruits.insert(0, 'apple')
print("fruits:", fruits)

# How many apples do we have?
print("We have {} apples".format(fruits.count("apple")))

# How many oranges do we have?
print("We have {} oranges".format(fruits.count("orange")))

pause_program()

# We'll cover the if statement at a later time, but you can also test if
# something is in a List with the 'in' keyword:
if 'cherry' in fruits:
    print("Yes!  We have a cherry in our List.")

# And we can test for the absence of something as well with 'not in':
if 'orange' not in fruits:
    print("Sorry, an orange was not found in our List.")

pause_program()

# Let's remove one of those apples.  The remove method will delete the first
# occurrence only.
print("Before removing first apple", fruits)
fruits.remove('apple')
print("After removing first apple", fruits)
pause_program()

# But don't attempt to remove something that's not in the List.  If you do,
# you'll get an exception.  Similar to lesson 1, so that we don't die here,
# we'll catch Python's exception and move on.
try:
    fruits.remove("orange")
except ValueError as ex:
    print("Caught {} exception: {}".format(type(ex).__name__, ex))
    print("Gracefully recovering from our mistake!")
pause_program()

# Lists are unordered - unless we give them some order.  We can use the sort method
# to sort our List.  Note that sort will change the List in-place.
fruits.sort()
print("After sorting:", fruits)
pause_program()

# By default, sort will sort in ascending order.  But we can ask for the List to
# be sorted in reverse (descending) order.
fruits.sort(reverse=True)
print("After sorting in reverse:", fruits)
pause_program()

# Since all the values in the List were strings, Python performed a dictionary like
# sort (alphabetic).  Technically, Python performed a lexographic sort.  This is a
# bit advanced for now, but we can actually ask Python to sort using a custom
# function that we pass in with the 'key' argument.  Let's sort by string length,
# using the 'len' function that we previously used to get the length of our List.
fruits.sort(key=len)
print("After sorting by string length", fruits)

# The above methods are not the only methods that can be used on Lists.  There are
# a few others (e.g. reverse(), index(), pop(), clear(), copy(), etc.).  See section 5.1
# here: https://docs.python.org/3/tutorial/datastructures.html.









