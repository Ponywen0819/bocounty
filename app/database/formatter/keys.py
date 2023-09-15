def get_keys_string(values: dict):
    string = '('
    for index, key in enumerate(values.keys()):
        if index != 0:
            string += ","
        string += f"{key}"
    string += ')'

    return string
