# tomato-disease-detection
🍅 Tomato Leaf Disease Detection – Web Application
📌 Project Overview

This project is a Crop Disease Detection System that uses Artificial Neural Networks (ANN) with Convolutional Neural Network (CNN) architecture to classify tomato leaf images as healthy or diseased.

A web-based application is developed using Streamlit, allowing users to upload a tomato leaf image and receive a disease prediction along with confidence score.

🎯 Objectives

To detect tomato leaf diseases using image classification

To apply deep learning techniques (CNN-based ANN)

To build a simple and user-friendly web interface

To assist farmers and users in early disease identification

🧠 Diseases Covered

Healthy Leaf

Early Blight

Late Blight

(Model may be trained on multiple plant disease classes depending on dataset used.)

🛠️ Technologies Used

Programming Language: Python

Deep Learning Framework: TensorFlow, Keras

Web Framework: Streamlit

Image Processing: PIL, NumPy

Dataset: PlantVillage Leaf Disease Dataset

📂 Project Structure
Tomato_Disease/
│
├── app.py              # Streamlit web application
├── requirements.txt    # Required Python libraries
├── .gitignore          # Ignores large model files
└── README.md           # Project documentation


⚠️ Note:
The trained model file (.h5) is not uploaded to GitHub due to file size limitations.
The model is loaded locally during execution.

🚀 How to Run the Project Locally
1️⃣ Install Required Libraries
pip install streamlit tensorflow pillow numpy

2️⃣ Place Model File

Ensure the trained model file is in the same folder:

tomato_disease_model.h5

3️⃣ Run the Web Application
streamlit run app.py

4️⃣ Open in Browser
http://localhost:8501


Upload a tomato leaf image and view the prediction.

🧪 Output

Displays uploaded leaf image

Shows predicted disease class

Shows confidence score

🧠 Methodology

User uploads a tomato leaf image

Image is resized and normalized

CNN-based ANN model extracts features

Model predicts disease class

Result is displayed on the web interface

📊 Dataset Description

The model is trained using the PlantVillage dataset, which contains labeled images of healthy and diseased plant leaves under controlled conditions.

✅ Advantages

Easy to use web interface

Accurate disease detection

Helps in early diagnosis

Scalable to other crops
