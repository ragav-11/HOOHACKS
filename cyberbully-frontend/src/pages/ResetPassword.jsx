// src/pages/ResetPassword.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const ResetPassword = () => {
  const [oldPassword, setOldPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  const handlePasswordReset = () => {
    const savedPassword = localStorage.getItem('userPassword');

    // Check if the old password matches the saved password
    if (oldPassword !== savedPassword) {
      setErrorMessage('Incorrect old password');
      return;
    }

    if (newPassword !== confirmPassword) {
      setErrorMessage('New passwords do not match');
      return;
    }

    // Save the new password to localStorage
    localStorage.setItem('userPassword', newPassword);
    setErrorMessage('');
    alert('Password reset successful');
    navigate('/parent-dashboard');
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md p-8 bg-white rounded-lg shadow-md space-y-6">
        <h2 className="text-3xl font-semibold text-center mb-6">Reset Password</h2>

        {errorMessage && <p className="text-red-500 text-sm">{errorMessage}</p>}

        <div className="mb-4">
          <label htmlFor="oldPassword" className="block text-sm font-medium text-gray-700">Old Password</label>
          <input
            type="password"
            id="oldPassword"
            value={oldPassword}
            onChange={(e) => setOldPassword(e.target.value)}
            className="mt-1 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
            required
          />
        </div>

        <div className="mb-4">
          <label htmlFor="newPassword" className="block text-sm font-medium text-gray-700">New Password</label>
          <input
            type="password"
            id="newPassword"
            value={newPassword}
            onChange={(e) => setNewPassword(e.target.value)}
            className="mt-1 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
            required
          />
        </div>

        <div className="mb-4">
          <label htmlFor="confirmPassword" className="block text-sm font-medium text-gray-700">Confirm New Password</label>
          <input
            type="password"
            id="confirmPassword"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            className="mt-1 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
            required
          />
        </div>

        <button
          onClick={handlePasswordReset}
          className="w-full bg-blue-500 text-white py-3 rounded-md hover:bg-blue-600 transition duration-200"
        >
          Reset Password
        </button>
      </div>
    </div>
  );
};

export default ResetPassword;
