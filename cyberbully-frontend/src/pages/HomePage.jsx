import React, { useState } from 'react';

const HomePage = () => {
  const [alerts] = useState([
    { id: 1, message: 'Cyberbullying detected!', time: '2 min ago' },
    { id: 2, message: 'Cyberbullying detected!', time: '5 min ago' },
    { id: 3, message: 'Cyberbullying detected!', time: '12 min ago' }
  ]);

  const handleReportBullying = () => {
    alert('Cyberbullying reported to parent!');
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gradient-to-r from-blue-100 to-indigo-200">
      <div className="w-full max-w-md p-6 bg-white rounded-xl shadow-xl space-y-8">

        {/* Recent Alerts Section */}
        <div className="space-y-3">
          <h3 className="text-2xl font-semibold text-center text-gray-800">
            🚨 Recent Alerts
          </h3>
          <div className="bg-gray-50 border border-gray-200 rounded-lg p-4 shadow-inner max-h-40 overflow-y-auto">
            <ul className="list-decimal pl-5 space-y-2 text-gray-700 text-sm">
              {alerts.map((alert) => (
                <li key={alert.id} className="flex justify-between items-center">
                  <span>{alert.message}</span>
                  <span className="text-gray-400 text-xs">{alert.time}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>

        {/* Divider */}
        <hr className="border-t border-gray-300" />

        {/* Report Button Section */}
        <div className="bg-gray-50 rounded-lg p-4 shadow-inner text-center space-y-3">
          <h3 className="text-lg font-medium text-gray-800">📣 Need to report something?</h3>
          <button
            onClick={handleReportBullying}
            className="w-full bg-green-500 text-white py-3 rounded-md hover:bg-green-600 active:scale-95 transition duration-150"
          >
            Report Cyberbullying
          </button>
        </div>
        
      </div>
    </div>
  );
};

export default HomePage;