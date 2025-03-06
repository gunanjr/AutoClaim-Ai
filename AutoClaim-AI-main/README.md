# AutoClaim AI

AutoClaim AI is a comprehensive AI-powered solution for vehicle damage assessment. It utilizes image analysis to detect and evaluate vehicle damage efficiently. The project features a modern frontend built with React and Vite, a backend powered by Flask and Express.js, and an AI model trained using TensorFlow and Keras.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
  - [Express.js Server Setup](#expressjs-server-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **AI-Powered Damage Assessment:** Uses TensorFlow and Keras to analyze vehicle damage from images.
- **Modern Frontend:** Built with React and Vite, styled with Tailwind CSS.
- **Robust Backend:** Flask for AI model serving and Express.js for additional backend functionalities.
- **Image Upload:** Users can upload images for damage analysis.
- **Thermal Scanner:** Detects internal vehicle issues using thermal imaging.

## Project Structure
```
AutoClaim AI/
│── frontend/       # React & Vite frontend
│── backend/        # Flask AI model serving
│── server/         # Express.js backend
│── models/         # AI models trained with TensorFlow & Keras
│── dataset/        # Training dataset for AI model
│── README.md       # Project documentation
```

## Installation

### Prerequisites
Make sure you have the following installed:
- Node.js
- Python 3.x
- TensorFlow
- MongoDB (for storing images)

### Backend Setup (Flask)
1. Navigate to the backend directory:
   ```sh
   cd backend
   ```
2. Install Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Flask server:
   ```sh
   python app.py
   ```

### Frontend Setup (React + Vite)
1. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
2. Install Node.js dependencies:
   ```sh
   npm install
   ```
3. Run the development server:
   ```sh
   npm run dev
   ```

### Express.js Server Setup
1. Navigate to the server directory:
   ```sh
   cd server
   ```
2. Install Node.js dependencies:
   ```sh
   npm install
   ```
3. Run the Express.js server:
   ```sh
   node server.js
   ```

## Usage
1. Open the frontend application in your browser:
   ```
   http://localhost:3000
   ```
2. Navigate to the **Analyze Damage** page.
3. Upload an image for damage assessment.
4. The Flask backend will process the image and return a prediction result.
5. View the prediction result and confidence score on the frontend.

## Contributing
Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

### Collaborators
- [Gunanjr](https://github.com/gunanjr)
- [Yuvraj Rajbanshi](https://github.com/YuvrajRajbanshi)

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, feel free to reach out or open an issue on GitHub.
