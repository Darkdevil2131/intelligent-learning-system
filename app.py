import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from hybrid_model import HybridModel

st.set_page_config(layout="wide")
st.title("AI Learning System")

@st.cache_resource
def load():
    model = HybridModel()
    score = model.train()
    return model, score

model, score = load()

st.sidebar.write(f"Model Score: {round(score,2)}")

# INPUT
st.header("📥 Input")

col1, col2 = st.columns(2)

with col1:
    studytime = st.slider("Study Time", 1, 4)
    failures = st.slider("Failures", 0, 3)
    absences = st.slider("Absences", 0, 30)

with col2:
    G1 = st.slider("G1", 0, 20)
    G2 = st.slider("G2", 0, 20)

history = st.text_input("Enter past scores (comma separated)", "10,12,14,15")

history = [int(x) for x in history.split(",") if x.strip().isdigit()]

if st.button("Predict"):

    result = model.predict(studytime, failures, absences, G1, G2, history)

    st.success(f"Final Prediction: {round(result['final'],2)}")

    st.write("### Breakdown")
    st.write(f"Random Forest: {round(result['rf'],2)}")
    st.write(f"LSTM Behavior Score: {round(result['lstm'],2)}")

    # Insight
    if result['final'] > 15:
        st.info("🔥 Strong student")
    elif result['final'] > 10:
        st.warning("⚠️ Moderate")
    else:
        st.error("❌ Needs improvement")

# GRAPH
st.header("📊 History Trend")

if len(history) > 0:
    fig, ax = plt.subplots()
    ax.plot(history, marker='o')
    ax.set_title("Performance Trend")
    st.pyplot(fig)