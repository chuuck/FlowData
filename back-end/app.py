from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET', 'POST'])
def ping_pong():
    data = request.json
    print (data)
    return jsonify(data)


if __name__ == '__main__':
    app.run()