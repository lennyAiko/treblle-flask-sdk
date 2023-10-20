from flask import request, Flask, jsonify
from .utils import (
    get_json_file,
    mask_json_values,
    mask_list_values,
    treblle_payload,
    send_payload,
    machine_info,
)
import datetime, json
from time import gmtime, strftime, time


class Treblle(object):
    __name__ = "Treblle"

    api_key: str
    project_id: str
    hidden_keys: list

    if get_json_file() is not None:
        api_key, project_id, hidden_keys = get_json_file()

    hidden_json_keys = [
        "password",
        "pwd",
        "secret",
        "password_confirmation",
        "passwordConfirmation",
        "cc",
        "card_number",
        "cardNumber",
        "ccv",
        "ssn",
        "credit_score",
        "creditScore",
    ]

    hidden_json_keys += hidden_keys

    start_request_time: int = 0
    response_body: dict = {}
    request_body: dict = {}
    server: dict = {"os": {}}
    keys: dict = {"api": api_key, "project": project_id}
    language: dict = {}
    errors: list = []

    def __init__(self, app: Flask | None = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        machine: dict = machine_info()
        if len(machine) < 4:
            self.errors.append("Incomplete machine")

        @app.before_request
        def get_request() -> None:
            self.start_request_time = time()
            self.server["ip"] = request.environ["SERVER_NAME"]
            self.server["timezone"] = strftime("%z", gmtime())
            self.server["software"] = request.environ["SERVER_SOFTWARE"]
            self.server["protocol"] = request.environ["SERVER_PROTOCOL"]
            self.server["os"]["name"] = machine["name"]
            self.server["os"]["release"] = machine["release"]
            self.server["os"]["architecture"] = machine["architecture"]
            self.language["version"] = machine["version"]
            self.request_body["method"] = request.method
            self.request_body["url"] = request.base_url
            self.request_body["user_agent"] = request.headers.get("User-Agent")
            self.request_body["ip"] = (
                request.headers.getlist("HTTP_X_FORWARDED_FOR").split(",")[0]
                if len(request.headers.getlist("HTTP_X_FORWARDED_FOR")) > 1
                else request.remote_addr
            )

            body = (
                request.get_data(as_text=True)
                if request.method == "GET"
                else mask_json_values(request.get_json(), self.hidden_json_keys)
            )

            self.request_body["body"] = (
                mask_json_values(body, self.hidden_json_keys)
                if isinstance(body, dict)
                else mask_list_values(body, self.hidden_json_keys)
            )
            self.request_body["headers"] = mask_json_values(
                json.loads(json.dumps({**request.headers})), self.hidden_json_keys
            )
            self.request_body["timestamp"] = datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            return

        @app.after_request
        def get_response(response):
            self.response_body["status_code"] = response.status_code
            headers = json.loads(json.dumps({**response.headers}))
            self.response_body["headers"] = mask_json_values(
                headers, self.hidden_json_keys
            )
            body = (
                response.get_json()
                if response.get_json()
                else response.get_data(as_text=True)
            )
            self.response_body["size"] = len(body)
            self.response_body["body"] = (
                mask_json_values(body, self.hidden_json_keys)
                if isinstance(body, dict)
                else mask_list_values(body, self.hidden_json_keys)
            )
            end_request_time = time()

            self.response_body["load_time"] = end_request_time - self.start_request_time

            payload = treblle_payload(
                keys=self.keys,
                server=self.server,
                language=self.language,
                request=self.request_body,
                response=self.response_body,
                errors=self.errors,
            )
            if payload is not False:
                send_payload(payload, self.api_key)
            return response


if __name__ == "__main__":
    Treblle()
