from flask import Blueprint, jsonify, request

projects_api=Blueprint('projects_api', __name__)

@projects_api.route('/', methods=['GET'])
def get_all_projects():
    return jsonify("test for projects api")
# jsonify('{"projects": ...}') 会返回双重编码的 JSON。不可以，必须双引号英文

@projects_api.route('/<project_id>', methods=['GET'])
def get_project(project_id):
    data={'code':200,'data':"This is project id: "+project_id}
    return jsonify(data)

