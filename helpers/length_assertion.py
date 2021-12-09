def length_assertion(object, required_length):
    actual_length = len(object)
    if actual_length != required_length:
        raise ValueError(object, "should have length", required_length, ", got", actual_length)