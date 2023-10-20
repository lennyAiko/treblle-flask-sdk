import os, json

"""
Fetch json file to extract keys

@returns { list }
"""


def get_json_file() -> list:
    path = os.getcwd() + "\\treblle.json"

    f = open(path, "r")
    treblle: dict = json.load(f)
    f.close()

    api_key = str(treblle["TREBLLE_API_KEY"])
    project_id = str(treblle["TREBLLE_PROJECT_ID"])
    hidden_keys = treblle["TREBLLE_HIDDEN_KEYS"]

    if not api_key or not project_id:
        print("No api key or project id found in treblle.json")
        return None

    if isinstance(hidden_keys, list):
        hidden_keys = list(x.lower() for x in hidden_keys)
        return api_key, project_id, hidden_keys
    else:
        print("TREBLLE_HIDDEN_KEYS should be a list")
        hidden_keys = []
        return api_key, project_id, hidden_keys


if __name__ == "__main__":
    get_json_file()
