from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
from io import BytesIO
import openai
import os
import pandasql as ps
import json
import re

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Dictionary of all tables storing the name of table and pandas dataframe
table_dict = {}

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

    file_list = request.files.getlist('file')

    for data_file in file_list:
        df = pd.read_csv(BytesIO(data_file.read()))
        table_dict[data_file.filename.replace(".csv", "")] = df


    prompt = request.form["prompt"]
    
    #print (f"This is the prompt: {prompt}")

    openai_prompt = create_message(prompt)
    print (openai_prompt)

    openai_response = api_request(openai_prompt)
    retrieved_query = "SELECT" + openai_response["choices"][0]["text"]

    queried_table = ps.sqldf("SELECT * FROM df ORDER BY Store_Sales DESC")

    #print (queried_table.to_json(orient="records"))

    response = {
        "table": queried_table.to_json(orient="records"),
        "query": retrieved_query
    }

    return (response)



# Function that creates an API message
def create_message(task) -> str:

    message = "### SQL Tables, with their properties:\n#\n"

    for key in table_dict:

        column_properties = "("

        for idx, column in enumerate(table_dict[key].columns):
            
            if (idx + 1 == len(table_dict[key].columns)):
                column_properties += column
            else:
                column_properties += column + ", "

        message += "# " + str(key) + column_properties + ")\n"

    message += "#\n# " + task + "\nSELECT"

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