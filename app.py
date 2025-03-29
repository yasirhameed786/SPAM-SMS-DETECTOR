from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open('spam_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            message = request.form.get('message', '').strip()

            if not message:
                return render_template('index.html', error="⚠️ Please enter a message!")

            message_tfidf = vectorizer.transform([message])

            prediction = model.predict(message_tfidf)[0]
            result = "Spam" if prediction == 1 else "Not Spam"

            return render_template('index.html', prediction=result)

        except Exception as e:
            return render_template('index.html', error=f"❌ Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
