def mask_json_values(json_values: dict | list, hidden_json_keys: list) -> dict:
    for key, value in json_values.items():
        if isinstance(value, dict):
            mask_json_values(value)
        elif isinstance(value, list):
            try:
                for item in value:
                    if key.lower() in hidden_json_keys:
                        json_values[key][item] = "*" * len(str(item))
                    mask_json_values(item)
            except Exception as e:
                for item in range(len(value)):
                    if key.lower() in hidden_json_keys:
                        json_values[key][item] = "*" * len(str(item))
        else:
            if key.lower() in hidden_json_keys:
                json_values[key] = "*" * len(str(value))
    return json_values


def mask_list_values(list_values: list | dict, hk: list) -> list:
    for item in list_values:
        if isinstance(item, dict):
            mask_json_values(item, hk)
        elif isinstance(item, list):
            mask_list_values(item, hk)
    return list_values
