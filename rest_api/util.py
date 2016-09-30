import json
from flask import make_response


def output_json(dict_data, code, headers=None):
    resp = make_response(json.dumps(dict_data), code)
    resp.headers.extend(headers or {})
    return resp
