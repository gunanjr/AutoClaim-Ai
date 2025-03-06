import React, { useState } from "react";
import axios from "axios";

const UploadImage = () => {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [uploadStatus, setUploadStatus] = useState("");
  const [prediction, setPrediction] = useState("");

  const handleImageChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setImage(file);
      setPreview(URL.createObjectURL(file));
      setUploadStatus(""); // Reset status when a new image is selected
      setPrediction(""); // Reset prediction
    }
  };

  const handleUpload = async () => {
    if (!image) {
      setUploadStatus("Please select an image first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", image);

    try {
      const response = await axios.post("http://localhost:5000/predict", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      setUploadStatus("Upload successful!");
      setPrediction(response.data.prediction);
    } catch (error) {
      setUploadStatus("Error uploading image. Please try again.");
      console.error(error);
    }
  };

  return (
    <div className="p-6 flex flex-col items-center">
      <input type="file" onChange={handleImageChange} className="border p-2 rounded-md" />
      
      {preview && (
        <img
          src={preview}
          alt="Preview"
          className="mt-4 w-48 h-48 object-cover rounded-lg shadow-md"
        />
      )}
      
      <button
        onClick={handleUpload}
        className="mt-4 p-2 bg-blue-500 text-white rounded-lg hover:bg-blue-700"
      >
        Upload
      </button>
      
      {uploadStatus && <p className="mt-4 text-gray-700">{uploadStatus}</p>}
      {prediction && <p className="mt-4 text-lg font-semibold">{`Prediction: ${prediction}`}</p>}
    </div>
  );
};

export default UploadImage;
