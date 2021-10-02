from flask import Response, jsonify

def invalid_route() -> Response:
    output = {"error":
              {"msg": "404 error: This route is currently not supported. See API documentation."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 404
    return resp


