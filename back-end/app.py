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

# getting csv file from front-end
@app.route('/csvuploader', methods=['GET', 'POST'])
def csv_uploader():
    file = request.files['file']
    if not file:
        return "No file"
    else:
        print ("asdasd")
        return "Success"
    return jsonify(data)



if __name__ == '__main__':
    app.run()