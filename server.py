# Import nessecary parts from flask and faker to generate random    # name and email.
from flask import Flask, request, jsonify
from faker import Faker
from flask_cors import CORS
import numpy as np
# To create and initialize a faker generator.
fake = Faker()
# Create the app object that will route our calls.
app = Flask(__name__)
CORS(app)
# Add a single endpoint that we can use as an API to accept GET and # POST requests.
@app.route("/highlight", methods=["POST", "GET"])

def computeHighlight():

    highlight = {}
    highlight["text"] = fake.paragraph(nb_sentences = 3, variable_nb_sentences = False)
    highlight["type"] = "delimiter"

    return jsonify(highlight)


# When run from command line, start the server.
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")