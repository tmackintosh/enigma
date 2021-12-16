def swap_characters(string: str, a, b):
    new_string = string

    index = string.index(a)
    new_string = new_string[:index] + b + new_string[index + 1:]

    index2 = string.index(b)
    new_string = new_string[:index2] + a + new_string[index2 + 1:]

    return new_string