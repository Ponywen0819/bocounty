def get_condition_string(condition: dict) -> str:
    if condition is None:
        return ''

    string = ''
    for index, key in enumerate(condition.keys()):
        if index != 0:
            string += "AND "

        string += f"{key} = "
        value = condition.get(key)
        if type(value) == str:
            string += f"'{value}' "
        else:
            string += f"{value} "

    return string
