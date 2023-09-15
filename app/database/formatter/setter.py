def get_setter_string(values: dict):
    if values is None:
        return ''

    string = ''
    for index, key in enumerate(values.keys()):
        if index != 0:
            string += ", "
        string += f"{key} = "
        value = values.get(key)
        if type(value) == str:
            string += f"'{value}' "
        else:
            string += f"{value} "

    return string
