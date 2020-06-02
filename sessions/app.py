import argparse
from flask import Flask, request, abort

import sklearn

from ie_nlp_utils.tokenization import tokenize as tokenize_sentence

app = Flask(__name__)


@app.route("/")
def hello():
    """Sample endpoint with GET parameters."""
    args = dict(request.args)
    # name = args.get("name")
    # if name:
    if name := args.get("name"):
        return f"Howdy, {name}!"
    else:
        return f"Hello, world!"


@app.route("/api/<int:version>")
def api(version):
    """Sample endpoints with dynamic URLs."""
    args = dict(request.args)
    return {
        "status": "ok",
        "name": args.get("name", "<NOT GIVEN>"),
        "version": version,
        "scikit-learn-version": sklearn.__version__,
    }


@app.route("/tokenize")
def tokenize():
    """Example with custom code and custom error status code."""
    args = dict(request.args)
    if sentence := args.get("sentence"):
        return {
            "tokens": tokenize_sentence(sentence),
            "sentence": sentence,
        }
    else:
        abort(400)


if __name__ == "__main__":
    # Use python app.py --help to showcase argument parsing
    parser = argparse.ArgumentParser(description="Sample Flask application")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    app.run(debug=args.debug)
