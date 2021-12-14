def get_setting(setting):
    if setting < 10:
        return "0" + str(setting)
    else:
        return str(setting)