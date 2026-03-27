# 🏥 Longitudinal Patient Health Risk Prediction System

### 📌 Diabetes & Cardiovascular Risk Monitoring (CDSS Prototype)

A data-driven clinical decision support system (CDSS) that analyzes **longitudinal patient health data** to predict disease risk and recommend follow-up care.

🔗 **Live App:** *https://longitudinal-health-risk-dashboard-dvg3en4tr9zzdgaehbfmic.streamlit.app/*
📂 **Tech Stack:** Python | Pandas | Scikit-learn | Streamlit | Matplotlib

---

# 🚀 Problem Statement

In real-world healthcare settings:

* Patient reports are fragmented across time
* Doctors manually interpret trends
* Early risk signals are often missed
* No automated system exists for **continuous risk monitoring**

👉 This project solves that by transforming static reports into **dynamic, time-aware health intelligence**

---

# 💡 Solution Overview

This system:

* Aggregates patient health records using a **unique patient ID**
* Engineers **temporal features** (trends, changes over time)
* Predicts **diabetes + cardiovascular risk**
* Provides **clinical recommendations**
* Displays results via an **interactive dashboard**

---

# 🧠 Key Features

### ✅ Longitudinal Data Analysis

* Captures patient history over time (not just single visit)
* Detects trends in HbA1c, BP, LDL, BMI

### ✅ Risk Prediction Model

* Logistic Regression (interpretable)
* Outputs:

  * Risk Probability
  * Risk Category (Low / Moderate / High)

### ✅ Clinical Recommendation Engine

* Hybrid system:

  * ML predictions + rule-based logic
* Example:

  * Rising HbA1c → endocrinology follow-up
  * Elevated BP → frequent monitoring

### ✅ Interactive Dashboard

* Select patient ID
* View:

  * Risk score
  * Health summary
  * Feature insights
  * Population-level distribution

---

# ⚙️ System Architecture

```
Raw Patient Data
        ↓
Data Aggregation (Patient ID)
        ↓
Feature Engineering (Trends, Slopes, Changes)
        ↓
Risk Prediction Model
        ↓
Recommendation Engine
        ↓
Streamlit Dashboard
```

---

# 📊 Features Engineered

* Mean HbA1c
* HbA1c trend (slope)
* Mean Blood Pressure
* BP trend
* Maximum LDL
* BMI change

These features capture **disease progression patterns over time**

---

# 📈 Model Performance

* **ROC-AUC Score:** 0.98

👉 Indicates strong predictive performance on the synthetic dataset

---

# 🖥️ Dashboard Preview

<img width="1920" height="918" alt="image" src="https://github.com/user-attachments/assets/880097d8-cc35-499f-81c6-f49c18e611b3" />
<img width="1920" height="922" alt="image" src="https://github.com/user-attachments/assets/a8b94f1e-d858-4177-ad0f-8db3911e0541" />

---

# 🛠️ Tech Stack

* **Python**
* **Pandas** → Data processing
* **Scikit-learn** → Model building
* **Matplotlib** → Visualization
* **Streamlit** → Web app deployment

---

# 📂 Project Structure

```
app.py                  # Streamlit application
patient_summary.csv     # Processed patient dataset
risk_model.pkl          # Trained ML model
requirements.txt        # Dependencies
```

---

# ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

# 🔬 Future Improvements

* 📈 Patient trend visualization (time-series plots)
* 🧠 Model explainability (SHAP)
* 📝 Manual input prediction mode
* 📊 Model calibration improvements
* 🏥 Integration with real EHR systems

---

# ⚠️ Disclaimer

This project is a **proof-of-concept (POC) prototype** built using simulated data for educational and demonstration purposes only.

It is not intended for real clinical use, diagnosis, or medical decision-making.

---

# 👩‍💻 Author

**Dyuthi Sai**
M.Tech Computational Biology → Data Science

---

# 🌟 Why This Project Matters

This project demonstrates:

* Longitudinal healthcare analytics
* Feature engineering on temporal data
* Interpretable ML in healthcare
* End-to-end system design
* Real-world problem solving

👉 Moving from *model building* to *product thinking*
