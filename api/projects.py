from flask import Blueprint, jsonify, request

projects_api=Blueprint('projects_api', __name__)

@projects_api.route('/', methods=['GET'])
def get_projects():
    return jsonify("test for projects api")
# jsonify('{"projects": ...}') 会返回双重编码的 JSON。不可以，必须双引号英文


