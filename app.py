from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


@app.get("/")
def index():
    return jsonify(message="Hello, CI!"), 200


@app.get("/test")
def test():
    return jsonify(message="This is a test endpoint!"), 200


if __name__ == "__main__":
    # For local runs: uvicorn/gunicorn is better for prod, but this is fine for demo.
    app.run(host="0.0.0.0", port=5001, debug=True)
