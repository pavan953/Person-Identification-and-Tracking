import React from 'react';
import axios from 'axios';
import './StartRecognition.css'; // Import the CSS file for styling

function StartRecognition() {
  const handleStart = async () => {
    try {
      const response = await axios.post('/api/start_recognition');
      alert(response.data.message);
    } catch (error) {
      alert('Failed to start face recognition');
    }
  };

  return (
    <div className="start-recognition-container">
      <h1>Start Face Recognition</h1>
      <button onClick={handleStart} className="button">Start</button>
    </div>
  );
}

export default StartRecognition;