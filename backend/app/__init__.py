from flask import Flask, request, jsonify
from flask_cors import CORS
from .recommender import Recommender
from .services import MovieService
from .routes import routes


cors = CORS()
recommender = Recommender()


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config/__init__.py')
    app.json.ensure_ascii = False

    cors.init_app(app)
    recommender.init_app(MovieService)

    @app.route('/healthz')
    def index():
        return {"status": "ok"}

    @app.route('/recommend/<user_id>', methods=['GET'])
    def recomm(user_id):
        return jsonify({"movies": recommender.recommend(user_id)})

    app.register_blueprint(routes)

    return app
