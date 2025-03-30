// src/pages/ParentDashboard.jsx
import React from 'react';

const ParentDashboard = () => {
  return (
    <div className="flex justify-center items-center h-screen bg-gray-100">
      <div className="w-full max-w-md p-8 bg-white rounded-lg shadow-md">
        <h2 className="text-3xl font-semibold text-center mb-6">Parent Dashboard</h2>
        <div className="mb-4">
          <p>Update your email and password here</p>
          {/* Add form to change email/password later */}
        </div>
        <button className="w-full bg-red-500 text-white py-2 rounded-md">Log Out</button>
      </div>
    </div>
  );
};

export default ParentDashboard;
