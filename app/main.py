import logging
import os

from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()

app = Flask(__name__)

log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=log_level,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


@app.before_request
def log_request():
    from flask import request
    logger.info("Request received: %s %s", request.method, request.path)


@app.route("/")
def home():
    return jsonify({
        "application": "Taskflow",
        "message": "Welcome to Taskflow API",
    })


@app.route("/health")
def health():
    logger.info("Health check successful")
    return jsonify({
        "status": "healthy",
        "application": "taskflow",
    }), 200



@app.route("/tasks")
def list_tasks():
    tasks = [
        {
            "id": 1,
            "title": "Learn Git",
            "completed": False,
        },
        {
            "id": 2,
            "title": "Build Taskflow API",
            "completed": False,
        },
    ]

    logger.info("Tasks list requested")

    return jsonify({"tasks": tasks}), 200



if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
