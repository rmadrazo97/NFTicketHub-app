from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message='Hello, World!')

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"data": "This is sample data from the API."}
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    if request.is_json:
        data = request.get_json()
        return jsonify(data), 201
    else:
        return jsonify(error="Request must be JSON."), 400

if __name__ == '__main__':
    app.run(debug=True)
