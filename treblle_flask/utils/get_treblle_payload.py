import json

"""
Return a completed Treblle payload, that can be modified before being sent.
@param { dict } keys
@param { dict } server
@param { dict } language
@param { dict } request
@param { dict } response
@param { list } errors
@returns { dict } payload
"""


def check_items(items: list, error: list, name: str):
    for item in items:
        for k, v in item.values():
            if len(v) < 1:
                error.append(f"Incomplete {name} data")
    return error


def treblle_payload(
    keys: dict,
    server: dict,
    language: dict,
    request: dict,
    response: dict,
    errors: list,
) -> dict | bool:
    errors = check_items([keys, server, language, request, response], errors, "keys")

    payload: dict = {
        "api_key": str(keys["api"]),
        "project_id": str(keys["project"]),
        "version": 0.1,
        "sdk": "flask",
        "data": {
            "server": {
                "ip": server["ip"],
                "timezone": server["timezone"],
                "software": server["software"],
                "signature": "",
                "protocol": server["protocol"],
                "os": {
                    "name": server["os"]["name"],
                    "release": server["os"]["release"],
                    "architecture": server["os"]["architecture"],
                },
            },
            "language": {
                "name": "python",
                "version": language["version"],
            },
            "request": {
                "timestamp": request["timestamp"],
                "ip": request["ip"],
                "url": request["url"],
                "user_agent": request["user_agent"],
                "method": request["method"],
                "headers": request["headers"],
                "body": json.dumps(request["body"]),
            },
            "response": {
                "headers": response["headers"],
                "code": response["status_code"],
                "size": response["size"],
                "load_time": response["load_time"],
                "body": response["body"],
            },
            "errors": errors,
        },
    }

    if not keys["api"] or not keys["project"]:
        print("No API key or Project ID found")
        return False
    elif len(keys["api"]) < 32 or len(keys["project"]) < 16:
        print("Invalid API key or project ID")
        return False
    else:
        try:
            payload = json.dumps(payload)
        except Exception as e:
            payload["data"]["response"]["body"] = ""
            payload["errors"] = errors.append(e)
            payload = json.dumps(payload)
        return payload


if __name__ == "__main__":
    treblle_payload()
