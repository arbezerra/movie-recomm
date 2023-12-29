from flask import Flask, request, jsonify
from flask_cors import CORS
from app.recommender import Recommender
from .routes import routes


cors = CORS()
recommender = Recommender()


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config/__init__.py')
    app.json.ensure_ascii = False

    cors.init_app(app)

    @app.route('/healthz')
    def index():
        return {"status": "ok"}

    @app.route('/recommend', methods=['POST'])
    def recomm():
        state = request.json.get('state')
        return jsonify({"products": recommender.recommend(state)})

    app.register_blueprint(routes)

    return app
