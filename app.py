from flask import Flask

from api.projects import projects_api
from api.managers import managers_api
from api.staff import staff_api
from api.login import login_api

from flask_migrate import Migrate
from flask_cors import CORS

app=Flask(__name__,static_folder='img')
app.register_blueprint(projects_api, url_prefix='/projects')
app.register_blueprint(managers_api, url_prefix='/managers')
app.register_blueprint(staff_api, url_prefix='/staff')
app.register_blueprint(login_api, url_prefix='/login')
app.secret_key = "my-secret-key-123" 

CORS(app,
    resources={r"/*": {"origins": "http://localhost:8080"}},  # 仅允许前端开发地址
    supports_credentials=True  # 允许携带 Cookie
    )

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/flask_test'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)

from models import db
db.init_app(app)

migrate = Migrate(app, db)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run('127.0.0.1',8000,debug=True)