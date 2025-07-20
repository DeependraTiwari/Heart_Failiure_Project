# Heart_Failiure_Project


# 💓 Heart Failure Prediction ML Project

A Machine Learning project that predicts the likelihood of heart failure using clinical records data. This project is part of the **DevTown Predictive Modelling Bootcamp**, and includes both model training and a Flask-based web application.

---

## 📂 Project Structure

```
heart_failure_project/
│
├── PredictiveModelAssignment.ipynb     # Model training notebook (Google Colab)
├── app.py                        # Flask app code
├── heart_model.pkl               # Trained ML model
├── scaler.pkl                    # Scaler used for input normalization
├── templates/
│   └── index.html                # Frontend UI for web app

README.md                     # Project documentation
```

---

## 🧠 Model Details

- **Model Used**: `Logical Regression`
- **Accuracy Achieved**: **80.00%**
- **Dataset**: `heart_failure_clinical_records_dataset.csv`
- **Input Features**:
  - age
  - anaemia
  - creatinine_phosphokinase
  - diabetes
  - ejection_fraction
  - high_blood_pressure
  - platelets
  - serum_creatinine
  - serum_sodium
  - sex
  - smoking
  - time

---

## 🚀 How to Run the Project

### 🔧 1. Train the Model
- Open the `.ipynb` file in Google Colab.
- Train using `Logical Regression` or any model of your choice.
- Save the model and scaler using `joblib`.

```python
joblib.dump(model, 'heart_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
```

---

### 🌐 2. Run the Flask App

```bash
pip install flask joblib
python app.py
```

- Open browser: `http://127.0.0.1:5000/`
- Input values and get prediction: **Low Risk** / **High Risk**

---

## 🧪 Sample Test Input

| Feature                    | Value |
|----------------------------|-------|
| age                        | 80    |
| anaemia                    | 1     |
| creatinine_phosphokinase   | 8000  |
| diabetes                   | 1     |
| ejection_fraction          | 20    |
| high_blood_pressure        | 1     |
| platelets                  | 150000|
| serum_creatinine           | 3.5   |
| serum_sodium               | 120   |
| sex                        | 1     |
| smoking                    | 1     |
| time                       | 5     |

---

## 🎨 Frontend Design

- Designed using **pure HTML + CSS**
- Modern UI with:
  - Gradient background
  - Rounded form fields
  - Responsive layout

---

## 📌 Key Dependencies

- `pandas`
- `scikit-learn`
- `xgboost` *(optional)*
- `flask`
- `joblib`
- `matplotlib` *(for visualization)*

---

## 👨‍💻 Author

**Deependraa Tiwari**

---

