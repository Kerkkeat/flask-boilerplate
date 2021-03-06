from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/')
def root():
    return "Working"

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=5000)