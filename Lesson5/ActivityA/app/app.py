from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to The API!'})

@app.route('/hello/<string:name>', methods=['GET'])
def hello(name):
    message = 'Hello, {}. Welcome to The API'.format(name)
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
