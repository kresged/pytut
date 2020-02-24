#
# Lesson 04: Dictionaries (introduction)
#
import os
import sys

# Please see the comments in Lesson 04's binsearch_game.py that explain what these next
# couple of lines are doing.
program_base = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.insert(0, os.path.dirname(program_base) + os.sep + 'libs')

from UserInput import pause_input, print_asteriks

PRESENTATION_MODE = True
if PRESENTATION_MODE:
    pause_program = pause_input
else:
    pause_program = print_asteriks

# We have covered lists, but lists are not quite the greatest things for associating a
# key with a value.  For instance, let's say that we want to form a basket of fruits, and we want to
# store how many of each fruit we have in the basket.  The fruits are the keys, and the count of each
# fruit is the value for that key.  Let's do this with lists.
fruits = ['bananas', 'peaches', 'apples', 'cherries', 'pears']
counts = [3,         5,         2,        10,         4]

# We used 2 different lists, one to hold the fruits, and one to hold the count of each fruit.  What are the steps
# for figuring out how many of any given fruit we have?
for fruit_to_find in ["apples", "oranges"]:
    # 1. Look up the fruit to get its index (position in the list).  But we need to be careful, because if
    # the fruit is not found, Python will raise an exception (so we need to catch that exception).
    try:
        index = fruits.index(fruit_to_find)
        print(f"Found {fruit_to_find} at position {index}")
    except ValueError:
        # Set index to a negative number to indicate that we did not find any apples
        index = -1
        print(f"Did not find {fruit_to_find}")

    # 2. If we found the fruit's index, then we can retrieve the value at the same index in the counts list
    # to see how many of that fruit we have.
    if index != -1:
        print(f"We have {counts[index]} of {fruit_to_find}")

pause_program()

# Another weakness of using lists like this is that we first have to look for the item.  What happens if we have a list of 100 million items?
# If we wanted to efficiently find something, we'd better keep it in sorted order, and we better use a binary search algorithm (like the one in
# the binsearch_game) to look for our item.  What a pain!  That's just too much work for a programmer, and programmers are lazy!!!

# Maintaining 2 lists to associate a key with a value seems like a pain, and indeed, it is.  Surely there must be a better way!
# Enter dictionaries (also known as associative arrays in some programming languages).  Python's dictionaries use {} (remember, lists use []).
# Let's create a "basket" dictionary, initialized with the same values as the 2 lists above.  It consists of comma-separated key:value pairs.
basket = {'bananas': 3, 'peaches': 5, 'apples': 2, 'cherries': 10, 'pears': 4}

# Let's print out the dictionary.  Before Python 3.6, dictionaries were not in any order.  Beginning with Python 3.6, they are now in "insertion order", meaning
# that the order that you insert items into them is the order that they stay in.  Not all programming languages are like this (and Python wasn't before 3.6), so
# be aware if you eventually start using dictionaries in other programming languages.  Personally, I don't think I can recall a situation where I
# depended on the ordering of items in a dictionary (for what it's worth).
print(basket)

# Recall from lesson 1 that Python is tracking the types of all variables.  The "basket"
# variable happens to be of type dict.  Let's ask Python (don't dwell on the details).
print("basket has the type: {}".format(type(basket).__name__))

pause_program()

# Can we easily add more items?  Yep.  Strangely, Python goes back to using [] for this purpose.  But in this context, [] does *not* mean list!!!
basket['kiwis'] = 6

# Notice how kiwis is put at the end of the dictionary (insertion order)
print(basket)

pause_program()

# Unlike lists, dictionaries are very efficient for lookups.  Much like the assignment above, we can use the basket[fruit] syntax to retrieve the
# value.  And the cool thing is that we didn't have to go writing any code for binary search lookups or the like.  We get it for "free" using
# dictionaries.
for fruit_to_find in ["apples", "oranges"]:
    if fruit_to_find in basket:
        print(f"Found {fruit_to_find} count {basket[fruit_to_find]}")
    else:
        print(f"Did not find {fruit_to_find}")

pause_program()

# Can we loop over dictionaries?  You bet.

# Get the keys (fruits)
for fruit in basket.keys():
    print(f"Key {fruit} value {basket[fruit]}")

pause_program()

# Just get the values (counts)
for count in basket.values():
    # Note that there's no way to get the keys (fruits) as well when you use values()
    print(f"value {count}")

pause_program()

# Get both the key and value
for fruit, count in basket.items():
    print(f"Key {fruit} value {count}")

pause_program()

# Delete a key.  If you don't want to get an exception, you should always test to see if the key is in the dictionary first.
print(f"Before delete: {basket}")
if "bananas" in basket:
    del(basket["bananas"])
print(f"After delete: {basket}")

# Some coders cheat and use the pop method to eliminate the need to test for the key (remember - coders are lazy).
# We deleted bananas above.  Let's do it again.  Warning!  If you don't want Python to raise an exception for a missing
# key, you must list the second argument to the pop method, which is the value Python will return if the key is not found.
# If the key is found, Python will return its value as well as delete the key.
basket.pop("bananas", None)

# Similar to lists, we can use the len function to see how many keys are in the basket
print(f"Number of keys in basket: {len(basket)}")

# Which is important if you want to retrieve via popitem an item from a dictionary.  If you attempt it on an empty
# dictionary, you'll get a "KeyError: 'popitem(): dictionary is empty'" exception.  In Python 3.7 and later, the last
# item inserted is the one popped; before 3.7, a random item was popped instead.
if (len(basket)):
    key, val = basket.popitem()
    print(f"popitem returned key {key} value {val}")

pause_program()

# Similar to pop, there is also a get method that will return the value for a given key.  And if the key is not found,
# Python will by default return None rather than raising a KeyError exception.
num_bananas = basket.get("bananas")
if num_bananas is None:
    print("Did not find any bananas")

# But we can also pass in a value to return instead of the default None.
num_bananas = basket.get("bananas", 0)
print(f"Found {num_bananas} bananas")

# Be careful with this though -- does this mean that the dictionary has the key bananas and it was set to 0?  Or does the dictionary
# have the key bananas at all?  It is best to use a value to return that would not be a valid value.  For instance, sticking with the
# default None might make more sense in this case, or maybe returning -1 instead (how could we have -1 bananas, so that would be a
# good indicator that the key bananas is not present).  Or maybe we don't care about the distinction, in which case it doesn't really matter.
pause_program()

# Similar to lists, we can "sort" dictionaries.  In this case, Python will sort by the keys, which in this case happen to be all strings.
# You'll get back a list of the sorted keys (which is why I put "sort" in quotes above - the dictionary itself is not sorted, but rather you
# get a new list returned back to you with the sorted keys of the dictionary).
for fruit in sorted(basket):
    print(f"Key {fruit} value {basket[fruit]}")

# If you want to learn more about dictionaries, see section 5.5 at https://docs.python.org/3/tutorial/datastructures.html#dictionaries or
# https://www.w3schools.com/python/python_dictionaries.asp.  There are lots more resources out there - just Google "Python Dictionaries".