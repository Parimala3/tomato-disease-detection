import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(page_title="Tomato Disease Detection", page_icon="🍅")
st.title("🍅 Tomato Leaf Disease Detection")
st.write("Upload a tomato leaf image to get prediction")

# -----------------------------
# Load model
# -----------------------------
MODEL_PATH = "tomato_disease_model.h5"

if not os.path.exists(MODEL_PATH):
    st.error("❌ Model file not found in project folder")
    st.stop()

model = tf.keras.models.load_model(MODEL_PATH)

# -----------------------------
# Upload image
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload Tomato Leaf Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess
    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)

    predicted_index = int(np.argmax(prediction))
    confidence = float(np.max(prediction)) * 100

    # -----------------------------
    # SAFE OUTPUT (NO LIST INDEXING)
    # -----------------------------
    st.success("✅ Prediction completed successfully")
    st.write(f"🧠 Predicted class index: **{predicted_index}**")
    st.write(f"📊 Confidence: **{confidence:.2f}%**")

    # Optional explanation
    st.info(
        "ℹ️ Class index corresponds to the trained dataset folder order.\n"
        "This avoids label mismatch errors."
    )
