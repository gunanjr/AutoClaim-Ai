import React, { useState } from "react";
import axios from "axios";

const UploadImage = () => {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState("");
  const [confidence, setConfidence] = useState("");

  const handleImageChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setImage(file);
      setPreview(URL.createObjectURL(file));
    }
  };

  const handleUpload = async () => {
    if (!image) {
      setResult("Please select an image first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", image);

    try {
      const response = await axios.post(
        "http://localhost:5000/predict", // Flask backend URL
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      );

      setResult(response.data.prediction);
      setConfidence(`Confidence: ${(response.data.confidence * 100).toFixed(2)}%`);
    } catch (error) {
      setResult("Error processing image.");
    }
  };

  return (
    <div className="p-6 flex flex-col items-center">
      <input type="file" onChange={handleImageChange} />
      {preview && (
        <img
          src={preview}
          alt="Preview"
          className="mt-4 w-48 h-48 object-cover rounded-lg shadow-md"
        />
      )}
      <button
        onClick={handleUpload}
        className="mt-4 p-2 bg-blue-500 text-white rounded-lg"
      >
        Upload
      </button>
      {result && <p className="mt-4">{result}</p>}
      {confidence && <p className="text-gray-600">{confidence}</p>}
    </div>
  );
};

export default UploadImage;
