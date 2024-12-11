import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css'; // Import the CSS file for styling

function Home() {
  return (
    <div className="home-container">
      <h1>Welcome to the Face Recognition App</h1>
      <Link to="/add-person" className="button">Add a New Person</Link>
      <br />
      <Link to="../../face_recognition_app.py" className="button">Start Face Recognition</Link>
    </div>
  );
}

export default Home;