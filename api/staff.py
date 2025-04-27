from flask import Blueprint, jsonify, request

staff_api=Blueprint('staff_api', __name__)

@staff_api.route('/', methods=['GET'])
def get_staff():
    return jsonify('Staff API')