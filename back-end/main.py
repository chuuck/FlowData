import pandas as pd

import os
import openai

file_path = "data/Stores.csv"

table_name = "Stores"


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

    print (response)


df = pd.read_csv(file_path)
task = "Sort out all data by descending order using store sales."
prompt = creates_message(list(df.columns), task)
print (api_request(prompt))











####### Example

### Postgres SQL tables, with their properties:
#
# Employee(id, name, department_id)
# Department(id, name, address)
# Salary_Payments(id, employee_id, amount, date)
#
### A query to list the names of the departments which employed more 


### Postgres SQL tables, with their properties:\n#\n# Employee(id, name, department_id)\n# Department(id, name, address)\n# Salary_Payments(id, employee_id, amount, date)\n#\n### A query to list the names of the departments which employed more than 10 employees in the last 3 months\nSELECT