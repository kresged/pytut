#
# Lesson 03: Loops
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

# In python, there are really only 2 types of loops.  We covered one of them in Lesson 02,
# namely the "while" loop.  While the condition evaluates to True, keep doing whatever is
# inside the while loop.  Once the condition becomes False, the while loop ends and we move
# on to the next statement in our program.  A little refresher on the while loop and lists...

# Remember lists are enclosed with square brackets
numbers = [10, 2, 5, 1, 7, 6, 8, 3, 9, 4]

# Number to find in the list
find_number = 6
# position will keep track of where we are while traversing the list.  In programming,
# we usually call this an index (e.g. the number 10 is at index 0, 2 is at index 1)
position = 0
# How many numbers do we have in out list?  The len function will tell us this.
numbers_length = len(numbers)
print(f"Looking for number {find_number} in numbers list {numbers} with length {numbers_length} using while ...")
while position < numbers_length:
    if numbers[position] == find_number:
        print(f" Found number {find_number} at position {position} so breaking out of while loop")
        break
    else:
        print(f" Number {numbers[position]} at position {position} is not what we're looking for")
    position = position + 1
pause_program()

# Now let's introduce the for loop by attempting to do the same thing that we did with the while loop.
position = 0
print(f"Looking for number {find_number} in numbers list {numbers} with length {numbers_length} using for ...")
# In this for loop, item will be set to each value in the numbers list.  You can say that we're
# "walking the numbers list" one item at a time.
for item in numbers:
    if item == find_number:
        print(f" Found number {find_number} at position {position} so breaking out of for loop")
        break
    else:
        print(f" Number {item} at position {position} is not what we're looking for")
    position = position + 1
pause_program()

# Now I'll let you in on a little "secret."  In the above for loop code, we were keeping track of the position
# (index) so that we could display the position the number was found at.   Python can do that for us with the
# enumerate function, which will return both the position (index) *and* the item at that position.
print(f"Looking for number {find_number} in numbers list {numbers} with length {numbers_length} using enumerate ...")
for position, item in enumerate(numbers):
    if item == find_number:
        print(f" Found number {find_number} at position {position} so breaking out of for loop")
        break
    else:
        print(f" Number {item} at position {position} is not what we're looking for")
pause_program()

# We'll change the code above just a little bit to try to "loop over" a series of numbers that we'll try to find.
# In the above code, notice that we did not handle the case where the number is not found.  There are a few ways
# to do this, but I'm going to show you a way that works with the "break" statement.  We did not cover it last week,
# but there is actually an "else" statement that can be used with the while statement.  It is *only* run if the while
# loop did not exit as a result of a break statement being run.  Since we're using break when we find the number, we
# can use the else statement to print out a message when we don't find the number.
find_numbers = [6, 20]
for find_number in find_numbers:
    position = 0
    print(f"Looking for number {find_number} in numbers list {numbers} with length {numbers_length} using while ...")
    while position < numbers_length:
        if numbers[position] == find_number:
            print(f" Found number {find_number} at position {position} so breaking out of while loop")
            break
        else:
            print(f" Number {numbers[position]} at position {position} is not what we're looking for")
        position = position + 1
    else:
        print(f" Did not find number {find_number} in numbers list {numbers}")
    pause_program()

# Similarly, the for loop has the same else logic, just like while.  Let's use enumerate again as well.
for find_number in find_numbers:
    print(f"Looking for number {find_number} in numbers list {numbers} with length {numbers_length} using for ...")
    for position, item in enumerate(numbers):
        if item == find_number:
            print(f" Found number {find_number} at position {position} so breaking out of for loop")
            break
        else:
            print(f" Number {item} at position {position} is not what we're looking for")
    else:
        print(f" Did not find number {find_number} in numbers list {numbers}")
    pause_program()

# What if we didn't care about the position (index)?  Much shorter code...
for find_number in find_numbers:
    print(f"Looking for number {find_number} in numbers list {numbers} with length {numbers_length} using in test ...")
    if find_number in numbers:
        print(f" Found number {find_number}")
    else:
        print(f" Did not find number {find_number}")
    pause_program()

# In python, the for loop syntax really resembles the following:
#  for item in iterable:
#   statement(s)
#  [else: 
#   statement(s)]
#
# The brackets surrounding the else statement mean that the else statement is optional.  You'll
# see this sort of thing a lot in the programming world, so I just thought I'd mention it.
#
# What is an iterable?  An iterable is any python object that is capable of returning its members one at a time,
# permitting it to be iterated (walked) over in a for loop.  So far, we've covered 2 iterables -- lists and, drum roll
# please, strings!  What?!?  A string is iterable?  Let's check it out.
for item in "hello":
    print(f"{item}")
pause_program()

# As you can see, we get back the characters of a string, one at a time.  As time goes on, we'll run
# across more and more iterables.