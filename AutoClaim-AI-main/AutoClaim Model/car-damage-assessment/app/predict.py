import tensorflow as tf
import numpy as np
import cv2
import sys

# Load trained model
model = tf.keras.models.load_model("auto_claim_model.h5")

# Function to predict damage or whole
def predict_damage(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))  # Resize to match training size
    img = img / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Reshape for model input

    # Prediction
    prediction = model.predict(img)[0][0]

    if prediction > 0.5:
        return "✅ No Damage (Whole Car)"
    else:
        return "🚨 Damage Detected"

# Run prediction
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict.py <image_path>")
    else:
        image_path = sys.argv[1]
        result = predict_damage(image_path)
        print(f"Prediction for {image_path}: {result}")
