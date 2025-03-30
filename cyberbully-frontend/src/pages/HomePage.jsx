// src/pages/HomePage.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const HomePage = () => {
  const [alerts] = useState([{ id: 1, message: 'Cyberbullying detected!' }]);
  const [isParentControl, setIsParentControl] = useState(false);
  const navigate = useNavigate();

  const handleReportBullying = () => {
    alert('Cyberbullying reported to parent!');
  };

  const toggleParentControl = () => {
    setIsParentControl(!isParentControl);
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-50">
      <div className="w-full max-w-md p-8 bg-white rounded-lg shadow-lg space-y-6">
        <h2 className="text-3xl font-semibold text-center mb-6">Home Page</h2>

        <div className="mb-4">
          <h3 className="text-xl font-semibold mb-2">Recent Alerts</h3>
          <ul className="list-disc pl-5">
            {alerts.map((alert) => (
              <li key={alert.id} className="text-gray-700">{alert.message}</li>
            ))}
          </ul>
        </div>

        {/* Show this button only if not in Parent Control */}
        {!isParentControl && (
          <button
            onClick={handleReportBullying}
            className="w-full bg-green-500 text-white py-3 rounded-md hover:bg-green-600 transition duration-200"
          >
            Report Cyberbullying
          </button>
        )}

        <button
          onClick={() => navigate('/parent-login')}  // Navigate to the parent login page
          className="w-full mt-4 bg-yellow-500 text-white py-3 rounded-md hover:bg-yellow-600 transition duration-200"
        >
          Go to Parental Control
        </button>

        {/* If toggled to Parental Control */}
        {isParentControl && (
          <div className="mt-4">
            <button
              onClick={() => navigate('/parent-login')}
              className="w-full mt-2 bg-purple-500 text-white py-3 rounded-md hover:bg-purple-600 transition duration-200"
            >
              Go to Parent Login
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default HomePage;
