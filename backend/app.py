from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # ✅ enable CORS

@app.route('/student-details', methods=['GET'])
def student_details():
    return jsonify({
        "name": "Yaswanth Sai Bhupalam",
        "roll_number": "BCD0057",
        "register_number": "2023BCD0057"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)