def type_assertion(object, required_type, can_be_none = False):
    """
    Asserts the type of an object.

    @param: object, the object to assess
    @param: required_type, the type object must be
    @param: can_be_none, whether the object can be a None object

    @returns nothing, throws on assertion error
    """
    
    actual_type = type(object)
    if actual_type != required_type and not (object is None and can_be_none):
        raise TypeError(object, "should be of type", required_type, ", got", actual_type)