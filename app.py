import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# Mock function to simulate model training
def train_model(model_name):
    st.write(f"Training {model_name}...")
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.05)  # Simulate training time
        progress_bar.progress(i + 1)
    accuracy = np.random.uniform(85, 95)  # Random accuracy for demo
    st.success(f"{model_name} Training Complete! Accuracy: {accuracy:.2f}%")
    return accuracy

# Title
st.title("IMDb Sentiment Analysis GUI")

# Sidebar for model selection
st.sidebar.header("Select Model to Train")
models = ["BERT", "LSTM", "Logistic Regression", "XGBoost", "Linear SVM", "Naïve Bayes"]
selected_model = st.sidebar.selectbox("Choose a model:", models)

# Train Button
if st.sidebar.button("Train Model"):
    accuracy = train_model(selected_model)
    if "results" not in st.session_state:
        st.session_state["results"] = []
    st.session_state["results"].append({"Model": selected_model, "Accuracy": accuracy})

# Display Results
if "results" in st.session_state:
    st.subheader("Training Results")
    results_df = pd.DataFrame(st.session_state["results"])
    st.table(results_df)

    # Plot Accuracy
    st.subheader("Model Accuracy Comparison")
    fig, ax = plt.subplots()
    ax.bar(results_df["Model"], results_df["Accuracy"], color='skyblue')
    ax.set_xlabel("Models")
    ax.set_ylabel("Accuracy (%)")
    ax.set_title("Accuracy Comparison")
    st.pyplot(fig)

# Placeholder for detailed plots (mock training process)
if st.checkbox("Show Training Process for Accuracy and Loss"):
    epochs = list(range(1, 6))
    train_acc = np.random.uniform(80, 95, 5)
    val_acc = np.random.uniform(75, 90, 5)

    fig, ax = plt.subplots()
    ax.plot(epochs, train_acc, label="Training Accuracy", marker="o")
    ax.plot(epochs, val_acc, label="Validation Accuracy", marker="o", linestyle="--")
    ax.set_xlabel("Epochs")
    ax.set_ylabel("Accuracy (%)")
    ax.set_title("Training and Validation Accuracy")
    ax.legend()
    st.pyplot(fig)
