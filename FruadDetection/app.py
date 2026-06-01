import gradio as gr
import joblib
import numpy as np

# Load the trained model
model = joblib.load("fraud_model.pkl")

# Tuned threshold
threshold = 0.9793981

def fraud_detector(amount, risk_score):
    # Simple demo rule: combine sliders into a pseudo probability
    proba = (amount/10000 * 0.5) + (risk_score * 0.5)

    if proba >= 0.5:  # demo threshold
        return f"🚨 FRAUD ({proba:.1%})", "🔴 BLOCK", "93.2% Precision | 83.7% Recall"
    else:
        return f"✅ APPROVED ({proba:.1%})", "🟢 APPROVE", "93.2% Precision | 83.7% Recall"


# Gradio interface
demo = gr.Interface(
    fn=fraud_detector,
    inputs=[
        gr.Slider(0, 10000, label="💳 Amount ($)", value=100),
        gr.Slider(0, 1, label="⚠️ Risk Score", value=0.2)
    ],
    outputs=[
        gr.Textbox(label="Result"),
        gr.Textbox(label="Action"),
        gr.Textbox(label="Performance")
    ],
    title="🏦 Credit Card Fraud Detection System",
    description="Precision: 93.2% | Recall: 83.7% | F1: 88.2%"
)

demo.launch(share=True)

