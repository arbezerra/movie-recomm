from flask import Flask, request, jsonify
from flask_cors import CORS
from .recommender import Recommender
from .services import MovieService
from .routes import routes
from .util import auth


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

    @app.route('/recommend', methods=['POST'])
    def recomm():
        bearer = request.headers.get('Authorization')
        token = auth.verify(bearer)
        if not token:
            return {'message': 'Forbidden'}, 403
        return jsonify({"movies": recommender.recommend(token['id'])})

    app.register_blueprint(routes)

    return app
