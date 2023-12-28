from flask import Flask, request, jsonify
from flask_cors import CORS
from recommender import Recommender

cors = CORS()
recommender = Recommender()


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    cors.init_app(app)

    @app.route('/healthz')
    def index():
        return "ok"

    @app.route('/recomm', methods=['GET', 'POST'])
    def recomm():
        state = request.json.get('state')
        return jsonify({"products": recommender.recommend(state)})

    return app
