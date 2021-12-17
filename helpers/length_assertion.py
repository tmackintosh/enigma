from helpers.type_assertion import type_assertion

def length_assertion(object, required_length):
    """
    Raises an error when an object doesn't have a specified length.
    Helpful for method defenses.

    @param: object, must be iterable (such as a list or string)
    @returns: nothing, throws when the length is not asserted
    """
    
    # Function defense
    type_assertion(required_length, int)
    actual_length = 0

    try:
        actual_length = len(object)
    except:
        raise ValueError("Object must be iterable, such as a string or list, got", type(object))
        
    if actual_length != required_length:
        raise ValueError(object, "should have length", required_length, ", got", actual_length)