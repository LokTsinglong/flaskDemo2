from flask import Flask

from api.projects import projects_api
from api.managers import managers_api
from api.staff import staff_api

app=Flask(__name__)
app.register_blueprint(projects_api, url_prefix='/projects')
app.register_blueprint(managers_api, url_prefix='/managers')
app.register_blueprint(staff_api, url_prefix='/staff')

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run('127.0.0.1',8000,debug=True)