from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import cv2
import os
from flask_cors import CORS  # Enable CORS for React

app = Flask(__name__)
CORS(app)  # Allow frontend to call API

# Load the trained model
model = tf.keras.models.load_model("auto_claim_model.h5")

def preprocess_image(image_path):
    """Loads and preprocesses an image for model prediction."""
    img = cv2.imread(image_path)
    if img is None:
        return None

    img = cv2.resize(img, (224, 224))  # Ensure correct model input size
    img = img / 255.0  # Normalize pixels (0 to 1)
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

@app.route("/predict", methods=["POST"])
def predict():
    """Handles image upload and returns model prediction."""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    file_path = "temp_image.jpg"
    file.save(file_path)

    img = preprocess_image(file_path)
    if img is None:
        return jsonify({"error": "Invalid image file"}), 400

    # Make a prediction
    prediction = model.predict(img)
    confidence = float(prediction[0][0])  # Get prediction score

    # Adjust based on how model was trained
    is_damaged = confidence < 0.5  # Adjust threshold if needed

    result = "Damage Detected" if is_damaged else "No Damage (Whole Car)"
    
    return jsonify({
        "prediction": result,
        "confidence": round(confidence * 100, 2)  # Show as percentage
    })

if __name__ == "__main__":
    app.run(debug=True)
