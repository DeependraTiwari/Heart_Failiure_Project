from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    final = scaler.transform([features])
    prediction = model.predict(final)
    result = "High Risk" if prediction[0] == 1 else "Low Risk"
    return render_template("index.html", prediction_text=f'Prediction: {result}')

if __name__ == "__main__":
    app.run(debug=True)
