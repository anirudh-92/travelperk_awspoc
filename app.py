import socket

import flask


def create_app():
    app = flask.Flask(__name__)

    @app.route('/health')
    def base_healthcheck_route():
        return {"message": "flask is operational", "error": False}, 200

    @app.route('/')
    def index():
        message = f"Hello from {socket.gethostname()}"
        return {"message": message}, 200

    return app

def main():
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=80)


if __name__ == "__main__":
    main()
