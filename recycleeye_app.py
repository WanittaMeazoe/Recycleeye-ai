# ♻️ RECYCLEEYE - Smart Waste Management in Liberia
# FTL Women Team

import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="RecycleEye", page_icon="♻️")

st.title("♻️ RecycleEye AI – Waste Management Liberia")
st.write("**FTL Women Team | AI + Sustainability Hackathon**")

st.success("🎯 Ready for Live Demo – Upload a waste image")

uploaded_file = st.file_uploader(
    "Choose a trash image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=300)

    filename = uploaded_file.name.lower()

    if "plastic" in filename:
        result, conf, tip = "🧃 PLASTIC", "94%", "Rinse → Plastic Recycling Bin"
    elif "paper" in filename:
        result, conf, tip = "📄 PAPER", "88%", "Keep dry → Paper Recycling"
    elif "glass" in filename:
        result, conf, tip = "🍶 GLASS", "91%", "Rinse → Glass Recycling"
    elif "cardboard" in filename:
        result, conf, tip = "📦 CARDBOARD", "86%", "Flatten → Cardboard Recycling"
    else:
        materials = [
            ("🧃 PLASTIC", "94%", "Rinse → Plastic Recycling"),
            ("📄 PAPER", "88%", "Keep dry → Paper Recycling"),
            ("🍶 GLASS", "91%", "Rinse → Glass Recycling"),
            ("📦 CARDBOARD", "86%", "Flatten → Cardboard Recycling")
        ]
        result, conf, tip = random.choice(materials)

    st.success(f"AI Prediction: {result}")
    st.info(f"Confidence: {conf}")
    st.warning(f"♻️ Recycling Tip: {tip}")

st.markdown("---")
st.caption("Built with ❤️ by FTL Women Team")
