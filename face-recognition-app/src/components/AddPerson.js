import React, { useState } from 'react';
import axios from 'axios';
import './AddPerson.css'; // Import the CSS file for styling

function AddPerson() {
  const [name, setName] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/add_person', { name });
      alert(response.data.message);
    } catch (error) {
      alert('Failed to add person');
    }
  };

  return (
    <div className="add-person-container">
      <h1>Add a New Person</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </label>
        <button type="submit" className="button">Add Person</button>
      </form>
    </div>
  );
}

export default AddPerson;