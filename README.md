**Project Overview**
This project is an SMS Spam Detection System that classifies messages as spam or ham (not spam) using Machine Learning (Naïve Bayes Classifier). It provides a Flask-based web interface for users to input a message and get an instant spam detection result.

**Features**
# Machine Learning Model – Trained using TF-IDF Vectorization and Multinomial Naïve Bayes.
# Web-Based Interface – Built with Flask, HTML, CSS, and JavaScript.
# Real-time Classification – Users can check messages instantly.
# High Accuracy – Model trained with optimized text preprocessing.
# Responsive UI – Styled with modern and professional CSS.

**Tech Stack**
# Backend: Python, Flask, Scikit-learn, Pandas
# Frontend: HTML, CSS, JavaScript
# Machine Learning: TF-IDF Vectorization, Naïve Bayes Classifier

**Project Structure**
SpamSMS-Detection/
│─static/
│  ├─style.css        
│  ├─sms.png
│
│─templates/
│  ├─index.html        
│
│─spam.csv              
│─train_model.py
│─app.py              
│─spam_model.pkl      
│─vectorizer.pkl     
│─README.md           
│─requirements.txt     

**To Run**
1.Install Dependencies - pip install -r requirements.txt
2.Train the Model - python train_model.py
3.Run the Flask App - python app.py
4.Open http://127.0.0.1:5000/ in your browser

**Future Improvements**
# Deep Learning Model (LSTMs for better spam detection)
# User Authentication (Login-based spam analysis)
# Real-time API (Integration with messaging apps)
