from flask import Flask, request, jsonify
from faker import Faker
from flask_cors import CORS
import numpy as np

fake = Faker()
app = Flask(__name__)
CORS(app)

@app.route("/api/highlight", methods=["POST", "GET"])

def computeHighlight():
    meeting = request.get_json()
    # highlights = []
    
    # for section in meeting["sections"]:
    #     highlights.append(fake.paragraph(nb_sentences = 2, variable_nb_sentences = False))

    # print(highlights)
    highlight = fake.paragraph(nb_sentences = 2, variable_nb_sentences = False)
    return jsonify(highlight)
    
# When run from command line, start the server.
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
