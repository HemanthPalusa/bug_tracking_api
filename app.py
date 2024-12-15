from flask import Flask
import argparse

app = Flask(__name__)

from routes import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5000)

    args = parser.parse_args()

    app.run(debug=True, port=args.port)
