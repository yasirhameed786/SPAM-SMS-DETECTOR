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
        message = request.form['message']
    
        message_tfidf = vectorizer.transform([message])
        
        prediction = model.predict(message_tfidf)[0]
        
        result = "Spam" if prediction == 1 else "Not Spam"
        return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
