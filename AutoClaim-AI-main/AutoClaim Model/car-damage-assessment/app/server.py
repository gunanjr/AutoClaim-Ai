from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import cv2

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Load the trained model
model = tf.keras.models.load_model("auto_claim_model.h5")

def preprocess_image(image):
    image = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
    image = cv2.resize(image, (224, 224))  # Resize to match model input
    image = image / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    image = request.files["file"]
    processed_image = preprocess_image(image)

    prediction = model.predict(processed_image)
    damage_probability = float(prediction[0][0])  # Adjust based on model output format

    return jsonify({"damage_probability": damage_probability})

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Runs on http://localhost:5000
