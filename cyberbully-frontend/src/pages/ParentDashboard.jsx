// src/pages/ParentDashboard.jsx
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const ParentDashboard = () => {
  const [email, setEmail] = useState(localStorage.getItem('userEmail') || '');
  const [phoneNumber, setPhoneNumber] = useState(localStorage.getItem('userPhone') || '');
  const [newPassword, setNewPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  const handleSaveDetails = () => {
    if (!email || !phoneNumber) {
      setErrorMessage('Please fill in both email and phone number.');
      return;
    }
    localStorage.setItem('userEmail', email);
    localStorage.setItem('userPhone', phoneNumber);
    setErrorMessage('');
    alert('Details saved successfully!');
  };

  const handleChangePassword = () => {
    navigate('/reset-password');
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md p-8 bg-white rounded-lg shadow-md space-y-6">
        <h2 className="text-3xl font-semibold text-center mb-6">Parent Dashboard</h2>

        {/* Display error message if there is any */}
        {errorMessage && <p className="text-red-500 text-sm">{errorMessage}</p>}

        <div className="mb-4">
          <label htmlFor="email" className="block text-sm font-medium text-gray-700">Email Address</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="mt-1 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
            required
          />
        </div>

        <div className="mb-4">
          <label htmlFor="phone" className="block text-sm font-medium text-gray-700">Phone Number</label>
          <input
            type="text"
            id="phone"
            value={phoneNumber}
            onChange={(e) => setPhoneNumber(e.target.value)}
            className="mt-1 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
            required
          />
        </div>

        <button
          onClick={handleSaveDetails}
          className="w-full bg-blue-500 text-white py-3 rounded-md hover:bg-blue-600 transition duration-200"
        >
          Save Contact Info
        </button>

        <button
          onClick={handleChangePassword}
          className="w-full mt-4 bg-yellow-500 text-white py-3 rounded-md hover:bg-yellow-600 transition duration-200"
        >
          Change Password
        </button>
      </div>
    </div>
  );
};

export default ParentDashboard;
