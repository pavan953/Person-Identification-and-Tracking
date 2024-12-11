import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import AddPerson from './components/AddPerson';
import StartRecognition from './components/StartRecognition';
import './App.css'; // Import the CSS file for styling

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/add-person" element={<AddPerson />} />
          <Route path="/start-recognition" element={<StartRecognition />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;