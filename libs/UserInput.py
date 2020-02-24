def get_integer(minInt=None, maxInt=None, minInclude=True, maxInclude=True, prompt=None):
    """
    Get an integer response from the user via a call to input.

    minInt - minimum integer (if desired - defaults to None)
    maxInt - maximum integer (if desired - defaults to None)
    minInclude - whether or not to include minInt itself in the range (defaults to True)
    maxInclude - whether or not to include maxInt itself in the range (defaults to True)
    prompt - custom prompt (if desired - defaults to None, but a prompt will be printed
             even if None)

    Returns the integer retrieved from the user.
    """

    input_str = prompt
    conditions = ""

    if minInt is not None:
        if type(minInt) is not int:
            raise ValueError("minInt must be an integer if specified")
        if minInclude:
            conditions += f">= {minInt}"
        else:
            conditions += f"> {minInt}"

    if maxInt is not None:
        if type(maxInt) is not int:
            raise ValueError("maxInt must be an integer if specified")
        if minInt is not None:
            conditions += " and "
        if maxInclude:
            conditions += f"<= {maxInt}"
        else:
            conditions += f"< {maxInt}"

    if input_str is None:
        input_str = "Enter integer"
        if conditions != "":
            input_str += f" {conditions}"
            input_str += ": "
    elif type(input_str) is not str:
        raise ValueError("prompt must be a string if specified")
        
    ret = None
    while ret is None:
        try:
            user_int = int(input(input_str))
            if minInt is not None:
                if minInclude:
                    if user_int < minInt:
                        raise ValueError("Too Low")
                else:
                    if user_int <= minInt:
                        raise ValueError("Too Low")
            if maxInt is not None:
                if maxInclude:
                    if user_int > maxInt:
                        raise ValueError("Too High")
                else:
                    if user_int >= maxInt:
                        raise ValueError("Too High")
            ret = user_int
        except ValueError as ex:
            print(f"ERROR - {ex} - Please enter integer", end="")
            if conditions:
                print(f" {conditions}")
            print()

    return ret

def get_choice(prompt=None, choices=None):
    """
    Get a string response from the user via input with the desired choices.

    prompt - custom prompt (if desired - defaults to None, but a prompt will be printed
             even if None)
    choices - list of choices that user must select from.  A non-empty list is required!

    Returns: the user's choice as a string.
    """

    if prompt is None:
        prompt = "Please enter your choice"
    elif type(prompt) is not str:
        raise ValueError("prompt must be a string if specified")

    if (type(choices) is not list) or (len(choices) == 0):
        raise ValueError("choices must be a non-empty list")

    # Join choices with a slash for display to the user
    choices_joined = "/".join(choices)
    prompt += f" [{choices_joined}] "

    ret = None
    while ret is None:
        response = input(prompt)
        if response in choices:
            ret = response
        else:
            print(f"Error - Invalid Entry - Please enter one of {choices_joined}")

    return ret

def get_yes_no(prompt=None):
    """
    Get a yes/no response from the user.

    prompt - custom prompt (if desired - defaults to None, but a prompt will be printed
             even if None)

    Returns - True (for yes), False (for no)
    """
    if get_choice(prompt, ['y','n']) == 'y':
        return True
    else:
        return False

def pause_input():
    print()
    input("*** Program paused.  Press Enter key to resume...")
    print("*" * 80)
    print()

def print_asteriks():
    print()
    print("*" * 80)
    print()

