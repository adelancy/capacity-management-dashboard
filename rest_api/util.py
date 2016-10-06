import json
from flask import make_response


def output_json(dict_data, code, headers=None):
    resp = make_response(json.dumps(dict_data), code)
    resp.headers.extend(headers or {})
    return resp


def handle_rest_error_response(error, api_name=None, status_code=500, code=None, headers=None):
    error_resp = error.message.get('_schema', None)
    if error_resp:
        error_resp = dict(errors=error_resp)
    else:
        error_resp = dict(errors=[dict(title=api_name, detail=error.message, code=code, status=status_code)])
    resp = make_response(json.dumps(error_resp), 500)
    resp.headers.extend(headers or {})
    return resp


def dasherize(text):
    return text.replace('_', '-')
