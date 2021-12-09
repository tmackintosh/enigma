def lexigraphical_range_assertion(object, minimum_value, maximum_value):
    if ord(object) < ord(minimum_value) or ord(object) > ord(maximum_value):
        raise TypeError("Should be between", minimum_value, "and", maximum_value, ", got", object)