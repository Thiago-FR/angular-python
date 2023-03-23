from flask import Flask
from .routes.user_router import user
from flask_cors import CORS


# def create_app():
#     app = Flask(__name__)
#     CORS(app)
#     app.register_blueprint(user)

#     return app

app = Flask(__name__)
CORS(app)
app.register_blueprint(user)

if __name__ == "__main__":
    app.run(debug=True)
