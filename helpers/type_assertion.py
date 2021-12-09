def type_assertion(object, required_type):
    actual_type = type(object)
    if actual_type != required_type:
        raise TypeError(object, "should be of type", required_type, ", got", actual_type)