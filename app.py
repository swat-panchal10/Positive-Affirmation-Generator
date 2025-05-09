from flask import Flask, render_template, request, jsonify
from affirmations import get_affirmation

app = Flask(__name__)

@app.route("/")
def home():


    return render_template("index.html")

@app.route("/get-affirmation", methods=["POST"])
def get_affirmation_route():
    data = request.get_json()
    emotion = data.get("emotion", "").lower()
    response = get_affirmation(emotion)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
