def is_even(number):
    string = str(number)
    for character in string:
        if int(character) % 2 != 0:
            return False

    return True