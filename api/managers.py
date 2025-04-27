from flask import Blueprint, jsonify, request

managers_api=Blueprint('managers_api', __name__)

@managers_api.route('/', methods=['GET'])
def get_managers():
    return jsonify("test for managers api")