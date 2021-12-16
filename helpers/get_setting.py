from helpers.type_assertion import type_assertion

def get_setting(setting):
    """
    Returns the setting in string format XX in a way that is compatible with
    EnigmaMachine constructors

    @param setting: int of the setting to encode
    @returns str of the setting in compatible format
    """

    # Function defense
    type_assertion(setting, int)

    if setting < 10:
        return "0" + str(setting)
    else:
        return str(setting)