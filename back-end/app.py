from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
from io import BytesIO
import openai
import os
import pandasql as ps
import json

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
@app.route("/upload-csv-test", methods=["POST"])
def upload_csv():
    print("receiving")
    file = request.files["file"]
    df = pd.read_csv(BytesIO(request.files['file'].read()))

    task = "Sort out all data by descending order using store sales."
    prompt = creates_message(list(df.columns), task)

    openai_response = api_request(prompt)
    retrieved_query = "SELECT" + openai_response["choices"][0]["text"]

    queried_table = ps.sqldf("SELECT * FROM df ORDER BY Store_Sales DESC")

    print (queried_table.to_json(orient="records"))

    if file:
        return (queried_table.to_json(orient="records"))
    else:
        return "No file found"


# Function that creates an API message
def creates_message(columns, task) -> str:

    message = "### SQL Tables, with their properties:\n#\n"

    column_properties = "("

    for idx, column in enumerate(columns):
        
        if (idx + 1 == len(columns)):
            column_properties += column
        else:
            column_properties += column + ", "

    table_name = "# " + "Stores" + column_properties + ")\n"

    message += table_name + "#\n### " + task + "\nSELECT"

    return (message)


def api_request(message):

    openai.api_key = "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"

    response = openai.Completion.create(
        model="code-davinci-002",
        prompt= message,
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["#", ";"]
    )

    return (response)




if __name__ == '__main__':
    app.run(port=8000)