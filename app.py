from flask import Flask, render_template, request, jsonify
import pickle

with open("model/spam_model.pkl", "rb") as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    message = data.get("message", "")
    prediction = model.predict([message])[0]
    return jsonify({"result": "Spam" if prediction == 1 else "Not Spam"})

if __name__ == "__main__":
    app.run(debug=True)
