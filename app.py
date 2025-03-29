import os
import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

MODEL_PATH = "spam_model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"

if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    raise FileNotFoundError("Error: Model files are missing. Please upload 'spam_model.pkl' and 'vectorizer.pkl'.")

with open(MODEL_PATH, "rb") as model_file:
    model = pickle.load(model_file)

with open(VECTORIZER_PATH, "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        message = data.get("message", "")

        if not message:
            return jsonify({"error": "No message provided"}), 400

        transformed_message = vectorizer.transform([message])
        
        prediction = model.predict(transformed_message)[0]
        result = "Spam" if prediction == 1 else "Not Spam"

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
