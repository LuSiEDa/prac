from flask import Flask
from flask_smorest import Api
from api import book_blp

flask_app = Flask(__name__)
# Flask-Smorest 설정 추가...

# API와 블루프린트 등록...
flask_app.config["API_TITLE"] = "Book API"
flask_app.config["API_VERSION"] = "v1"
flask_app.config["OPENAPI_VERSION"] = "3.1.3"
flask_app.config["OPENAPI_URL_PREFIX"] = "/"
flask_app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
flask_app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(flask_app)
	# Flask app 객체에 Api를 붙여주는 것.
api.register_blueprint(book_blp)

if __name__ == '__main__':
    flask_app.run(debug = True)

