
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Healthcare Risk CDSS",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🏥 Longitudinal Health Risk Prediction System")
st.markdown("### Diabetes & Cardiovascular Risk Monitoring (CDSS Prototype)")

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("patient_summary.csv")

df = load_data()

# -----------------------------
# Sidebar - Patient Selection
# -----------------------------
st.sidebar.header("🔎 Select Patient")
patient_id = st.sidebar.selectbox(
    "Patient ID",
    df["patient_id"].unique()
)

patient = df[df["patient_id"] == patient_id].iloc[0]

# -----------------------------
# Layout Columns
# -----------------------------
col1, col2, col3 = st.columns(3)

# -----------------------------
# Risk Overview Cards
# -----------------------------
with col1:
    st.metric("Risk Probability", f"{patient['risk_probability']:.2f}")

with col2:
    st.metric("Risk Category", patient["risk_category"])

with col3:
    if patient["risk_category"] == "High":
        st.error("⚠️ High Risk")
    elif patient["risk_category"] == "Moderate":
        st.warning("⚠️ Moderate Risk")
    else:
        st.success("✅ Low Risk")

# -----------------------------
# Recommendation Section
# -----------------------------
st.subheader("📋 Clinical Recommendation")
st.info(patient["recommendation"])

# -----------------------------
# Clinical Metrics Table
# -----------------------------
st.subheader("📊 Patient Health Summary")

metrics = pd.DataFrame({
    "Metric": [
        "Mean HbA1c",
        "HbA1c Trend",
        "Mean Blood Pressure",
        "BP Trend",
        "Max LDL",
        "BMI Change"
    ],
    "Value": [
        round(patient["mean_hba1c"],2),
        round(patient["hba1c_slope"],3),
        round(patient["mean_bp"],1),
        round(patient["bp_slope"],3),
        round(patient["max_ldl"],1),
        round(patient["bmi_change"],2)
    ]
})

st.dataframe(metrics, use_container_width=True)

# -----------------------------
# Feature Importance (Visual)
# -----------------------------
st.subheader("📈 Feature Importance Insight")

features = ["mean_hba1c","hba1c_slope","last_hba1c",
            "mean_bp","bp_slope","max_ldl","bmi_change"]

values = patient[features].values

fig, ax = plt.subplots()
ax.barh(features, values)
ax.set_title("Patient Feature Values")

st.pyplot(fig)

# -----------------------------
# Risk Distribution (Global Insight)
# -----------------------------
st.subheader("🌍 Population Risk Distribution")

risk_counts = df["risk_category"].value_counts()

fig2, ax2 = plt.subplots()
ax2.pie(risk_counts, labels=risk_counts.index, autopct='%1.1f%%')
ax2.set_title("Risk Category Distribution")

st.pyplot(fig2)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("⚠️ *This is a prototype clinical decision support system using simulated data.*")
