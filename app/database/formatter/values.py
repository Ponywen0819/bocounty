def get_values_string(values: dict):
    string = "("
    for index, val in enumerate(values.values()):
        if index != 0:
            string += ","
        if type(val) == str:
            string += f"'{val}'"
        else:
            string += f"{val}"
    string += ")"

    return string
