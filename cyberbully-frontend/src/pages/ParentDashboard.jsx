import React, { useState } from 'react';

const ParentDashboard = ({ onLogout }) => {
  const [email, setEmail] = useState(localStorage.getItem('userEmail') || '');
  const [phoneNumber, setPhoneNumber] = useState(localStorage.getItem('userPhone') || '');
  const [newPassword, setNewPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

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
    alert('Redirecting to reset password page...');
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gradient-to-r from-blue-100 to-indigo-200">
      <div className="w-full max-w-md p-6 bg-white rounded-xl shadow-xl space-y-6">
        <h2 className="text-3xl font-semibold text-center text-gray-800">
          👨‍👩‍👧‍👦 Parent Dashboard
        </h2>

        {errorMessage && <p className="text-red-500 text-sm text-center">{errorMessage}</p>}

        <div className="space-y-4">
          <div>
            <label htmlFor="email" className="block text-sm font-medium text-gray-700">
              Email Address
            </label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="mt-1 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
              required
            />
          </div>

          <div>
            <label htmlFor="phone" className="block text-sm font-medium text-gray-700">
              Phone Number
            </label>
            <input
              type="text"
              id="phone"
              value={phoneNumber}
              onChange={(e) => setPhoneNumber(e.target.value)}
              className="mt-1 block w-full p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
              required
            />
          </div>
        </div>

        <div className="space-y-4 pt-2">
          <button
            onClick={handleSaveDetails}
            className="w-full bg-blue-500 text-white py-3 rounded-md hover:bg-blue-600 transition duration-200"
          >
            Save Contact Info
          </button>

          <button
            onClick={handleChangePassword}
            className="w-full bg-yellow-500 text-white py-3 rounded-md hover:bg-yellow-600 transition duration-200"
          >
            Change Password
          </button>

          <button
            onClick={onLogout}
            className="w-full bg-red-500 text-white py-3 rounded-md hover:bg-red-600 transition duration-200"
          >
            Log Out
          </button>
        </div>
      </div>
    </div>
  );
};

export default ParentDashboard;