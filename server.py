from flask import Flask, request, jsonify
from faker import Faker
from flask_cors import CORS
import numpy as np
import time
import json
import datetime

fake = Faker()
app = Flask(__name__)
CORS(app)

@app.route("/api/highlight", methods=["POST", "GET"])

def computeHighlight():
    meeting = request.get_json()
    # highlights = []
    
    # for section in meeting["sections"]:
    #     highlights.append(fake.paragraph(nb_sentences = 2, variable_nb_sentences = False))

    print(meeting)
    highlight = fake.paragraph(nb_sentences = 2, variable_nb_sentences = False)
    time.sleep(2)
    return jsonify(highlight)
    
@app.route("/api/deeptalk-transcript", methods=["POST"])

def seeTranscript():
    transcript = request.get_json()
    print(transcript)
    with open('../MeetingTool/static/transcript-' + str(datetime.datetime.now()) + '.json', 'w') as outfile:
        json.dump(transcript, outfile)
    return "ok"

# When run from command line, start the server.
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
