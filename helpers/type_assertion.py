def type_assertion(object, required_type, can_be_none = False):
    actual_type = type(object)
    if actual_type != required_type and not (object is None and can_be_none):
        raise TypeError(object, "should be of type", required_type, ", got", actual_type)