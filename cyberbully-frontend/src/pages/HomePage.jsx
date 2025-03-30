import React, { useState, useEffect } from 'react';

const HomePage = () => {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/run-detection", {
      method: "POST"
    })
      .then(res => res.json())
      .then(data => {
        const result = data.alerts.map((msg, i) => ({
          id: i,
          message: msg.message,
          time: msg.timestamp.split("T")[1].slice(0, 5)
        }));
        setAlerts(result);
      })
      .catch(err => console.error("Error fetching alerts:", err));
  }, []);

  const handleReportBullying = () => {
    alert('Cyberbullying reported to parent!');
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gradient-to-r from-blue-100 to-indigo-200">
      <div className="w-full max-w-md p-6 bg-white rounded-xl shadow-xl space-y-8">

        {/* Alerts */}
        <div className="space-y-3">
          <h3 className="text-2xl font-semibold text-center text-gray-800">🚨 Recent Alerts</h3>
          <div className="bg-gray-50 border border-gray-200 rounded-lg p-4 shadow-inner max-h-40 overflow-y-auto">
            <ul className="list-decimal pl-5 space-y-2 text-gray-700 text-sm">
              {alerts.length > 0 ? alerts.map(alert => (
                <li key={alert.id} className="flex justify-between items-center">
                  <span>{alert.message}</span>
                  <span className="text-gray-400 text-xs">{alert.time}</span>
                </li>
              )) : <li className="text-gray-500 italic">No alerts yet</li>}
            </ul>
          </div>
        </div>

        {/* Divider */}
        <hr className="border-t border-gray-300" />

        {/* Report Button */}
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