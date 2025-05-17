from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Load the JSON data
with open('q-vercel-python.json', 'r') as file:
    students = json.load(file)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    if not names:
        return jsonify({"error": "No names provided"}), 400
    
    marks = []
    for name in names:
        for student in students:
            if student['name'] == name:
                marks.append(student['marks'])
                break
        else:
            marks.append(None)  # If name not found, append None
    
    return jsonify({"marks": [mark for mark in marks if mark is not None]})

if __name__ == '__main__':
    app.run(debug=True)